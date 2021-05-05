import cv2 as cv

class FaceLocalizer:
    def __init__(self,path):
        self.face_cascade=cv.CascadeClassifier(path)

    def getFace(self,img):
        d=self.face_cascade.detectMultiScale(img)
        return d