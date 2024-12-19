import streamlit as st
import requests

@st.cache_data
def get_all():
    response = requests.get(f"{st.secrets["base_url"]}/api/subcontratista")
    return response.json()

def store(data):
    response = requests.post(f"{st.secrets["base_url"]}/api/subcontratista", json=data)
    return response.json()