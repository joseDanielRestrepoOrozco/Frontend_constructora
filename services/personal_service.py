import streamlit as st
import requests

@st.cache_data
def get_all():
    base_url = st.secrets["base_url"]
    response = requests.get(f"{base_url}/api/personal")
    return response.json()