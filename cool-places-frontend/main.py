import streamlit as st
import requests

# API base URL
Backend_URL = "http://backend/locations"

# Page title
def main():
    st.title("Cool Places App")

    # Create location form
    st.header("Create Location")
    name = st.text_input("Name")
    country = st.text_input("Country")
    description = st.text_area("Description")
    if st.button("Create"):
        create_location(name, country, description)

    # Display all locations
    st.header("All Locations")
    locations = get_all_locations()
    for location in locations:
        st.write(f"Name: {location['name']}")
        st.write(f"Country: {location['country']}")
        st.write(f"Description: {location['description']}")
        st.write("-----")

def create_location(name, country, description):
    url = f"{Backend_URL}/locations"
    data = {
        "name": name,
        "country": country,
        "description": description
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        st.success("Location created successfully.")
    else:
        st.error("Failed to create location.")

def get_all_locations():
    url = f"{Backend_URL}/locations"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

if __name__ == "__main__":
    main()
