# app.py
# Installed imports
import streamlit as st

# Internal imports
from config import PAGES

def display_social_media_links():
    """Display social media links in the sidebar."""
    # display the title
    st.sidebar.markdown("Social Media Links")
    
    # display the social media links
    col1, col2, col3 = st.sidebar.columns(3)
    # Instagram Link
    col1.markdown('''
        <a href="https://www.instagram.com/planet___djanet/?hl=fr">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/240px-Instagram_icon.png" width="50" height="50" />
        </a>''',
                unsafe_allow_html=True
                )
    # Facebook Link
    col2.markdown('''
        <a href="https://www.facebook.com/PlanetDjanet/">
            <img src="https://cdn-icons-png.flaticon.com/512/124/124010.png" width="50" height="50" />
        </a>''',
                unsafe_allow_html=True
                )
    # Twitter Link
    col3.markdown('''
        <a href="https://planetdjanet.com/fr/">
            <img src="http://planetdjanet.com/wp-content/uploads/2020/06/logo2.0._blanc_noback.png" width="80" height="50" />
        </a>''',
                unsafe_allow_html=True
                )
    
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
    display_social_media_links()

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
