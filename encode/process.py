import face_recognition
import cv2
import imager.img_to_val as k
import imager.img_to_val as img

class tnt:
    
    def tandt(self,path):
        self.path = path
        self.imgelon_rgb,self.imgelon = k.im_val().image_to_values(path)
        train_elon_encodings = face_recognition.face_encodings(self.imgelon)[0]
        train_encode = train_elon_encodings
        # test = face_recognition.load_image_file('training_dataset/1/agash2.jpeg')
        # test = cv2.cvtColor(test, cv2.COLOR_BGR2RGB)
        # test_encode = face_recognition.face_encodings(test)[0]
        # print(face_recognition.compare_faces([train_encode],test_encode))
        encoded_face_train = img.im_val().findEncodings(self.path)

        return encoded_face_train