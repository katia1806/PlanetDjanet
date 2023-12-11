# app.py
# Installed imports
import streamlit as st

# Internal imports
from config import PAGES
# from src.common import display_social_media_links


def display_sidebar() -> str:
    """Display the sidebar of the page
    Returns:
        selected_page: The page selected by the user
    """
    # display the logo
    st.sidebar.image("static/logo2.0._blanc_noback.png", width=300)  # Replace with your logo path
    
    # display the privacy policy
    checking = st.sidebar.checkbox("I agree to the privacy policy")

    # display the navigation menu
    if checking:
        selected_page = st.sidebar.radio("Navigate to", list(PAGES.keys()))
    else:
        selected_page = None
        st.sidebar.caption("Agree to the privacy policy to access the pages")

    # display social media links or other information in the sidebar
    # display_social_media_links()

    return selected_page


def app():
    """Main app function"""
    # initialisations
    sidebar = st.sidebar
    header = st.container()
    main = st.container()
    footer = st.container()
    
    with sidebar:
        page_selected = display_sidebar()

    with header:
        st.markdown(
        f"""<h1 style='text-align: center;'>Welcome to Planet Djanet</h1>""", unsafe_allow_html=True)  # h1 title of the page

    with main:
        if page_selected:
            page = PAGES[page_selected]
            page.display()

    with footer:
        st.markdown(
            "<footer style='text-align: center;'>Copyright©2022 Planet Djanet. All Rights Reserved.</footer>", unsafe_allow_html=True)


if __name__ == "__main__":
    app()
