from mtcnn_cv2 import MTCNN

class LandmarkDetection:
    def __init__(self):
        self.model=MTCNN()
    
    def getLandmarks(self,img):
        faces=self.model.detect_faces(img)
        if(len(faces)==0):
            return []
        face=faces[0]
        keypoints=face['keypoints']
        landmark=[]
        for key in keypoints:
            x,y=keypoints[key]
            landmark.append(x)
            landmark.append(y)
        #landmark:leye,reye,nose,lmouth,rmouth
        return landmark
