from PyQt5.QtWidgets import QApplication, QWidget,QLabel
from PyQt5.QtGui import QPixmap,QImage
import cv2 as cv
from PyQt5.QtCore import pyqtSignal, QObject,Qt
import sys
from threading import Thread
from PyQt5 import QtGui, QtCore
import time

class GUI(QWidget):
    trigger=pyqtSignal()
    def __init__(self):
        super().__init__()      
        self.setGeometry(0,0,1000,600)
        self.image=QLabel(self)
        im=cv.imread('C:\\Python Scripts\\Live sticker\\sticker images\\cam.png')
        img=self.convert_cv_qt(im)
        self.image.setPixmap(img)
        self.image.setStyleSheet( "padding-top : 20px;"
                                   "padding-left:20px;"
                                   "padding-right:10px;"
                                   "padding-bottom :5px;")
        self.trigger.connect(self.updateFrame)
        self.show()
    
    def setcurFrame(self,frame):
        self.cur_frame=self.convert_cv_qt(frame)
    
    def updateFrame(self):
        self.image.setPixmap(self.cur_frame)
    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv.cvtColor(cv_img, cv.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(600,400, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
