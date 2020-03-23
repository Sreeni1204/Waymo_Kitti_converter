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

    parser.add_argument('--source_folder', help = 'provide source path', type=str)
    parser.add_argument('--destination_folder', help='provide destinaetion path', type=str)

    args = parser.parse_args()

    source_folder = args.source_folder
    dest_folder = args.destination_folder

    # files = [f for f in os.listdir(source_folder)]
    # path = [os.path.join(source_folder, f) for f in files]
    path = File_names_and_path(source_folder)

    isExist = os.path.exists(os.path.join(dest_folder, 'Camera'))
    isExist1 = os.path.exists(os.path.join(dest_folder, 'Velodyne'))
    isExist2 = os.path.exists(os.path.join(dest_folder, 'Calibration'))
    # isExist3 = os.path.exists(os.path.join(dest_folder, 'Label_all'))
    isExist3 = os.path.exists(os.path.join(dest_folder, 'Labels'))
    if isExist and isExist1 and isExist2 and isExist3:
        pass
    else:
        os.makedirs(os.path.join(dest_folder, "Velodyne"))
        os.makedirs(os.path.join(dest_folder, "Calibration/Calib_all"))
        # os.makedirs(os.path.join(dest_folder, "Label_all"))
        os.makedirs(os.path.join(dest_folder, "Labels/Label_all"))
        subfolder_names1 = ['Labels/Label/0', 'Labels/Label/1', 'Labels/Label/2', 'Labels/Label/3', 'Labels/Label/4']
        for folder_name in subfolder_names1:
            os.makedirs(os.path.join(dest_folder, folder_name))
        subfolder_names1 = ['Calibration/Calib/0', 'Calibration/Calib/1', 'Calibration/Calib/2', 'Calibration/Calib/3', 'Calibration/Calib/4']
        for folder_name in subfolder_names1:
            os.makedirs(os.path.join(dest_folder, folder_name))
        subfolder_names = ['Camera/Front', 'Camera/Front_left', 'Camera/Side_left', 'Camera/Front_right', 'Camera/Side_right']
        for folder_name in subfolder_names:
            os.makedirs(os.path.join(dest_folder, folder_name))

    Front = os.path.join(dest_folder, "Camera/Front/")
    Front_left = os.path.join(dest_folder, "Camera/Front_left/")
    Side_left = os.path.join(dest_folder, "Camera/Side_left/")
    Front_right = os.path.join(dest_folder, "Camera/Front_right/")
    Side_right = os.path.join(dest_folder, "Camera/Side_right/")
    lidar = os.path.join(dest_folder, "Velodyne/")
    Calib_all = os.path.join(dest_folder, "Calibration/Calib_all/")
    Calib = os.path.join(dest_folder, "Calibration/Calib/")
    Label_all = os.path.join(dest_folder, "Labels/Label_all/")
    Label = os.path.join(dest_folder, "Labels/Label/")

    i, j, k, l = 0, 0, 0, 0
    print('Extraction process started:')
    
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