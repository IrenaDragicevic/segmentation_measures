# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 18:33:02 2022

@author: Irena

Part of the histogram segmentation that focuses on comparing our segmentation
and the ground truth. The output are measures that we want presented.
Accuracy = TP+TN / TP + TN + FP + FN
Precision = TP / TP + FP
Recall or sensitivity = TP / TP + FN
Specificity =TN / FP + FN
Dice-Sorensen Coefficient = 2 * TP / 2 * TP + FP + FN
"""

import cv2
import os
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage.filters import threshold_multiotsu
from skimage import img_as_float, img_as_ubyte, io
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage import measurements

directory_flair_hist = 'flair_hist'
directory_seg_hist = 'seg_hist'
directory_flair = 'flair'


my_array_seg_hist = []
my_array_flair_hist = []
my_array_flair = []
flair_counter = 0
flair_img_counter = 0


for subdir, dirs, files in os.walk(directory_flair):
    for file in files:
        #print os.path.join(subdir, file)
      
        filepath = subdir + os.sep + file

        if filepath.endswith(".jpg"):
            #you have to change the os.sep slashes into / if you're working on windows
            #because the os.sep slashes were made on onyx
            sub_path = subdir[6:]
            img_path = './flair/' + sub_path + '/' + file
            print (img_path)
            #load img as float
            img = img_as_float(io.imread(img_path))
            my_array_flair.append(img)
           
            #choosing the slice if you wish for slice #83 because imgs in my directory start from 0000
            #but you have to keep it out of the for loops
            #img02 = my_array[83]

            #we have to do some denoising
            sigma_est = np.mean(estimate_sigma(img, multichannel=True))
            denoise = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode = True, patch_size=5, patch_distance=3, multichannel=True)
            #we'll turn the images back to ubyte so that the histogram makes some sense
            denoise_ubyte = img_as_ubyte(denoise)
            #if you want to see the convoluted image
            #plt.imshow(denoise, cmap = 'gray')
            
            
            if measurements.mean(denoise_ubyte) > 0:
                thresholds = threshold_multiotsu(denoise_ubyte, classes = 3)
                regions = np.digitize(denoise_ubyte, bins = thresholds)
                segm1 = (regions == 0)
                segm2 = (regions == 1)
                segm3 = (regions == 2)
                all_segments = np.zeros((denoise_ubyte.shape[0], denoise_ubyte.shape[1], 3))
                all_segments[segm1] = (0, 0, 0)
                all_segments[segm2] = (0, 0, 0)
                all_segments[segm3] = (1, 1, 1)
                
                
                #making the title for the new segmented files so we can use them later on
                l = len(file)
                img_save_path = './flair_hist/' + sub_path + '/' + file [:l-8] + '_hist_' + file [l-8:]
                #print (img_save_path)
                
                
                #saving the images
                plt.imsave(img_save_path, all_segments)
                
           
print ("Done with multi-Otsu! :)")


for subdir, dirs, files in os.walk(directory_flair_hist):
    for image in files:

      
        filepath = subdir + os.sep + image

        if filepath.endswith(".jpg"):
            sub_path = subdir[11:]
            img_path = './flair_hist/' + sub_path + '/' + image
            
            img = cv2.imread(img_path)

            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            (thresh, black_and_white_img) = cv2.threshold(gray_img, 40, 255, cv2.THRESH_BINARY)
            my_array_flair_hist.append(black_and_white_img)
            
        flair_img_counter += 1
            
    flair_counter += 1
    print ("Done loading " + subdir + " folder from " + directory_flair_hist)
            
print ("Done with loading flair_hist segmented images! :)")


for subdir, dirs, files in os.walk(directory_seg_hist):
    for image in files:
      
        filepath = subdir + os.sep + image

        if filepath.endswith(".jpg"):
            sub_path = subdir[9:]
            img_path = './seg_hist/' + sub_path + '/' + image
            
            img = cv2.imread(img_path)
            
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            (thresh, black_and_white_img) = cv2.threshold(gray_img, 40, 255, cv2.THRESH_BINARY)
            my_array_seg_hist.append(black_and_white_img)
            
print ("Done with loading seg_hist segmented images! 3:)")

a = int(flair_img_counter/(flair_counter - 1))
b = int(flair_counter - 1)

for i in range(b):
    for number in range(a):
        
        img_flair =  my_array_flair_hist[i * 155 + number]
        img_seg = my_array_seg_hist[i * 155 + number]
        
        intersection1 = img_flair - img_seg
        intersection2 = img_seg - img_flair
        union = img_flair + img_seg
        
        resolution = img_flair.size
        
        img_flair_pixels = 0
        img_seg_pixels = 0
        intersection1_pixels = 0
        intersection2_pixels = 0
        union_pixels = 0
        
    
        for row in img_flair:
            for pixels in row:
                if (pixels > 240):
                    img_flair_pixels = img_flair_pixels + 1
                
        print("Img_flair " + str(number) + " has " + str(img_flair_pixels) + " pixels")
                
        for row in img_seg:
            for pixels in row:
                if (pixels > 240):
                    img_seg_pixels = img_seg_pixels + 1
     
        print("Img_seg " + str(number) + " has " + str(img_seg_pixels) + " pixels")
    
        for row in union:
            for pixels in row:
                if (pixels > 240):
                    union_pixels = union_pixels + 1   
               
        print("Union " + str(number) + " has " + str(union_pixels) + " pixels")
    
        for row in intersection1:
            for pixels in row:
                if (pixels > 240):
                    intersection1_pixels = intersection1_pixels + 1
                
        for row in intersection2:
            for pixels in row:
                if (pixels > 240):
                    intersection2_pixels = intersection2_pixels + 1 
    
        print("Intersection " + str(number) + " has " + str(union_pixels - (intersection1_pixels + intersection2_pixels)) + " pixels")
        
        print("folder:" + str(i+1))
        
        
       
        if img_seg_pixels == 0:
            num1=float(resolution)
            num2=0
            num3=0
            num4=0
            num5=0
            num6=float(resolution)
            num7=0
            num8=0
            num9=0
            num10=1
            num11=0
            print("True positive area", num4)
            print("True negative area ", num6)
            print("False positive area", num8)
            print("False negative area ", num7)
        
            print("Sensitivity or Recall ", num9)
            print("Specificity ", num10)
            print("Dice-Sorensen Coefficient ", num11) 
 
            

        else: 
            num1=float(resolution)
            num2=float(img_seg_pixels)
            num3=float(img_flair_pixels)
            num4=float(union_pixels - (intersection1_pixels + intersection2_pixels))
            num5=float(union_pixels)
            num6=num1-num5
            num7=num2-num4
            num8=num3-num4
            num9=num4/(num4+num7)
            num10=num6/(num6+num8)
            num11=(2*num4)/(2*num4+num8+num7)
                         
            print("True positive area", num4)
            print("True negative area", num6)
            print("False positive area", num8)
            print("False negative area", num7)
        
            print("Sensitivity or Recall", num9)
            print("Specificity", num10)
            print("Dice-Sorensen Coefficient", num11) 
            
        