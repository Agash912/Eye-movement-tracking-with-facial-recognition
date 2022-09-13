import cv2
import face_recognition
import os

class im_val:

    def image_to_values(self,p):
        path=p
        a=os.listdir(path)
        path = (path+a[0])
        imgelon_bgr = face_recognition.load_image_file(path)
        imgelon_rgb = cv2.cvtColor(imgelon_bgr,cv2.COLOR_BGR2RGB)
        # cv2.imshow('bgr', imgelon_bgr)
        # cv2.imshow('rgb', imgelon_rgb)
        # cv2.waitKey(0)
        imgelon =face_recognition.load_image_file(path)
        imgelon = cv2.cvtColor(imgelon,cv2.COLOR_BGR2RGB)
        return imgelon_rgb,imgelon
    
    def encoder(self,path):
        self.path = path
        images = []
        classNames = []
        mylist = os.listdir(path)
        for cl in mylist:
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])
        return images,classNames
    
    def findEncodings(self,path):
        self.path = path
        images,classNames = im_val().encoder(path)
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encoded_face = face_recognition.face_encodings(img)[0]
            encodeList.append(encoded_face)

        return encodeList

    