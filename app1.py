import streamlit as st
import os
import shutil
from fpdf import FPDF
import base64

def app():

    st.title("Eye ball movement detection with facial recognition")
    st.subheader("This application can identify a person and track motion of their eyeballs in real time using feature extraction")
    st.write("Kindly follow the below instructions: ")
    user_input = st.text_input("1. Enter your name in the below field", 'Default user')
    image_file = st.file_uploader("2. Upload your photo and then navigate to Detect page from sidebar", type=['jpg', 'png', 'jpeg'])

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

