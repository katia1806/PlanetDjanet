# app.py
# Installed imports
import streamlit as st

# Backend URL
BACKEND_URL = "http://backend:8000"

# # Internal imports
from src import (
    facebook,
    # pictures, 
    # meta, 
    # instagram
    )

# from common import display_social_media_links

# declaration of different pages
PAGES = {
    # 'Instagram': instagram,
    'Facebook': facebook,
    # 'Meta': meta,
    # 'Trips': trips,
    #'Pictures': pictures,
}

# create the container block
sidebar = st.sidebar
header = st.container()
main = st.container()
footer = st.container()

def display_sidebar():
    """Display the sidebar of the page"""
    st.sidebar.image("img/logo.png", width=300)  # Replace with your logo path
    checking = st.sidebar.checkbox("I agree to the privacy policy")

    if checking:
        selected_page = st.sidebar.radio("Navigate to", list(PAGES.keys()))
    else:
        selected_page = None
        st.sidebar.caption("Agree to the privacy policy to access the pages")

    # Display social media links or other information in the sidebar
    # display_social_media_links()

    return selected_page


def app():
    """Main app function"""
    # with sidebar:
    #     selected_page = display_sidebar()

    with header:
        # You can put a welcome message or header information here
        st.title("Welcome to Planet Djanet")

    with main:
        selected_page = display_sidebar()
        if selected_page:
            page = PAGES[selected_page]
            page.display()

    with footer:
        # Footer content
        st.markdown("Copyright©2022 Planet Djanet. All Rights Reserved.")


if __name__ == "__main__":
    app()
