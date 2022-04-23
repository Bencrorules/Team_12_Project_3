import numpy as np
import cv2

# ~ Credits ~
# Models: https://github.com/richzhang/colorization/tree/caffe/colorization/models
# Points: https://github.com/richzhang/colorization/blob/caffe/colorization/resources/pts_in_hull.npy

def colorize(image):

    # sets the files in root to some variable names
    modelPath = 'colorization_release_v2.caffemodel'
    protoPath = 'colorization_deploy_v2.prototxt'
    kernelPath = 'pts_in_hull.npy'
    imagePath = image

    # calls a function within the pre-trained neural network using our various imported files
    neuralNetwork = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

    # the following few lines are copied/slightly edited from OpenCV Documentation of kernel manipulation
    points = np.load(kernelPath)
    # defines the size of the point/kernel to be 1x1
    points = points.transpose().reshape(2, 313, 1, 1)
    # obtains the type of color restoration we'll be using. in this case it'll be LAB instead of your typical RGB
    neuralNetwork.getLayer(neuralNetwork.getLayerId("class8_ab")).blobs = [points.astype(np.float32)]
    neuralNetwork.getLayer(neuralNetwork.getLayerId("conv8_313_rh")).blobs = [np.full([1, 313], 2.606, dtype="float32")]

    # original code - image manipulation to allow neural network to comprehend
    # loads our selected image into a variable through the OpenCV function imread
    bwImage = cv2.imread(imagePath)
    # normalizes the image to values between 0 and 1 instead of 0 to 255
    normalizedImage = bwImage.astype("float32") / 255.0
    # converts image data to the LAB formatting our imported neural network is trained on
    labImageData = cv2.cvtColor(normalizedImage, cv2.COLOR_BGR2LAB)

    # resizes the image data to fit the 224x224 canvas the imported neural network is trained on
    resizedImage = cv2.resize(labImageData, (224, 224))
    # sets new constant as a split from the image. reduced by the mean lightness level, can be played with for dif results
    lightness = cv2.split(resizedImage)[0]
    lightness -= 50

    # imports lightness data into the neural network and receives data back stored into variable ab
    neuralNetwork.setInput(cv2.dnn.blobFromImage(lightness))
    ab = neuralNetwork.forward()[0,:,:,:].transpose((1,2,0))

    # resizes the data back to the original pictures dimensions
    ab = cv2.resize(ab, (bwImage.shape[1], bwImage.shape[0]))
    lightness = cv2.split(labImageData)[0]

    # converts our newly obtained ab data back into RGB for image display
    colorizedImage = np.concatenate((lightness[:, :, np.newaxis], ab), axis=2)
    colorizedImage = cv2.cvtColor(colorizedImage, cv2.COLOR_LAB2BGR)
    colorizedImage = (255.0 * colorizedImage).astype("uint8")

    # saves the newly created image and sends it off
    filename = 'finalImage.jpg'
    cv2.imwrite(filename, colorizedImage)
    return filename
