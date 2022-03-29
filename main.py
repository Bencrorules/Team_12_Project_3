import numpy as np
import cv2

# ~ Credits ~
# Models: https://github.com/richzhang/colorization/tree/caffe/colorization/models
# Points: https://github.com/richzhang/colorization/blob/caffe/colorization/resources/pts_in_hull.npy

# sets the files in root to some variable names
modelPath = 'dummy.caffemodel'
protoPath = 'colorization_deploy_v2.prototxt'
kernelPath = 'pts_in_hull.npy'
imagePath = 'cat.jpeg'

# 
neuralNetwork = cv2.dnn.readNetFromCaffe(protoPath, modelPath)
