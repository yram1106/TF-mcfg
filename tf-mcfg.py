import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pdfkit

# Configuración de la página
st.set_page_config(
    page_title=Análisis Interactivo de Datos,
    page_icon="📈",
    layout=wide
)

# Título principal con emoji
st.title("📈 Aplicación Interactiva de Análisis de Datos")

# Barra lateral para el menú
menu = ["Inicio 🏠, EDA 🧮, Regresiones 📈, Generar Informe 📝"]
choice = st.sidebar.selectbox(Navega por los módulos, menu)

# Variables globales para almacenar datos
uploaded_data = None

# Módulos según la opción seleccionada
if choice == "Inicio 🏠"
    st.header("🏠 Bienvenido a la Aplicación")
    st.write(
        Esta herramienta interactiva te permite cargar datasets, realizar análisis exploratorios (EDA),
        aplicar modelos de regresión y generar informes en PDF. 
        Utiliza el menú lateral para comenzar.
    )
    st.image(
        httpsstreamlit.ioimagesbrandstreamlit-logo-secondary-colormark-darktext.png,
        caption=Streamlit App,
        use_column_width=True
    )

elif choice == "EDA 🧮"
    st.header("🧮 Análisis Exploratorio de Datos" (EDA))
    file = st.file_uploader(Sube un archivo CSV, type=[csv])
    
    if file is not None
        uploaded_data = pd.read_csv(file)
        st.success(¡Dataset cargado con éxito!)
        st.write(### Vista previa del dataset)
        st.dataframe(uploaded_data.head())
        
        # Estadísticas descriptivas
        st.write(### Estadísticas descriptivas)
        st.write(uploaded_data.describe())

        # Visualización
        st.write(### Visualización de Datos)
        col_x = st.selectbox(Selecciona la columna X para el gráfico, uploaded_data.columns)
        col_y = st.selectbox(Selecciona la columna Y para el gráfico, uploaded_data.columns)

        if st.button(Generar gráfico de dispersión)
            fig, ax = plt.subplots()
            sns.scatterplot(x=uploaded_data[col_x], y=uploaded_data[col_y], ax=ax)
            st.pyplot(fig)

elif choice == "Regresiones 📈"
    st.header("📈 Modelos de Regresión")
    st.write(
        En este módulo podrás aplicar modelos de regresión a tus datos.
        Próximamente Implementaremos regresiones lineales, polinómicas y más.
    )
    st.warning(Funcionalidad de regresiones en desarrollo.)

elif choice == "Generar Informe 📝"
    st.header("📝 Generación de Informes")
    
    if uploaded_data is not None
        st.write(Generando un informe con el dataset cargado...)
        # Generar HTML para el informe
        report_html = f
        html
        headtitleInforme Ejecutivotitlehead
        body
        h1Informe Ejecutivoh1
        h2Vista previa del dataseth2
        {uploaded_data.head().to_html()}
        h2Estadísticas descriptivash2
        {uploaded_data.describe().to_html()}
        body
        html
        
        
        if st.button(Exportar informe a PDF)
            # Guardar el informe como PDF
            try
                pdfkit.from_string(report_html, informe.pdf)
                st.success(Informe generado con éxito. Descárgalo abajo)
                with open(informe.pdf, rb) as pdf_file
                    st.download_button("📥 Descargar Informe", pdf_file, file_name=informe.pdf)
            except Exception as e
                st.error(fError al generar el informe {e})
    else
        st.warning(Por favor, sube un dataset en el módulo de EDA antes de generar el informe.)

# Footer
st.sidebar.write(Desarrollado por [Mary Figueroa - Paradigmas de programación])
