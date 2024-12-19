import streamlit as st
import pandas as pd
import services.clientes_service as cs

data = cs.get_all()
df = pd.DataFrame(data)
df.set_index("id", inplace=True)

st.header('Constructoras')

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Registros")
    st.dataframe(df)

with col2:
    # Formulario para ingresar nuevos registros
    st.subheader("Agregar nueva constructora")
    with st.form("nuevo_constructora"):
        nombre = st.text_input("Nombre")
        direccion = st.text_input("Dirección")
        contacto = st.text_input("Contacto")
        submitted = st.form_submit_button("Agregar registro")
        if submitted:
            if not nombre or not direccion or not contacto:
                st.error("Por favor, completa todos los campos de texto.")
            else:
                data = {
                    "nombre": nombre,
                    "direccion": direccion,
                    "contacto": contacto
                }
                cs.store(data)
                cs.get_all.clear()
                st.rerun()
