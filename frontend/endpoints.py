from fastapi import APIRouter

item_router = APIRouter()

@item_router.get("/{file_name}")
def get_file(file_name):
    """Retrieve data by file name from the backend."""
    response = requests.get(f"{BACKEND_URL}/{file_name}")
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to retrieve data: {response.status_code}")