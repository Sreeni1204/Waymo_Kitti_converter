import os
import argparse
import sys
from Image_extractor import *
from Lidar_pointcloud_extractor import *
from Calibration_extractor import *
from Label_extractor import *

def File_names_and_path(source_folder):

    dir_list = os.listdir(source_folder)
    files = list()

    for directory in dir_list:

        path = os.path.join(source_folder, directory)

        if os.path.isdir(path):
            files = files + File_names_and_path(path)
        else:
            files.append(path)

    tf_files = [f for f in files if f.endswith('.' + 'tfrecord')]

    return tf_files

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--source', help = 'provide source path', type=str)
    parser.add_argument('--dest', help='provide destinaetion path', type=str)
    parser.add_argument('--velo',action="store_true", help='extract only lidar data points, calibration parameters and labels')
    parser.add_argument('--img',action="store_true", help='extract only camera images, calibration parameters and labels')
    parser.add_argument('--all',action="store_true", help='extract only lidar data points, camera images, calibration parameters and labels')


    args = parser.parse_args()

    source_folder = args.source
    dest_folder = args.dest


    # files = [f for f in os.listdir(source_folder)]
    # path = [os.path.join(source_folder, f) for f in files]
    path = File_names_and_path(source_folder)

    isExist = os.path.exists(os.path.join(dest_folder, 'Output'))

    if isExist:
        pass
    else:
        os.makedirs(os.path.join(dest_folder, "Output/Velodyne"))
        os.makedirs(os.path.join(dest_folder, "Output/Calibration/Calib_all"))
        os.makedirs(os.path.join(dest_folder, "Output/Labels/Label_all"))
        subfolder_names1 = ['Output/Labels/Label/0', 'Output/Labels/Label/1', 'Output/Labels/Label/2', 'Output/Labels/Label/3', 'Output/Labels/Label/4']
        for folder_name in subfolder_names1:
            os.makedirs(os.path.join(dest_folder, folder_name))
        subfolder_names1 = ['Output/Calibration/Calib/0', 'Output/Calibration/Calib/1', 'Output/Calibration/Calib/2', 'Output/Calibration/Calib/3', 'Output/Calibration/Calib/4']
        for folder_name in subfolder_names1:
            os.makedirs(os.path.join(dest_folder, folder_name))
        subfolder_names = ['Output/Camera/Front', 'Output/Camera/Front_left', 'Output/Camera/Side_left', 'Output/Camera/Front_right', 'Output/Camera/Side_right']
        for folder_name in subfolder_names:
            os.makedirs(os.path.join(dest_folder, folder_name))

    Front = os.path.join(dest_folder, "Output/Camera/Front/")
    Front_left = os.path.join(dest_folder, "Output/Camera/Front_left/")
    Side_left = os.path.join(dest_folder, "Output/Camera/Side_left/")
    Front_right = os.path.join(dest_folder, "Output/Camera/Front_right/")
    Side_right = os.path.join(dest_folder, "Output/Camera/Side_right/")
    lidar = os.path.join(dest_folder, "Output/Velodyne/")
    Calib_all = os.path.join(dest_folder, "Output/Calibration/Calib_all/")
    Calib = os.path.join(dest_folder, "Output/Calibration/Calib/")
    Label_all = os.path.join(dest_folder, "Output/Labels/Label_all/")
    Label = os.path.join(dest_folder, "Output/Labels/Label/")

    i, j, k, l = 0, 0, 0, 0
    print('Extraction process started:')

    if args.velo:
        for filename in path:

            j = point_cloud_extractor(j, filename, lidar)
            k = calibration_extractor(k, filename, Calib_all, Calib)
            l = label_extractor(l, filename, Label_all, Label)
            j = j
            k = k
            l = l

    if args.img:
        for filename in path:

            i = image_extractor(i, filename, Front, Front_left, Side_left, Front_right, Side_right)
            k = calibration_extractor(k, filename, Calib_all, Calib)
            l = label_extractor(l, filename, Label_all, Label)
            i = i
            k = k
            l = l
    
    if args.all:

        for filename in path:

            i = image_extractor(i, filename, Front, Front_left, Side_left, Front_right, Side_right)
            j = point_cloud_extractor(j, filename, lidar)
            k = calibration_extractor(k, filename, Calib_all, Calib)
            l = label_extractor(l, filename, Label_all, Label)
            i = i
            j = j
            k = k
            l = l

    print('Number of images extracted:', i)
    print('Number of point clouds extracted:', j)
    print('Number of calibration parameters extracted:', k)
    print('Number of labels extracted:', l)
    print('Extraction process complete:')