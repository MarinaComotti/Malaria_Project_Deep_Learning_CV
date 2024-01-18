import streamlit as st
import process_info
import prediction_layout

st.set_page_config(page_title="Load image", page_icon="💿", layout="wide")


def load():
    uploaded_file = st.file_uploader("Load image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image_name = uploaded_file.name
        return process_info.open_image(uploaded_file), image_name
    else:
        return None, None


def create_columns(img):
    col1, col2 = st.columns(2)
    with col1:
        st.image(img, caption="Imagen cargada", width=300)
    with col2:
        process_info.show_prediction(img, " hhb ")


img, image_name = load()
if img is not None:
    prediction_layout.create_columns(img, image_name)
