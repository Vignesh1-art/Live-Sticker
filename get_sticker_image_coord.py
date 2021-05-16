import cv2 as cv

def getCoord(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        print("x:",x," y:",y)
cv.namedWindow('sticker')
cv.setMouseCallback('sticker',getCoord)
path="C:\\Python Scripts\\Live sticker\\sticker images\\beard.png"
img=cv.imread(path)
cv.imshow('sticker',img)
cv.waitKey(0)