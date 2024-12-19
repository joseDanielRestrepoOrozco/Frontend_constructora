import streamlit as st
import requests

@st.cache_data
def get_all():
    response = requests.get(f"{st.secrets["base_url"]}/api/material")
    return response.json()

def store(data):
    response = requests.post(f"{st.secrets["base_url"]}/api/material", json=data)
    return response.json()