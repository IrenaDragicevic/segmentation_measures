# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 19:15:15 2022

@author: Irena
"""
import nibabel as nib
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage as nd
from scipy.ndimage.filters import gaussian_filter

flair_img = nib.load ("./Brats18_2013_2_1_flair.nii")

flair_data = np.copy(flair_img.get_data())
flair_data = flair_data.astype(np.float64)
slice_z = flair_data[:, :, 108]
plt.imsave("./z_slice_v2.jpg", slice_z)
#change sigma if you like
gaussian_slice_z = gaussian_filter(slice_z, sigma=1)
plt.imsave("./Gaussian_z_slice_v2.jpg", gaussian_slice_z)
#normalize if you have to
gaussian_slice_z_ubyte = gaussian_slice_z.astype(np.uint8)

#plotting the histogram, uncomment if you need it
plt.hist(gaussian_slice_z_ubyte.flat, bins = 100, range = (0, 256))

segm1 = (gaussian_slice_z_ubyte <=1)
segm2 = ((gaussian_slice_z_ubyte > 1) & (gaussian_slice_z_ubyte <= 150))
segm3 = ((gaussian_slice_z_ubyte > 150) & (gaussian_slice_z_ubyte <= 175))
segm4 = (gaussian_slice_z_ubyte >= 175)

#create a blank image of the same shape, fill it with 0s
all_segments = np.zeros((gaussian_slice_z_ubyte.shape[0], gaussian_slice_z_ubyte.shape[1], 3))
all_segments[segm1] = (0, 0, 0) #black
all_segments[segm2] = (0, 1, 0) #green
all_segments[segm3] = (0, 0, 1) #blue
all_segments[segm4] = (1, 1, 0) #yellow

#cleaning up stray pixels
segm1_opened = nd.binary_opening(segm1, np.ones((3,3)))
segm1_closed = nd.binary_closing(segm1_opened, np.ones((3,3)))
segm2_opened = nd.binary_opening(segm2, np.ones((3,3)))
segm2_closed = nd.binary_closing(segm2_opened, np.ones((3,3)))
segm3_opened = nd.binary_opening(segm3, np.ones((3,3)))
segm3_closed = nd.binary_closing(segm3_opened, np.ones((3,3)))
segm4_opened = nd.binary_opening(segm4, np.ones((3,3)))
segm4_closed = nd.binary_closing(segm4_opened, np.ones((3,3)))
all_segments_cleaned = np.zeros((gaussian_slice_z_ubyte.shape[0], gaussian_slice_z_ubyte.shape[1], 3))
all_segments_cleaned[segm1_closed] = (0, 0, 0) #black
all_segments_cleaned[segm2_closed] = (0, 1, 0) #green
all_segments_cleaned[segm3_closed] = (0, 0, 1) #blue
all_segments_cleaned[segm4_closed] = (1, 1, 0) #yellow
#plt.imshow(all_segments_cleaned) 
plt.imsave("./nifti_segm_v2.jpg", all_segments_cleaned)



