import cv2 as cv
from mtcnn_cv2 import MTCNN
class FaceLocalizer:
    def __init__(self):
        self.model=MTCNN()
    
    def getFace(self,img):
        faces=self.model.detect_faces(img)
        if len(faces)<=0:
            return []
        face=faces[0]
        b=face['box']
        x,y,w,h=b[0],b[1],b[2],b[3]
        return [x,y,w,h]