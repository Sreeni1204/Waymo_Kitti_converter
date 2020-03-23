import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as im
import tensorflow as tf
import itertools
import math
import os
import argparse
import sys

tf.enable_eager_execution()

import waymo_open_dataset
from waymo_open_dataset.utils import range_image_utils
from waymo_open_dataset.utils import transform_utils
from waymo_open_dataset.utils import  frame_utils
from waymo_open_dataset import dataset_pb2 as open_dataset


def calibration_extractor(i, filename, Calib):

    FileName = filename
    dataset = tf.data.TFRecordDataset(FileName, compression_type='')

    for data in dataset:

        i_str = '{0:06}'.format(i)

        frame = open_dataset.Frame()
        frame.ParseFromString(bytearray(data.numpy()))

        file_path = os.path.join(Calib, "%s.txt"%(i_str))

        f_open = open(file_path, 'w+')

        waymo_cam_RT = np.array([0,-1,0,0,  0,0,-1,0,   1,0,0,0,    0 ,0 ,0 ,1]).reshape(4,4)
        calib_cam = []
        R0_rect = ["%e"%a for a in np.eye(3).flatten()]
        Tr_velo_to_cam = []
        calib_context = ''

        for camera in frame.context.camera_calibrations:
            tmp=np.array(camera.extrinsic.transform).reshape(4,4)
            tmp=np.linalg.inv(tmp).reshape((16,))
            Tr_velo_to_cam.append(["%e" % i for i in tmp])

        for cam in frame.context.camera_calibrations:
            tmp=np.zeros((3,4))
            tmp[0,0]=cam.intrinsic[0]
            tmp[1,1]=cam.intrinsic[1]
            tmp[0,2]=cam.intrinsic[2]
            tmp[1,2]=cam.intrinsic[3]
            tmp[2,2]=1
            tmp=(tmp @ waymo_cam_RT)
            tmp=list(tmp.reshape(12))
            tmp = ["%e" % a for a in tmp]
            calib_cam.append(tmp)

        for a in range(5):
            calib_context += "P" + str(a) + ": " + " ".join(calib_cam[a]) + '\n'
        calib_context += "R0_rect" + ": " + " ".join(R0_rect) + '\n'
        for a in range(5):
            calib_context += "Tr_velo_to_cam_" + str(a) + ": " + " ".join(Tr_velo_to_cam[a]) + '\n'
        f_open.write(calib_context)
        f_open.close()


        i = i + 1
    return i