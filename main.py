import app1
import app2
import streamlit as st

PAGES = {
    "Home Page": app1,
    "Detection": app2
}

st.sidebar.title('Page Contents')
selection = st.sidebar.radio("Go To :", list(PAGES.keys()))
url = "https://github.com/Agash912"
#st.sidebar.write("Find ")
#st.sidebar.write("Made by[link](%s)" % url)
st.markdown("Made by [Agash Uthayasuriyan](%s)" % url)
page = PAGES[selection]
page.app()