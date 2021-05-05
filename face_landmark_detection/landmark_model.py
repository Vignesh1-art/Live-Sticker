import tensorflow as tf
from tensorflow.keras import layers,models

class LandmarkModel:
    def __init__(self,inp_shape):
        self.model = models.Sequential()
        self.model.add(layers.Conv2D(16, (5, 5), activation='relu', input_shape=inp_shape))#l1
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Conv2D(48, (3, 3), activation='relu'))
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Conv2D(64, (2, 2), activation='relu'))
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(100,activation='relu'))
        self.model.add(layers.Dense(10))

    def getModel(self):
        return self.model

