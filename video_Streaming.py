import cv2

class Video(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
        self.count=0
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret,frame=self.video.read() 
        ret,jpg=cv2.imencode('.jpg',frame,Compress(50))
        self.count +=1
        
        return jpg.tobytes()





def Compress(value):
    return [int(cv2.IMWRITE_JPEG_QUALITY), value]

