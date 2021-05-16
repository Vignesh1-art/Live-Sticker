import cv2 as cv
from PyQt5.QtWidgets import QApplication
from gui import GUI
import sys
from threading import Thread
from sticker_handler import StickerHandler
from landmark_detection import LandmarkDetection

class Main:
    def __init__(self):
        self.ld=LandmarkDetection()
        self.stickers=StickerHandler("C:\\Python Scripts\\Live sticker\\sticker images\\")
        self.vc=cv.VideoCapture(0)
        self.cam_on=True

    
    def getFrames(self,gui):
        stk_id=0
        anchor="eye"
        while self.cam_on:
            cv.waitKey(20)
            _,frame=self.vc.read()
            landmark=self.ld.getLandmarks(frame)
            if(len(landmark)>0):
                if anchor=="eye":
                    p1=landmark[0:2]
                    p2=landmark[2:4]
                elif anchor=="mouth":
                    p1=landmark[6:8]
                    p2=landmark[8:10]
                stk_img,shift=self.stickers.getSticker(stk_id,p1,p2)
                x=p1[0]-shift[0]
                y=p1[1]-shift[1]
                subframe=frame[y:y+stk_img.shape[0],x:x+stk_img.shape[1]]
                StickerHandler.overlaySticker(subframe,stk_img)
            gui.setcurFrame(frame)
            gui.trigger.emit()
        self.vc.release()
        

    def shutdownCam(self):
        self.cam_on=False
        
    
if __name__=="__main__":
    main=Main()
    app=QApplication(sys.argv)
    gui=GUI()
    t=Thread(target=main.getFrames,args=[gui])
    t.start()
    app.exec_()
    main.shutdownCam()
    t.join()
sys.exit(0)