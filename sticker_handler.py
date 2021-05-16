import cv2 as cv
from math import sqrt
class StickerHandler:
    stickers=["eye_glasses.png","beard.png"]
    img=[]
    sticker_points={stickers[0]:[250,253,971,253],stickers[1]:[193,208,418,208]}
    def __init__(self,path):
        self.path=path
        for s in self.stickers:
            self.img.append(cv.imread(self.path+s,cv.IMREAD_UNCHANGED))
    @staticmethod
    def getDistance(p1,p2):
        xd=(p1[0]-p2[0])**2
        yd=(p1[1]-p2[1])**2
        return sqrt(xd+yd)
    
    @staticmethod
    def rescaleCoord(coord,new,old):
        Rx=new[0]/old[0]
        Ry=new[1]/old[1]
        return (round(Rx*coord[0]),round(Ry*coord[1]))
    
    def getSticker(self,sticker_id,p1,p2):
        lndmk_dist=StickerHandler.getDistance(p1,p2)
        sticker_point=self.sticker_points[self.stickers[sticker_id]]
        sp_dist=StickerHandler.getDistance(sticker_point[0:2],sticker_point[2:4])
        scale_factor=lndmk_dist/sp_dist
        img=self.img[sticker_id]
        w=img.shape[1]*scale_factor
        h=img.shape[0]*scale_factor
        dsize=(round(w),round(h))
        im=cv.resize(img,dsize)
        spoint=StickerHandler.rescaleCoord(sticker_point[0:2],dsize,(img.shape[1],img.shape[0]))
        return im,spoint

    @staticmethod
    def overlaySticker(frame,sticker):
        for i in range(frame.shape[0]):
            for j in range(frame.shape[1]):
                if sticker[i,j,0]!=0:
                    frame[i,j]=sticker[i,j,1:]
