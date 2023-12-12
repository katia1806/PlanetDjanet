# pictures_page.py
import streamlit as st
from src.view.common import get_image


def display():
    st.title("Pictures")

    # load images
    image1 = get_image("static/image_PD1.jpeg")
    image2 = get_image("static/image_PD2.jpeg")
    image3 = get_image("static/IMG_6386.JPG")

    # display images
    col1, col2 = st.columns(2)
    col1.image(image1)
    col2.image(image2)
    st.image(image3)