# segmentation_measures

The goal of the histogram_segmentation_v6 program is to use and quantify a thresholding 
method on a set of BraTS 2020 images. The images were converted to jpg using Fiji,
meaning that each stack (coming from a single patient) was converted to 155 individual
jpg images that were stored into a directory by the name of flair for flair sequences
and seg for images previously annotated by radiologists. Each directory has 15 folders
(named flair01, etc.), each containing 155 images for an individual patient.

The flair images are then segmented using an Otsu thresholding method and stored
into the flair_seg directory. The ground-truth images also have to be modified using
histogram segmentation so that they could be worked on and as such, are stored into
the seg_hist folder. 

The program was made specifically to work with images of white tumors on a black
background and most likely cannot be used for anything except the whole-tumor (WT)
volume.

The second part of the program is used to compare the images segmented with Otsu to
the ground truth images. It allows for the calculation of resolution, ground truth/
Otsu-segmented area, true positive, true negative, false positive, false negative
and union area, sensitivity, specificity, Dice-Sorensen coefficient and Hausdorff
distance. The calculated values are then exported into an Excel file.
