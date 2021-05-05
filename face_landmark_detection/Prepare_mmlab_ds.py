import cv2 as cv
import numpy as np
from math import ceil
class PrepareDataset:
    def __init__(self,path,size):
        self.cur_shape=(160,216)
        self.new_shape=(40,40)
        self.path=path
        self.annotations=open(self.path+'trainImageList.txt')
        self.ann_list=[]
        for i,a in enumerate(self.annotations):
            if(i==size):
                break
            temp=a.split()
            self.ann_list.append(temp)

    
    @staticmethod
    def rescaleCoord(coord,new,old):
        Rx=new[0]/old[0]
        Ry=new[1]/old[1]
        return round(Rx*coord[0]),round(Ry*coord[1])
    

    def getLandmarks_and_Rect(self,index):
        temp=self.ann_list[index]
        im_name=temp[0]
        landmarks=temp[1:]
        landmarks=[ceil(float(i)) for i in landmarks]
        bbox=landmarks[0:4]
        return im_name,landmarks[4:],bbox
    
    def getFace_and_Landmarks(self,index):
        im_id,lm,b=self.getLandmarks_and_Rect(index)
        x1,y1=b[0],b[3]
        x2,y2=b[1],b[2]
        img=cv.imread(self.path+im_id)
        crp_im=img[y2:y1,x1:x2]
        #tranform landmark points to local crp_im points
        for i in range(0,10,2):
            x=lm[i]
            y=lm[i+1]
            x=x-x1
            y=y-y2
            lm[i]=x
            lm[i+1]=y
        return crp_im,lm
    
    def getDataset(self,start,end):
        x=[]
        y=[]
        for i in range(start,end):
            img,landmarks=self.getFace_and_Landmarks(i)
            for j in range(0,10,2):
                x1,y1=PrepareDataset.rescaleCoord(landmarks[j:j+2],self.new_shape,img.shape)
                landmarks[j]=x1
                landmarks[j+1]=y1
            img=cv.resize(img,self.new_shape)
            x.append(img)
            y.append(landmarks)
        x=np.array(x)
        y=np.array(y)
        x=x/255.0
        return x,y
    
    def test(self,x,y):
        for i in range(0,10,2):
            point=(round(y[i]),round(y[i+1]))
            x=cv.circle(x,point, radius=0, color=(0, 255, 0), thickness=-1)
        x=cv.resize(x,(500,500))
        cv.imshow('test',x)
        cv.waitKey(0)