import numpy as np
import tensorflow as tf
import itertools
import math
import os

tf.enable_eager_execution()

import waymo_open_dataset
from waymo_open_dataset.utils import range_image_utils
from waymo_open_dataset.utils import transform_utils
from waymo_open_dataset.utils import  frame_utils
from waymo_open_dataset import dataset_pb2 as open_dataset
from Adapter_utilities import *


def point_cloud_extractor(i, filename, lidar):

    FileName = filename
    dataset = tf.data.TFRecordDataset(FileName, compression_type='')

    for data in dataset:

        i_str = '{0:06}'.format(i)

        frame = open_dataset.Frame()
        frame.ParseFromString(bytearray(data.numpy()))

        (range_images, range_image_top_pose) = parse_range_image_and_camera_projection(frame)

        points, reflectence = convert_range_image_to_point_cloud(frame,range_images,range_image_top_pose)

        points_all = np.concatenate(points, axis=0)
        reflectence_all = np.concatenate(reflectence, axis=0)

        point_cloud = np.column_stack((points_all, reflectence_all))

        file_path = os.path.join(lidar, "%s.bin"%(i_str))

        point_cloud.tofile(file_path)

        i = i + 1

    return i