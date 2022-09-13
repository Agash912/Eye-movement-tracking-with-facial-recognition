import cv2
import numpy as np
import face_recognition
from imager.img_to_val import image_to_values

class face_recog:
    
    def recog(self):
        self.imgelon_rgb,self.imgelon = image_to_values('dataset')
        face = face_recognition.face_locations(self.imgelon_rgb)[0]
        copy = self.imgelon.copy()
        cv2.rectangle(copy, (face[3], face[0]),(face[1], face[2]), (255,0,255), 2)
        cv2.imshow('Face Identification', copy)
        #cv2.imshow('agash',imgelon)
        #cv2.waitKey(0)
