import cv2 as cv
import os
import numpy as np
from face_landmark_detection.landmark_predict import LandmarkPredict
from face_detection.face_localizer import FaceLocalizer
from PyQt5.QtWidgets import QApplication
from gui import GUI
import sys
from threading import Thread
from sticker_handler import StickerHandler
def rescaleCoord(coord,new,old):
    Rx=new[0]/old[0]
    Ry=new[1]/old[1]
    return (round(Rx*coord[0]),round(Ry*coord[1]))

def init():
    global vc,fl,lp,on_cam
    on_cam=True
    path=os.path.realpath("__file__")
    path=path[:-8]
    path='C:\\Python Scripts\\Live Emoji\\'
    lp=LandmarkPredict("C:\Python Scripts\Live sticker\models\saved_model")
    fl=FaceLocalizer()
    vc=cv.VideoCapture(0)
    global sticker
    sticker=StickerHandler("C:\\Python Scripts\\Live sticker\\sticker images\\")

def getLandmarks(frame):
    bbox=fl.getFace(frame)
    if len(bbox)>0:
        x,y,w,h=bbox[0],bbox[1],bbox[2],bbox[3]
        face=frame[y:y+h,x:x+w]
        sface=cv.resize(face,(40,40))
        sface=sface/255.0
        points=lp.getLandmarks(sface)[0]
        del sface
        for i in range(0,10,2):
            point=(int(points[i]),int(points[i+1]))
            point=rescaleCoord(point,(w,h),(40,40))
            points[i],points[i+1]=point[0]+x,point[1]+y
        return points
    else:
        return np.array([])

def getFrames(gui_object):
    while on_cam:
        _,frame=vc.read()
        landmarks=getLandmarks(frame)
        if not len(landmarks)==0:
            leye=landmarks[0:2]
            reye=landmarks[2:4]
            stk,shift=sticker.getSticker(0,leye,reye)
            x=int(leye[0])-shift[0]
            y=int(leye[1])-shift[1]+10
            subframe=frame[y:y+stk.shape[0],x:x+stk.shape[1]]
            StickerHandler.overlaySticker(subframe,stk)

        gui_object.setcurFrame(frame)
        gui_object.trigger.emit()
        cv.waitKey(15)

if __name__=="__main__":
        init()
        app=QApplication(sys.argv)
        gui=GUI()
        t=Thread(target=getFrames,args=[gui])
        t.start()
        app.exec_()
        on_cam=False
        t.join()
sys.exit(0)