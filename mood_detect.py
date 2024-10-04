from capture import capture
import cv2 as cv
from deepface import DeepFace
class SaveAndProcess:
    def __init__(self):
        self.cap=capture()
    def process(self,filename="test.png"):
        frame=self.cap.click()
        if frame is None:
            return
        cv.imwrite(filename,frame)


pic=SaveAndProcess()
pic.process()
