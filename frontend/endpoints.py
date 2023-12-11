from fastapi import APIRouter
import requests

BACKEND_URL = "http://backend:8000"

item_router = APIRouter()

@item_router.get("/{page_name}")
def get_page_data(page_name):
    """Retrieve data by page_name from the backend."""
    response = requests.get(f"{BACKEND_URL}/{page_name}")
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to retrieve data: {response.status_code}")