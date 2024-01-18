import streamlit as st

st.set_page_config(page_title="AI App", page_icon="🖥️", layout="wide")

st.title("Clasificación de Imágenes para la Detección de Malaria")
st.markdown(
    """
    ## ¡Bienvenido! :wave:
    
    En esta página podrás probar un modelo de **deep learning** entrenado para realizar clasificación de imágenes de células según se encuentren infectadas o no del parásito que provoca la enfermedad de **Malaria**.
        
    ### Tienes dos maneras de utilizarlo: :wrench:
    
    1. **Load your image**: Si tienes imágenes en tu computadora de células que pueden estar o no enfermas, dirígete a esta sección. Ten en cuenta que el modelo fue entrenado con imágenes tomadas de muestras de frotis sanguíneo de células segmentadas. Por lo tanto, para que la clasificación sea lo más correcta posible, las imágenes que se carguen deben pertenecer también a muestras de este tipo.
        
    2. **Choose an image**: Si no tienes tus propias imágenes de células, puedes ir a esta sección donde encontrarás un conjunto de imágenes pre-seleccionadas para probar el modelo. Estas imágenes no fueron utilizadas durante el entrenamiento ya que pertenecen al conjunto de test.
    """,
    unsafe_allow_html=True,
)
