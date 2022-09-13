from typing import Text
import cv2
import face_recognition
import numpy as np
import os
import encode.process as enc
import operations.operations as op
import imager.img_to_val as img_val
import time
import av
import shutil
from eye_detect.eye_detection import eyeTracking
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

def app():

    
    def real_time_prediction(image):

        logg=[]
        eye = eyeTracking()
        path = 'dataset/'
        data = op.file_operations()
        __,classNames = img_val.im_val().encoder(path)
        encoded_face_train = enc.tnt().tandt(path)


        img = image
        eye.refresh(img)
        frame = eye.annotated_frame()
        text = ''
        #logging = open("logger.txt",'r+')

        if eye.is_blinking():
            text = "Blinking"
        elif eye.is_right():
            text = "Looking right"
        elif eye.is_left():
            text = "Looking left"
        elif eye.is_center():
            text = "Looking center"


        imgS = cv2.resize(img, (0,0), None, 0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        faces_in_frame = face_recognition.face_locations(imgS)
        encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

        for encode_face, faceloc in zip(encoded_faces,faces_in_frame):
            matches = face_recognition.compare_faces(encoded_face_train, encode_face)
            faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
            matchIndex = np.argmin(faceDist)
        
            if matches[matchIndex]:
                name = classNames[matchIndex].upper().lower()
                data.database(name)
                y1,x2,y2,x1 = faceloc
                y1, x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(frame, (x1,y2-35),(x2,y2), (0,255,0), cv2.FILLED)
                cv2.putText(frame,name, (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
                cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
            
            print(logg)

        return frame

    

    RTC_CONFIGURATION = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

    class VideoProcessor:
        def recv(self, frame):
            img = frame.to_ndarray(format="bgr24")
            img = real_time_prediction(img)
            return av.VideoFrame.from_ndarray(img, format="bgr24")
            
    webrtc_ctx = webrtc_streamer(
        key="WYH",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={"video": True, "audio": False},
        video_processor_factory=VideoProcessor,
        async_processing=True,
    )

    