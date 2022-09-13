import app1
import app2
import streamlit as st

PAGES = {
    "Home Page": app1,
    "Begin Proctoring": app2
}

st.sidebar.title('Page Contents')
selection = st.sidebar.radio("Go To :", list(PAGES.keys()))
st.sidebar.write("Made by Agash Uthayasuriyan")
page = PAGES[selection]
page.app()