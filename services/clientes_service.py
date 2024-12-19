import streamlit as st
import requests

@st.cache_data
def get_all():
    response = requests.get(f"{st.secrets["base_url"]}/api/cliente")
    return response.json()

def store(data):
    response = requests.post(f"{st.secrets["base_url"]}/api/cliente", json=data)
    return response.json()

def show(id):
    response = requests.get(f"{st.secrets["base_url"]}/api/cliente/{id}")
    return response.json()

def delete(id):
    response = requests.delete(f"{st.secrets["base_url"]}/api/cliente/{id}")
    return response.json()