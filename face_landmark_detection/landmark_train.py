import numpy as np
import cv2 as cv
from tensorflow import keras
from Prepare_mmlab_ds import PrepareDataset
from landmark_model import LandmarkModel

path="C:\\Python Scripts\\Live Emoji\\face_landmark_detection\\dataset\\"
prepd=PrepareDataset(path,10000)
modelpath="C:\\Python Scripts\\Live Emoji\\face_landmark_detection\\saved_model"

x,y=prepd.getDataset(0,10000)
try:
    model=keras.models.load_model(modelpath)
except:
    model=LandmarkModel((40,40,3)).getModel()
    model.compile(optimizer='adam',loss='mse')
model.fit(x[0:9500],y[0:9500],batch_size=2,epochs=5,validation_data=(x[9500:10000],y[9500:10000]))
model.save(modelpath)
