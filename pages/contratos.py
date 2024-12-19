import streamlit as st
import services.contratos_service as cs
from services.clientes_service import show as show_cliente
from services.proyectos_service import show as show_proyecto
from services.clientes_service import get_all as all_clientes
from services.proyectos_service import get_all as all_proyectos

st.set_page_config(layout="wide")

data = list(cs.get_all())
clientes = list(all_clientes())
proyectos = list(all_proyectos())

st.header('Contratos')

def expander(contrato):

    cliente = show_cliente(contrato["cliente"])
    proyecto = show_proyecto(contrato["proyecto"])

    with st.expander(f"Proyecto {contrato['id']} - Cliente {contrato['cliente']}", expanded=False):
        col1, col2 = st.columns(2)

        with col1:
            st.metric("ID", contrato["id"])
            st.metric("Cliente", cliente["nombre"])
            st.metric("Proyecto", proyecto["_nombre"])

        with col2:
            st.metric("Monto", f"${contrato['monto']:,.2f}")
            st.write("**Estado:**", contrato["estado"])
            st.write("**Condiciones:**", contrato["condiciones"])

col_registros, col_form = st.columns([2, 1])

with col_registros:
    st.subheader("Registros")
    for contrato in data:
        expander(contrato)

with col_form:
    # Formulario para ingresar nuevos registros
    st.subheader("Agregar nuevo Contrato")
    with st.form("nuevo_contrato"):
        monto = st.number_input("Nombre", min_value=0.0, value=0.0, step=0.1)
        condiciones = st.text_input("Condiciones", value="")
        estado = st.text_input("Estado")

        # Dropdown para seleccionar proyecto
        proyecto_options = {p["_nombre"]: p["_id"] for p in proyectos}
        proyecto_select = st.selectbox("Seleccione un proyecto",
                                options=list(proyecto_options.keys()),
                                format_func=lambda x: x)

        # Dropdown para seleccionar cliente
        cliente_options = {c["nombre"]: c["id"] for c in clientes}
        cliente_select = st.selectbox("Seleccione un cliente",
                               options=list(cliente_options.keys()),
                               format_func=lambda x: x)

        submitted = st.form_submit_button("Agregar registro")
        if submitted:
            if monto <= 0:
                st.error("monto no valido")
            elif not estado:
                st.error("estado no valido")
            elif not proyecto_select:
                st.error("seleccione un proyecto")
            elif not cliente_select:
                st.error("seleccione un cliente")
            else:
                data = {
                    "monto": monto,
                    "condiciones": condiciones,
                    "estado": estado,
                    "proyecto_id": proyecto_options[proyecto_select],
                    "cliente_id": cliente_options[cliente_select]
                }
                cs.store(data)
                cs.get_all.clear()
                all_clientes.clear()
                all_proyectos.clear()
                st.rerun()
