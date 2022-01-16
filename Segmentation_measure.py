# -*- coding: utf-8 -*-
"""
This is a script made for calculating the specificity, sensitivity and Dice-Sorensen score of a segmentation.
"""
import math 
num1=float(input("Insert whole image area: "))
num2=float(input("Insert ground truth segment area: "))
num3=float(input("Insert your segmentation area: "))
num4=float(input("Insert overlap area: "))
num5=float(input("Insert union of two segmentations: "))
num6=num1-num5
num7=num3-num4
num8=num2-num4
num9=num4/(num4+num7)
num10=num6/(num6+num7)
num11=(2*num4)/(num2+num3)


print("True positive area", num4)
print("True negative area: ", num6)
print("False positive area:", num7)
print("False negative area: ", num7)

"""
Sensitivity=true positives/(true positives+false negatives)
Specificity=true negatives/(true negatives+false positives)
DSC=2*overlap/area of ground truth mask + area of our segmentation mask
"""
print("Sensitivity: ", num9)
print("Specificity: ", num10)
print("Dice-Sorensen Coefficient: ", num11)

