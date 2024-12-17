import streamlit as st
import services.personal_service as ps

st.header('Personal')

data = ps.get_all()
st.text(data)
