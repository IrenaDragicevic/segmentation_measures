# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 18:45:12 2022

@author: Irena Dragicevic
"""

from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import img_as_float, img_as_ubyte, io
import numpy as np
from matplotlib import pyplot as plt
import cv2

img = img_as_float(io.imread("./test_img2.jpg"))

sigma_est = np.mean(estimate_sigma(img, multichannel=True))
denoise = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode = True, patch_size=5, patch_distance=3, multichannel=True)
denoise_ubyte = img_as_ubyte(denoise)

#uncomment the line if you want the histogram, comment the next plt
plt.hist(denoise_ubyte.flat, bins = 100, range = (0, 256))

segm1 = (denoise_ubyte <=20)
segm2 = ((denoise_ubyte > 20) & (denoise_ubyte <= 82))
segm3 = ((denoise_ubyte > 82) & (denoise_ubyte <= 180))
segm4 = (denoise_ubyte >= 180)

#create a blank image of the same shape, fill it with 0s
all_segments = np.zeros((denoise_ubyte.shape[0], denoise_ubyte.shape[1], 3))
all_segments[segm1] = (0, 0, 0) #black
all_segments[segm2] = (0, 1, 0) #green
all_segments[segm3] = (0, 0, 1) #blue
all_segments[segm4] = (1, 1, 0) #yellow

#cleaning up stray pixels
from scipy import ndimage as nd
segm1_opened = nd.binary_opening(segm1, np.ones((3,3)))
segm1_closed = nd.binary_closing(segm1_opened, np.ones((3,3)))
segm2_opened = nd.binary_opening(segm2, np.ones((3,3)))
segm2_closed = nd.binary_closing(segm2_opened, np.ones((3,3)))
segm3_opened = nd.binary_opening(segm3, np.ones((3,3)))
segm3_closed = nd.binary_closing(segm3_opened, np.ones((3,3)))
segm4_opened = nd.binary_opening(segm4, np.ones((3,3)))
segm4_closed = nd.binary_closing(segm4_opened, np.ones((3,3)))
all_segments_cleaned = np.zeros((denoise_ubyte.shape[0], denoise_ubyte.shape[1], 3))
all_segments_cleaned[segm1_closed] = (0, 0, 0) #black
all_segments_cleaned[segm2_closed] = (0, 1, 0) #green
all_segments_cleaned[segm3_closed] = (0, 0, 1) #blue
all_segments_cleaned[segm4_closed] = (1, 1, 0) #yellow
#plt.imshow(all_segments_cleaned) 

plt.imsave("./histogram_segmented_test2.jpg", all_segments_cleaned)