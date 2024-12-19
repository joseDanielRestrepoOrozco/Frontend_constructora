import streamlit as st
import requests

def vincular_proyecto_personal(data):
    response = requests.post(f"{st.secrets['base_url']}/api/personal/proyectos", json=data)
    response.raise_for_status()  # Lanza una excepción si hay un error
    return response.json()