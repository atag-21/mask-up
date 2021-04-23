# Usage: `python detect_mask.py --image <image.ext>`

# Supress tensorflow debug info
from os import environ as osenv
osenv["TF_CPP_MIN_LOG_LEVEL"] = "3"

# import relevant packages
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import cv2
import os

def ismasked(imagefile):

    # defaults
    edge_confidence = 0.5
    model_dir = "models"
    mask_model = model_dir + "/mask_detector.model"

    # load face detector model
    prototxtPath = os.path.sep.join([model_dir, "deploy.prototxt"])
    weightsPath = os.path.sep.join([model_dir,
        "res10_300x300_ssd_iter_140000.caffemodel"])
    net = cv2.dnn.readNet(prototxtPath, weightsPath)

    # load face mask detector model
    model = load_model(mask_model)

    # load input image from disk, clone it, and grab the image spatial
    # dimensions
    image = cv2.imread(imagefile)
    orig = image.copy()
    (h, w) = image.shape[:2]

    # construct a blob from the image
    blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300),
        (104.0, 177.0, 123.0))

    # pass the blob through the network and obtain the face detections
    net.setInput(blob)
    detections = net.forward()

    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with
        # the detection
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the confidence is
        # greater than the minimum confidence
        if confidence > edge_confidence:
            # compute the (x, y)-coordinates of the bounding box for
            # the object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # ensure the bounding boxes fall within the dimensions of
            # the frame
            (startX, startY) = (max(0, startX), max(0, startY))
            (endX, endY) = (min(w - 1, endX), min(h - 1, endY))

            # extract the face ROI, convert it from BGR to RGB channel
            # ordering, resize it to 224x224, and preprocess it
            face = image[startY:endY, startX:endX]
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            face = cv2.resize(face, (224, 224))
            face = img_to_array(face)
            face = preprocess_input(face)
            face = np.expand_dims(face, axis=0)

            # pass the face through the model to determine if the face
            # has a mask or not
            (mask, withoutMask) = model.predict(face)[0]
            if mask > withoutMask:
                f = open("maskyes", 'a')
                f.write("a")
                print("yes")
                return True
            else:
                f = open("maskno", 'a')
                f.write("b")
                print("no")
                return False