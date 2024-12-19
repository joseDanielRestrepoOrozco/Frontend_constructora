import streamlit as st
import services.contratos_service as cs

data = list(cs.get_all())

st.header('Contratos')

def expander(proyecto):
    with st.expander(f"Proyecto {proyecto['id']} - Cliente {proyecto['cliente']}", expanded=False):
        col3, col4 = st.columns(2)

        with col3:
            st.metric("Cliente", proyecto["cliente"])
            st.metric("ID", proyecto["id"])
            st.metric("Proyecto", proyecto["proyecto"])

        with col4:
            st.metric("Monto", f"${proyecto['monto']:,.2f}")
            st.write("**Estado:**", proyecto["estado"])
            st.write("**Condiciones:**", proyecto["condiciones"])

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Registros")
    for proyecto in data:
        expander(proyecto)

with col2:
    # Formulario para ingresar nuevos registros
    st.subheader("Agregar nuevo Contrato")
    with st.form("nuevo_constrato"):
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
