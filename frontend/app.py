# app.py

import tools as t
import streamlit as st
# Internal packages
from src import (
    facebook,
    instagram,
    meta,
    pictures,
    trips)

# Declaration of different pages
PAGES = {
    'Instagram': instagram,
    'Facebook': facebook,
    'Meta': meta,
    'Trips': trips,
    'Pictures': pictures,
}

# create the container block
sidebar = st.sidebar
header = st.container()
main = st.container()
footer = st.container()


def display_sidebar():
    """ display the sidebar of the page

    Returns:
        streamlit.runtime.uploaded_file_manager.UploadedFile: the file uploaded
        str: the page selected
    """
    st.markdown(
        "<h2 style='text-align: center;'>Google Map Dataset</h2>", unsafe_allow_html=True)  # title of the sidebar
    st.image("img/Google-Maps-Logo.png")  # logo de google
    myzipfile = t.upload()  # upload the data
    selection = st.radio("Navigation of the pages", list(
        PAGES.keys()))  # navigation to the other page

    # show the contact of linkedin and github
    st.markdown(
        "<h2 style='text-align: center;'>Contact me</h2>", unsafe_allow_html=True)  # contact me
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""<div style="text-align: center">
                                <a href='https://www.linkedin.com/in/xiangyu-an-34109a196/'>{t.img_to_html('img/linkedin.png')}</a>
                            </div>""",
                    unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div style="text-align: center">
                            <a href='https://github.com/AN-Xiang-yu'>{t.img_to_html('img/github.png')}</a>
                        </div>""",
                    unsafe_allow_html=True)
    return myzipfile, selection


#  ----- body of the page ------
# sidebar of the page
with sidebar:
    myzipfile, selection = display_sidebar()


# --- header of the page ---
with header:
    st.markdown(
        f"""<h1 style='text-align: center;'>{selection}</h1>""", unsafe_allow_html=True)  # h1 title of the page

# --- main of the page ----
with main:
    page = PAGES[selection]
    page.main(myzipfile)
    if page == "Facebook":
        facebook.show_facebook_dashboard()
    if page == "Instagram":
        instagram.show_instagram_dashboard()
    if page == "Meta":
        meta.show_meta_dashboard()
    if page == "Trips":
        trips.show_trips_dashboard()
    if page == "Pictures":
        pictures.show_pictures_dashboard()

# --- footer of the page ---
with footer:
    st.markdown(
        "<footer style='text-align: center;'>Copyright©2022-2023 Xiangyu AN - All Rights Reserved. </footer>", unsafe_allow_html=True)
