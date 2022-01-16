//Measuring of the whole image area
selectWindow("Ground truth_segmentacija_inverted.tif");
print("Our Segmentation Measures");
run("Select All");
getStatistics(area, mean, min, max, std);
print("Whole Image Area", area);
run("Select None");

//Measuring ground truth and our segmentation mask area

//ground truth area
setAutoThreshold("Default");
//run("Threshold...");
run("Create Selection");
roiManager("Add");
roiManager("Select", 0);
roiManager("Rename", "gr_t_inv");
getStatistics(area, mean, min, max, std);
print("gr_t_inv area ", area);

//our segmentation mask area
selectWindow("Moja level sets segmentacija_inverted.tif");
//run("Threshold...");
run("Create Selection");
roiManager("Add");
roiManager("Select", 1);
roiManager("Rename", "ls");
getStatistics(area, mean, min, max, std);
print("ls area ", area);

//measuring overlap

roiManager("Select", newArray(0,1));
roiManager("AND");
roiManager("Add");
roiManager("Select", 2);
roiManager("Rename", "overlap");
getStatistics(area, mean, min, max, std);
print("Overlap ", area);

//measuring the union of two segmentations
roiManager("Select", 0);
roiManager("Select", newArray(0,1));
roiManager("Combine");
roiManager("Add");
roiManager("Select", 3);
roiManager("Rename", "Union");
getStatistics(area, mean, min, max, std);
print("Union area ", area);

