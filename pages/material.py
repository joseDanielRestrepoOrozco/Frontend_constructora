import streamlit as st
import pandas as pd
import services.material_service as ms

# Configurar la página para usar un diseño más amplio
st.set_page_config(layout="wide")

st.header('Materiales')

data = ms.get_all()
df = pd.DataFrame(data)
df.set_index("id", inplace=True)

col1, col2 = st.columns([2, 1])  # Ajusta las proporciones de las columnas

with col1:
    # Mostrar el DataFrame como una tabla en Streamlit
    st.subheader("Registros")
    st.dataframe(
        df,
        hide_index=True,
        use_container_width=True
    )

with (col2):
    # Formulario para ingresar nuevos registros
    st.subheader("Agregar nuevo Material")
    with st.form("nuevo_material"):
        nombre = st.text_input("Nombre")
        precio = st.number_input('precio', min_value=0.0, value=0.0, step=0.1, format="%.1f")

        submitted = st.form_submit_button("Agregar material")
        if submitted:
            if not nombre:
                st.error("Por favor, complete el campo de nombre")
            elif precio <= 0:
                st.error("el precio debe ser mayor a 0")
            else:
                data = {
                    "nombre": nombre,
                    "precio": precio,
                }
                ms.store(data)
                ms.get_all.clear()
                st.rerun()