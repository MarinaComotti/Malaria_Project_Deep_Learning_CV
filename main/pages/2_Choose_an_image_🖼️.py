import streamlit as st
import prediction_layout
from paths import Path
from PIL import Image

st.set_page_config(page_title="Choose image", page_icon="🖼️", layout="wide")

options = [f"Image {i+1}" for i in range(10)]
images_names = [f"{i+1}.jpg" for i in range(10)]


def search_image_name(option):
    num_str = option[6:]
    num_int = int(num_str)
    return images_names[
        num_int - 1
    ]  # le resto -1 porque en las lista las pos empiezan con 0


def select_image(image_class, image_name):
    paths = Path()
    if image_class == 0:
        parasitized_folder_path = paths.get_parasitized_images_path()
        image_path = paths.get_image_complete_path(parasitized_folder_path, image_name)
        image_path_str = str(image_path)
        return Image.open(image_path_str)

    else:
        uninfected_folder_path = paths.get_uninfected_images_path()
        image_path = paths.get_image_complete_path(uninfected_folder_path, image_name)
        image_path_str = str(image_path)
        return Image.open(image_path_str)


def create_tabs():
    tab1, tab2 = st.tabs(["Parasitized images: ", "Uninfected images: "])
    with tab1:
        option = st.selectbox(
            "Select an image from the 'Parasitized' class:",
            options=options,
            index=None,
            placeholder="Parasitized images...",
        )
        if option is not None:
            image_name = search_image_name(option)
            selected_image = select_image(0, image_name)
            prediction_layout.create_columns(
                selected_image,
                option,
                "Parasitized",
            )

    with tab2:
        option = st.selectbox(
            "Select an image from the 'Uninfected' class:  ",
            options=options,
            index=None,
            placeholder="Uninfected images...",
        )
        if option is not None:
            image_name = search_image_name(option)
            selected_image = select_image(1, image_name)
            prediction_layout.create_columns(
                selected_image,
                option,
                "Uninfected",
            )


create_tabs()
