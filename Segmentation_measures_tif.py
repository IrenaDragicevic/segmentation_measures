
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 16:53:43 2022
runfile('Segmentation_measures_tif.py', args='Moja_level_sets_segmentacija.tif Ground_truth_segmentacija.tif')
runfile('Segmentation_measures_tif.py', args='Moja_level_sets_segmentacija.tif Moja_level_sets_segmentacija.tif')

@author: filipivic and irenadragicevic
"""

from apeer_ometiff_library import io
from matplotlib import pyplot as plt
import sys
import glob
import os

#def tiff_difference_finder(img1_path, img2_path, img3_path, img4_path):
def tiff_difference_finder(img1_path, img2_path):
    (img1, metadata) = io.read_ometiff("./" + img1_path)
    (img2, metadata) = io.read_ometiff("./" + img2_path)
    
    intersection1 = img1 - img2
    intersection2 = img2 - img1
    union = img1 + img2

    resolution = img1.size
    
    img1_pixels = 0
    img2_pixels = 0
    intersection1_pixels = 0
    intersection2_pixels = 0
    union_pixels = 0
    
    for arrays1 in img1:
        for arrays2 in arrays1:
            for arrays3 in arrays2:
                for arrays4 in arrays3:
                    for pixels in arrays4:
                        if (pixels > 200):
                            img1_pixels = img1_pixels +1
    
    for arrays1 in img2:
        for arrays2 in arrays1:
            for arrays3 in arrays2:
                for arrays4 in arrays3:
                    for pixels in arrays4:
                        if (pixels > 200):
                            img2_pixels = img2_pixels +1
                            
    for arrays1 in union:
        for arrays2 in arrays1:
            for arrays3 in arrays2:
                for arrays4 in arrays3:
                    for pixels in arrays4:
                        if (pixels > 200):
                            union_pixels = union_pixels +1                        
                                                                      
    for arrays1 in intersection1:
        for arrays2 in arrays1:
            for arrays3 in arrays2:
                for arrays4 in arrays3:
                    for pixels in arrays4:
                        if (pixels > 200):
                            intersection1_pixels = intersection1_pixels +1
                            
    for arrays1 in intersection2:
        for arrays2 in arrays1:
            for arrays3 in arrays2:
                for arrays4 in arrays3:
                    for pixels in arrays4:
                        if (pixels > 200):
                            intersection2_pixels = intersection2_pixels +1
                            
                            
    ###########################-Ispis Grafova-################################   
    
    for arrays1 in img1:
        for arrays2 in arrays1:
            for arrays3 in arrays2:
                plt.imshow(arrays3, interpolation="nearest")
                plt.show()
                
    for arrays1 in img2:
        for arrays2 in arrays1:
            for arrays3 in arrays2:
                plt.imshow(arrays3, interpolation="nearest")
                plt.show()
                
    for arrays1 in union:
        for arrays2 in arrays1:
            for arrays3 in arrays2:
                plt.imshow(arrays3, interpolation="nearest")
                plt.show()               
                                     
    for arrays1 in intersection1:
        for arrays2 in arrays1:
            for arrays3 in arrays2:
                plt.imshow(arrays3, interpolation="nearest")
                plt.show()
                
    for arrays1 in intersection2:
        for arrays2 in arrays1:
            for arrays3 in arrays2:
                plt.imshow(arrays3, interpolation="nearest")
                plt.show()
    
    print('\n')
    print("Program successfully executed!")
    print("\n")
    
    print("Image resolution is: " + str(resolution) + " pixels")
    print("The ground truth segmentation " + img1_path[:-5] + " has: " + str(img1_pixels) + " pixels")
    print("Your segmentation mask " + img2_path[:-5] + " has: " + str(img2_pixels) + " pixels")
    print("\n")
    
    print("The union of two segmentations has: " + str(union_pixels) + " pixels")
    print("The overlap of two segmentations has: " + str(union_pixels - (intersection1_pixels + intersection2_pixels)) + " pixels")
    print("\n")
    
    print("The surface remainder of the overlap from image " + img1_path[:-5] + " with segmentation mask from image " + img2_path[:-5] + " has: " + str(intersection1_pixels) + " pixels")
    print("The surface remainder of the overlap from image " + img2_path[:-5] + " with segmentation mask from image " + img1_path[:-5] + " has: " + str(intersection2_pixels) + " pixels")
    print("\n")
    print("Overlap percentage: " + str((union_pixels - (intersection1_pixels + intersection2_pixels))/union_pixels * 100) + "%")
    
    """
    num1=float(str(resolution))
    num2=float(str(img1_pixels))
    num3=float(str(img2_pixels))
    num4=float(str(union_pixels)) - (float(str(intersection1_pixels)) + float(str(intersection2_pixels)))
    num5=float(str(union_pixels))
    num6=num1-num5
    num7=num3-num4
    num8=num2-num4
    num9=num4/(num4+num7)
    num10=num6/(num6+num7)
    num11=(2*num4)/(num2+num3)
    """


    num1=float(resolution)
    num2=float(img1_pixels)
    num3=float(img2_pixels)
    num4=float(union_pixels) - (float(intersection1_pixels) + float(intersection2_pixels))
    num5=float(union_pixels)
    num6=num1-num5
    num7=num3-num4
    num8=num2-num4
    num9=num4/(num4+num7)
    num10=num6/(num6+num7)
    num11=(2*num4)/(num2+num3)

    print("True positive area", num4)
    print("True negative area: ", num6)
    print("False positive area:", num8)
    print("False negative area: ", num7)

    print("Sensitivity: ", num9)
    print("Specificity: ", num10)
    print("Dice-Sorensen Coefficient: ", num11)
    
                   
    
        
   
if __name__ == '__main__':
    
    program = sys.argv[0]
    
    img1_path = sys.argv[1]
    img2_path = sys.argv[2]
    
    names = [os.path.basename(name) for name in glob.glob("*")]
    if img1_path and img2_path in names:
        tiff_difference_finder(img1_path, img2_path)
        
    else:
        print("Wrong image names!!!")              
    
    print('\n')