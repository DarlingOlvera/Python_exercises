import streamlit as st
import pandas as pd
import time


def inicializar_estado():
    # Se crea la clave del sesion state la primera vez que se ejecuta el sitio (inicializacion)
    if "transacciones" not in st.session_state:
        st.session_state.transacciones = []


def usar_formulario():
    categorias = ['Comidas', 'Transporte', 'Salud',
                  'Entretenimiento', 'Ingreso extra']

    with st.sidebar:
        st.subheader("Registrar nuevo movimiento")
        # formulario de la transaccion
        with st.form("nueva_transaccion"):
            descripcion = st.text_input("Descripción del gasto o ingreso")
            monto = st.number_input(
                "Monto", step=1.0, min_value=0.0, format="%0.2f")
            fecha = st.date_input("Fecha")
            categoria = st.selectbox("categoria", categorias)
            tipo = st.radio("Tipo", ["Ingreso", "Gasto"], horizontal=True)
            enviado = st.form_submit_button("Guardar")

        if enviado:
            st.session_state.transacciones.append({
                "descripcion": descripcion,
                "monto": monto,
                "fecha": fecha,
                "categoria": categoria,
                "tipo": tipo
            })
            mensaje = st.empty()
            mensaje.success("Transacción guardada exitosamente")
            time.sleep(3)
            mensaje.empty()


def mostrar_transacciones():
    # muestra de prueba
    st.subheader("Transacciones registradas:")

    if st.session_state.transacciones:
        df = pd.DataFrame(st.session_state.transacciones)
        st.dataframe(df)
    else:
        st.info("No se han registrado transacciones aún. Utiliza el formulario para agregar tus gastos e ingresos.")


def mostrar_resumen():
    if not st.session_state.transacciones:
        st.info("No se han registrado transacciones aún. Utiliza el formulario para agregar tus gastos e ingresos.")
        return

    df = pd.DataFrame(st.session_state.transacciones)

    ingresos = df[df["tipo"] == "Ingreso"]["monto"].sum()
    gastos = df[df["tipo"] == "Gasto"]["monto"].sum()
    balance = ingresos - gastos
    gastos_df = df[df["tipo"] == "Gasto"]["monto"]
    # mean() calcula el promedio aritmetico de los valores de una Serie (suma total / cantidad de registros)
    # El condicional evita llamarlo cuando la Serie esta vacia, ya que mean() de una Serie vacia retorna NaN
    gasto_promedio = gastos_df.mean() if not gastos_df.empty else 0.0

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Ingresos", f"${ingresos:,.2f}")
    col2.metric("Gastos", f"${gastos:,.2f}")
    col3.metric("Balance", f"${balance:,.2f}")
    col4.metric("Gasto promedio", f"${gasto_promedio:,.2f}")


def mostrar_titulos():
    st.title("Tracker financiero personal")
    st.write("Lleva el control de tus gastos e ingresos mensuales")
    st.caption("Version 1.0")


mostrar_titulos()

inicializar_estado()
usar_formulario()

tab_resumen, tab_movimientos, tab_analisis = st.tabs(
    ["Resumen", "Movimientos", "Análisis"])

with tab_resumen:
    mostrar_resumen()

with tab_movimientos:
    mostrar_transacciones()
