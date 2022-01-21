# -*- coding: utf-8 -*-

"""
Created on Sat Jan 15 18:56:21 2022

@author: Irena Dragičević and Filip Ivić
"""

import cv2
import numpy as np
from scipy.spatial.distance import directed_hausdorff

img1 = cv2.imread("seg.jpg", 0)
img2 = cv2.imread("g_seg.jpg", 0)

edges1 = cv2.Canny(img1, 100,255)
edges2 = cv2.Canny(img2, 100,255)

indices1 = np.where(edges1 != [0])
indices2 = np.where(edges2 != [0])

coordinates1 = list(zip(indices1[1], indices1[0]))
coordinates2 = list(zip(indices2[1], indices2[0]))

#print(list(coordinates1))
#print(list(coordinates2))

u = np.array(coordinates1)

v = np.array(coordinates2)

a = directed_hausdorff(u, v)[0]

b = max(directed_hausdorff(u, v)[0], directed_hausdorff(v, u)[0])

print("Directed Hausdorff distance (in pixels): ", a)
print("Max Hausdorff distance (in pixels): ", b)