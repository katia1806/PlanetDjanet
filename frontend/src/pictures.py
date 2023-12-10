# pictures_page.py
import streamlit as st
# from backend.src.common import get_image


def display():
    st.title("Pictures")

    # Load images
    image1 = get_image("image_PD1.jpeg")
    image2 = get_image("image_PD2.jpeg")
    image3 = get_image("IMG_6386.JPG")
    image4 = get_image("image_PD4.jpeg")
    image5 = get_image("image_PD5.jpeg")
    image6 = get_image("image_PD6.jpeg")

    # Display images
    col1, col2 = st.columns(2)
    col1.image(image1)
    col2.image(image2)
    st.image(image3)
    st.image(image4)
    st.image(image5)
    st.image(image6)

This function can be called from the main app.py file
