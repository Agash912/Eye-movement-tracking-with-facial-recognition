import streamlit as st
import os
import shutil
from fpdf import FPDF
import base64

def app():

    st.title("Real-time Proctoring App")
    st.subheader("This application lets you proctor the test taker by recognizing face and tracking eye balls ")
    st.text("**** Click Begin Proctoring from sidebar only after you upload image ****")


    user_input = st.text_input("Enter your name", 'User')
    image_file = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg'])

    if image_file is not None:
        file_details = {"FileName":user_input,"FileType":image_file.type,"FileSize":image_file.size}
        st.write(file_details)
        open('log.txt', 'w').close()
        with open(image_file.name,'wb') as f:
            shutil.rmtree('dataset')
            os.mkdir('dataset')
            f.write(image_file.getbuffer())
            os.rename(image_file.name,user_input+".jpeg")
            new_path = "dataset/"+ user_input+".jpeg"
            shutil.move(user_input+".jpeg", new_path)

