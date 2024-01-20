import streamlit as st

st.set_page_config(page_title="Malaria Detection App", page_icon="🖥️", layout="wide")

st.title("Image Classification for Malaria Detection")
st.markdown(
    """
    ## ¡Welcome! :wave:
    
    On this page, you will be able to test a trained **deep learning** model for image classification of cells, determining whether they are infected or not with the parasite that causes **Malaria**.
        
    ### You have two ways to use it: :wrench:
    
    1. **Load your image**: If you have images on your computer of cells that may or may not be diseased, go to this section. Keep in mind that the model was trained with images taken from blood smear samples of segmented cells. Therefore, for the classification to be as accurate as possible, the uploaded images should also belong to samples of this type.
        
    2. **Choose an image**: If you don't have your own images of cells, you can go to this section where you will find a set of pre-selected images to test the model. These images were not used during training as they belong to the test set.
    """,
    unsafe_allow_html=True,
)
