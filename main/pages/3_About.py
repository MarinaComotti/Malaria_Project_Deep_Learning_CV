import streamlit as st

st.title("The model ")

st.markdown(
    """
    This model was created using TensorFlow and Keras. Different techniques were applied in its development, including image augmentation, transfer learning and fine-tuning. During the evaluation stage, it achieved 95% accuracy on the test set.
    ### Dataset    
    Training was performed using the 'Malaria' dataset from TFDS, consisting of 27,558 images taken from thin blood smear samples of segmented cells. The images are divided into two classes: 'Parasitized' and 'Uninfected,' with an equal number of samples in each. The 'Parasitized' class contains samples of cells infected by the parasite that causes malaria, while the 'Uninfected' class has images of healthy cells. For more information about the dataset, you can visit the official page: [TFDS Malaria](https://www.tensorflow.org/datasets/catalog/malaria).
    ### Note
    This work is part of a development project and exploration of the main deep learning tools for computer vision on medical images. It remains open to new corrections and changes that can further improve and expand the model to make its diagnoses increasingly accurate.
    ### More Information
    To learn more about the model's development, you can visit the following link to our document on Google Colab:

       <a href="https://colab.research.google.com/drive/1axlsmSISJnFnXoOWlggPWBin-7SzdURA?usp=sharing" target="_blank">
       <img src="https://colab.research.google.com/img/colab_favicon_256px.png" alt="GitHub" style="width:24px; height:24px; vertical-align:middle;">
       Malaria detection - Binary clasification with CNN and Transfer learning </a> 
    """,
    unsafe_allow_html=True,
)
# style="font-size:20px"
st.header("Authors", divider="rainbow")


st.markdown(
    f"""
    - <a style="font-size:18px" href="https://github.com/MarinaComotti" target="_blank">
       <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" style="width:24px; height:24px; vertical-align:middle;">
       Marina Comotti </a>

    - <a style="font-size:18px" href="https://github.com/catrielramirez" target="_blank">
      <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" style="width:24px; height:24px; vertical-align:middle;">
      Catriel Ramirez </a>
    """,
    unsafe_allow_html=True,
)
