import numpy as np
import cv2 as cv
from tensorflow import keras

class LandmarkPredict:
    def __init__(self,path):
        self.model=keras.models.load_model(path)
    
    def getLandmarks(self,face):
        shape=face.shape
        face=np.reshape(face,(1,shape[0],shape[1],3))
        landmarks=self.model.predict(face)
        return np.round_(landmarks)
