import streamlit as st

def display_social_media_links():
    """Display social media links in the sidebar."""
    st.sidebar.markdown("#### Social Media Links")
    
    # Instagram Link
    st.sidebar.markdown(
        """<a href="https://www.instagram.com/yourusername" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/instagram-new.png" width="30" height="30"/>
        </a>""", unsafe_allow_html=True)
    
    # Facebook Link
    st.sidebar.markdown(
        """<a href="https://www.facebook.com/yourusername" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/facebook-new.png" width="30" height="30"/>
        </a>""", unsafe_allow_html=True)
    
    # Twitter Link
    st.sidebar.markdown(
        """<a href="https://twitter.com/yourusername" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/twitter.png" width="30" height="30"/>
        </a>""", unsafe_allow_html=True)
    
     # LinkedIn Link
    st.sidebar.markdown(
        """<a href="https://www.linkedin.com/in/yourusername" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/linkedin.png" width="30" height="30"/>
        </a>""", unsafe_allow_html=True)

        