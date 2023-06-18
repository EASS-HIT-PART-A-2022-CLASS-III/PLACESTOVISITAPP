import streamlit as st
import requests

# Define the backend URL
BACKEND_URL = "http://backend:8800"






# Function to create a new location
def create_location(name, description):
    data = {"name": name, "description": description}
    response = requests.post(f"{BACKEND_URL}/locations", json=data)
    if response.status_code == 200:
        st.success("Location created successfully")
    else:
        st.error("Error creating location")

# Function to delete a location
def delete_location(location_id):
    response = requests.delete(f"{BACKEND_URL}/locations/{location_id}")
    if response.status_code == 200:
        st.success("Location deleted successfully")
    else:
        st.error("Error deleting location")

# Main Streamlit app
def main():
    st.title("cool places APIApp")

    message = f"there is a map so u can see the country of the location u added"
    # Display a map 
    st.map(location_id)

    # Create a new location
    st.header("Create a New Location")
    name = st.text_input("Name")
    description = st.text_input("Description")
    if st.button("Create"):
        create_location(name, description)

    # Delete a location
    st.header("Delete a Location")
    location_id = st.number_input("Location ID", min_value=1)
    if st.button("Delete"):
        delete_location(location_id)

if __name__ == "__main__":
    main()
