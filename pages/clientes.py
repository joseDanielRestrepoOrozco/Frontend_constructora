import streamlit as st
import pandas as pd
import services.clientes_service as cs

data = cs.get_all()
df = pd.DataFrame(data)
df.set_index("id", inplace=True)

st.header('Clientes')

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Registros")
    
    # Añadir una columna de checkbox para seleccionar filas a eliminar
    df['Eliminar'] = False
    
    # Usar st.data_editor en lugar de st.dataframe
    edited_df = st.data_editor(df)
    
    # Botón para eliminar las filas seleccionadas
    if st.button('Eliminar seleccionados'):
        rows_to_delete = edited_df[edited_df['Eliminar']].index.tolist()
        for row_id in rows_to_delete:
            cs.delete(row_id)  
        st.success('Registros eliminados exitosamente')
        cs.get_all.clear()
        st.rerun()

with col2:
    # El resto de tu código para agregar nuevos clientes permanece igual
    st.subheader("Agregar nuevo Cliente")
    with st.form("nuevo_cliente"):
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