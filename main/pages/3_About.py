import streamlit as st

st.title("The model ")

st.markdown(
    """
    This model was created using Tensorflow and Keras. Different techniques were applied in its development, including CNN, Image Augmentation, Transfer Learning (with VGG16), and Fine-Tuning. During the evaluation stage, it achieved a 96% accuracy on the test set.
    ### Dataset    
    Training was performed using the "Malaria" dataset from TFDS, consisting of 27,558 images taken from thin blood smear samples of segmented cells. The images are divided into 2 classes: 'Parasitized' and 'Uninfected', with an equal number of samples in each. The 'Parasitized' class contains samples of cells infected by the parasite that causes malaria, while the 'Uninfected' class has images of healthy cells. For more information about the dataset, you can visit the official TFDS page: https://www.tensorflow.org/datasets/catalog/malaria.
    ### Note
    This work is part of a development project and exploration of the main deep learning tools for computer vision on medical images. It remains open to new corrections and changes that can further improve and expand the model to make its diagnoses increasingly accurate.
    ### More Information
    To learn more about the model's development, you can visit the following link to our document on Google Colab: ____."    """
)

st.header("Authors", divider="rainbow")
st.markdown(
    """
    - Marina Comotti:
    - !GitHub GitHub (--- falta completar con los enlaces---)
    - !LinkedIn LinkedIn (--- falta completar con los enlaces---)
    
- Catriel Ramires:
    - !GitHub GitHub (--- falta completar con los enlaces---)
    - !LinkedIn LinkedIn (--- falta completar con los enlaces---)
    """,
    unsafe_allow_html=True,
)
