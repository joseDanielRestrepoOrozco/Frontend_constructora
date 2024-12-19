import streamlit as st
import pandas as pd
from datetime import date
import services.proyectos_service as ps

# Configurar la página para usar un diseño más amplio
st.set_page_config(layout="wide")

st.header('Proyectos')

data = ps.get_all()
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

with col2:
    # Formulario para ingresar nuevos registros
    st.subheader("Agregar nuevo proyecto")
    with st.form("nuevo_proyecto"):
        nombre = st.text_input("Nombre")
        presupuesto = st.number_input("presupuesto inicial", min_value=0.0, value=0.0, step=0.1, format="%.1f")
        inicio = st.date_input("Fecha de inicio")
        estimacion_fin = st.date_input("Fecha estimada de fin")
        submitted = st.form_submit_button("Agregar registro")

        if submitted:
            if not nombre:
                st.error("Por favor, completa todos los campos de texto.")
            elif presupuesto <= 0:
                st.error("Por favor, ingresa un valor de presupuesto valido")
            elif inicio < date.today():
                st.error("La fecha de inicio no puede ser anterior a la fecha actual.")
            elif estimacion_fin < inicio:
                st.error("La fecha estimada de fin no puede ser anterior a la fecha de inicio.")
            else:
                # Convertir las fechas a cadenas con el formato deseado
                inicio = inicio.strftime("%Y-%m-%d")
                estimacion_fin = estimacion_fin.strftime("%Y-%m-%d")

                data = {
                    "nombre": nombre,
                    "presupuesto_inicial": presupuesto,
                    "fecha_inicio": inicio,
                    "fecha_estimacion_fin": estimacion_fin
                }
                ps.store(data)
                ps.get_all.clear()
                st.rerun()
