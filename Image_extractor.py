import numpy as np
import tensorflow as tf
import itertools
import math
import os
import cv2
# add v2 compability 
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

tf.enable_eager_execution()

import waymo_open_dataset
from waymo_open_dataset.utils import range_image_utils
from waymo_open_dataset.utils import transform_utils
from waymo_open_dataset.utils import  frame_utils
from waymo_open_dataset import dataset_pb2 as open_dataset


def image_extractor(i ,filename, Front, Front_left, Side_left, Front_right, Side_right):

    FileName = filename
    dataset = tf.data.TFRecordDataset(FileName, compression_type='')

    for data in dataset:
        frame = open_dataset.Frame()
        frame.ParseFromString(bytearray(data.numpy()))

        for index, image in enumerate(frame.images):

            i_str = '{0:06}'.format(i)
            ima = tf.image.decode_jpeg(image.image).numpy()
            if index == 0:
                cv2.imwrite(os.path.join(Front, "%s.png")%(i_str), cv2.cvtColor(ima, cv2.COLOR_RGB2BGR))
                continue
            if index == 1:
                cv2.imwrite(os.path.join(Front_left, "%s.png")%(i_str), cv2.cvtColor(ima, cv2.COLOR_RGB2BGR))
                continue
            if index == 2:
                cv2.imwrite(os.path.join(Side_left, "%s.png")%(i_str), cv2.cvtColor(ima, cv2.COLOR_RGB2BGR))
                continue
            if index == 3:
                cv2.imwrite(os.path.join(Front_right, "%s.png")%(i_str), cv2.cvtColor(ima, cv2.COLOR_RGB2BGR))
                continue
            if index == 4:
                cv2.imwrite(os.path.join(Side_right, "%s.png")%(i_str), cv2.cvtColor(ima, cv2.COLOR_RGB2BGR))
                # continue
            
        i = i+ 1
    return i


