from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QGridLayout,QHBoxLayout
from PyQt5.QtGui import QPixmap
import cv2 as cv
from PyQt5.QtCore import pyqtSignal,Qt
from PyQt5 import QtGui


class GUI(QWidget):
    trigger=pyqtSignal()
    stk_id=0
    def __init__(self):
        super().__init__()      
        self.setGeometry(0,0,1000,600)
        self.trigger.connect(self.updateFrame)
        self.setupVideoView()

        hLayout = QHBoxLayout()
        hLayout.addWidget(self.image)
        hLayout.addLayout(self.getButtonLayout())
        self.setLayout(hLayout)
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

    def setupVideoView(self):
        self.image=QLabel()
        im=cv.imread('C:\\Python Scripts\\Live sticker\\sticker images\\cam.png')
        img=self.convert_cv_qt(im)
        self.image.setPixmap(img)
        self.image.setStyleSheet( "padding-top : 20px;"
                                   "padding-left:20px;"
                                   "padding-right:10px;"
                                   "padding-bottom :5px;")
    
    def eyeglassesClicked(self):
        self.stk_id=0

    def beardClicked(self):
        self.stk_id=1

    def getButtonLayout(self):
        grid=QGridLayout()
        eye_glasses=QPushButton("Eye Glasses")
        beard=QPushButton("Beard")
        grid.addWidget(eye_glasses,0,0)
        grid.addWidget(beard,0,1)


        eye_glasses.clicked.connect(self.eyeglassesClicked)
        beard.clicked.connect(self.beardClicked)
        return grid
