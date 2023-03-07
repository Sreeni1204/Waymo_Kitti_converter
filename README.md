# Scripts for extracting data from Waymo Open Dataset to Kitti format

> Author: **Sreenivasa Hikkal Venugopala**
>
> Contact: **hvsreenivasa93@gmail.com**
## Update
+ (March, 2023) mention that the origin tool doesn't compatible with tensorflow v2, we add tensorflow v2 capability for this version.
## Instruction
1. Clone the repository [Scripts](https://github.com/Sreeni1204/Waymo_Kitti_converter.git).
2. Requirements: Install following libraries
	1. Tensorflow 1.15.0 
	2. waymo-open-dataset
	3. OpenCV-python
	
3. Download the Waymo open dataset and extract the content into a folder.
4. Run the following command - 
"python Waymo_to_kitti.py --source=path/to/tfrecord_data_folder --dest=path/to/extract/data --all"
	1. Provided with more command line options to generate
	```
	"--velo" - velodyne lidar points with option with camera calibration and labels
	"--img" - camera images with option with camera calibration and labels
	"--all" - to generate lidar, images, camera calibration and labels.
	"--oclu" - to generate lidar, images, camera calibration and labels with basic occlusion information.
	```
	
5. Output folders will have following sructure under destination folder.

``` 
.
Output
├── Calibration
│   └── Calib
│   	├── 0
│   	├── 1
│   	├── 2
│   	├── 3
│   	└── 4
│   └── Calib_all
├── Camera
│   ├── Front
│   ├── Front_left
│   ├── Front_right
│   ├── Side_left
│   └── Side_right
├── Labels
│   └── Label
│   	├── 0
│   	├── 1
│   	├── 2
│   	├── 3
│   	└── 4
│   └── Labels_all
└── Velodyne

```

## Info on Data

### Cameras

Waymo has 5 cameras -  Front, Front_left, Front_right, Side_left, Side_right. Each is assigned with values from 0 to 4.


### Label

***Under construction***

Consists of two sub folders.
1. Labels - consists of labels for each individual cameras and folder names denotes what camera the label belongs. The number is mentiond in camera section.
2. Labels_all - consists of all label in single file.

Labels in kitti format with basic occlusion information as follows:
1. occlusion level 1 - for occluded objects.
2. occlusion level 0 - for non occluded objects.

All in vehicle frame.


### Calib

Consists of two sub folders.
1. Calib - consists of calibration for each individual cameras and folder names denotes what camera the label belongs. The number is mentiond in camera section.
2. Calib_all - consists of all calibrations in single file.


```
P0-P4 : intrinsic matrix for each camera
R0_rect : rectify matrix
Tr_velo_to_cam_0 - Tr_velo_to_cam_4 : transformation matrix from vehicle frame to camera frame
```


### Lidar

Point cloud in vehicle frame.

```
x y z reflectance
```

## References

1. [Waymo open dataset](https://github.com/waymo-research/waymo-open-dataset)
2. [Waymo_Kitti_Adapter](https://github.com/RocketFlash/Waymo_Kitti_Adapter)
3. [simple-waymo-open-dataset-reader](https://github.com/gdlg/simple-waymo-open-dataset-reader)
