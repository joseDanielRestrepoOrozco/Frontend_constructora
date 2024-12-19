import streamlit as st
import pandas as pd
import services.subcontratistas_service as scs

data = scs.get_all()
df = pd.DataFrame(data)
df.set_index("id", inplace=True)

st.header('subcontratista')

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Registros")
    st.dataframe(df)

with col2:
    # Formulario para ingresar nuevos registros
    st.subheader("Agregar nuevo subcontratista")
    with st.form("nuevo_subcontratista"):
        nombre = st.text_input("Nombre")
        especialidad = st.text_input("Especialidad")
        disponible = st.checkbox('Disponibilidad')
        submitted = st.form_submit_button("Agregar registro")
        if submitted:
            if not nombre or not especialidad:
                st.error("Por favor, completa todos los campos de texto.")
            else:
                data = {
                    "nombre": nombre,
                    "especialidad": especialidad,
                    "disponible": disponible
                }

                scs.store(data)
                scs.get_all.clear()
                st.rerun()
