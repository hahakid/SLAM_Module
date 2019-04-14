# SLAM_Module

## preprocessor
### ground filter
1. linefit
2. heightDiff in gridMap

#### result:
original frame, points num:124668
![](image/origin_img.png) 

linefit(take scan ID < 40 as ROI), points num:46977
![](image/removeGRound_linefit40.png)

linefit(take scan ID < 50 as ROI), points num:33524
![](image/removeGRound_linefit50.png)

heightDiff in gridMap, thre = 0.5, points num:34983
![](image/removeGRound_gridMapHeightDiff0_5.png)

heightDiff in gridMap, thre = 0.3, points num:34983
![](image/removeGRound_gridMapHeightDiff0_3.png)

### segmentation
