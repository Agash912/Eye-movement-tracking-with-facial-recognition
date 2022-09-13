import streamlit as st
import os
import shutil
from fpdf import FPDF
import base64

def app():

    st.title("Face recognition with Eye ball movement detection")
    st.subheader("This application can be used to authorise a person and also track their motion of eyeballs")
    st.write("To begin, ")
    #st.write("1. Enter your name in the below field")
    user_input = st.text_input("1. Enter your name in the below field", 'Default user')
    #st.write("2. Upload your photo ")
    image_file = st.file_uploader("2. Upload your photo ", type=['jpg', 'png', 'jpeg'])

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

