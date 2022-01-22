import cv2
class Video(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret,frame=self.video.read()
        ret,jpg=cv2.imencode('.jpg',frame)
        return jpg.tobytes()









# import fractions
# import cv2

# video=cv2.VideoCapture(0)

# faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# print(faceDetect)
# while True:
#     ret,frame=video.read()
#     print(ret)
#     positions=faceDetect.detectMultiScale(frame,1.3,5)
#     for x,y,w,h in positions:
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2)
#     cv2.imshow('Frame',frame)
#     k=cv2.waitKey(1)
#     if k==ord('q'):
#         break
# video.release()
# cv2.destroyAllWindows()
