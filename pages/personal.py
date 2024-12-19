import streamlit as st
import pandas as pd
import services.personal_service as ps
import services.vinculacion_service as vs  # Importar el nuevo servicio

# Configurar la página para usar un diseño más amplio
st.set_page_config(layout="wide")

st.header('Personal')

# Obtener los datos del servicio
data = ps.get_all()
df = pd.DataFrame(data)

col1, col2 = st.columns([2, 1])  # Ajusta las proporciones de las columnas

with col1:
    # Mostrar el DataFrame como una tabla en Streamlit
    st.subheader("Registros")
    st.dataframe(
        df.drop(columns=['proyectos']),  # Eliminamos la columna 'proyectos'
        column_config={
            "id": st.column_config.NumberColumn("ID"),
            "nombre": "Nombre",
            "rol": "Rol",
            "horas_trabajadas": st.column_config.NumberColumn("Horas trabajadas", format="%d")
        },
        hide_index=True,
        use_container_width=True
    )

with col2:
    # Formulario para ingresar nuevos registros
    st.subheader("Agregar nuevo registro")
    with st.form("nuevo_registro"):
        nombre = st.text_input("Nombre")
        rol = st.text_input("Rol")
        horas_trabajadas = st.number_input("Horas trabajadas", min_value=0, step=1)

        submitted = st.form_submit_button("Agregar registro")
        if submitted:
            if nombre and rol and horas_trabajadas > 0:
                data = {
                    "nombre": nombre,
                    "rol": rol,
                    "horas_trabajadas": horas_trabajadas,
                }
                ps.store(data)
                ps.get_all.clear()
                st.rerun()
            else:
                st.error("Por favor, complete todos los campos. Las horas trabajadas deben ser mayores que 0.")

    # Nuevo formulario para vincular un proyecto a un miembro del personal
    st.subheader("Vincular proyecto a personal")
    with st.form("vincular_proyecto"):
        proyecto_id = st.text_input("ID del Proyecto")
        personal_id = st.text_input("ID del Personal")

        submitted_proyecto = st.form_submit_button("Vincular")
        if submitted_proyecto:
                try:
                    data = {
                        "proyecto_id": proyecto_id,
                        "personal_id": personal_id,
                    }
                    vs.vincular_proyecto_personal(data)  # Llamar al servicio de vinculación
                    st.success("Proyecto vinculado correctamente.")
                except Exception as e:
                    st.error(f"Error al vincular proyecto: {e}")