import streamlit as st

st.title("El modelo: ")

st.markdown(
    """
    Este modelo fue creado con **Tensorflow** y **Keras**. Para su desarrollo se aplicaron diferentes técnicas como CNN, Image Augmentation, Transfer Learning (con VGG16) y Fine-Tuning. Durante la etapa de evaluación, el mismo alcanzó un 96% de accuracy sobre el conjunto de test.

    ### Dataset    
    Su entrenamiento se realizó con el dataset "Malaria" de TFDS, el mismo está conformado por 27,558 imágenes tomadas de muestras de frotis de sangre delgada de células segmentadas. Las imágenes se encuentran divididas en 2 clases: 'Parasizited' y 'Uninfected', con misma cantidad de muestras en cada una. La clase 'Parasizited' cuenta con muestras de células infectadas por el parásito que provoca la malaria, mientras que por el contrario la clase 'Uninfected' tiene imágenes de células sanas. Para más información sobre el dataset puede ingresar a la página oficial de TFDS: https://www.tensorflow.org/datasets/catalog/malaria.

    ### Nota
    Este trabajo forma parte de un proyecto de desarrollo y exploración de las principales herramientas de deep learning para computer vision sobre imágenes médicas. El mismo continúa abierto a nuevas correcciones y cambios que puedan continuar mejorando y expandiendo el modelo con el fin de que sus diagnósticos sean cada vez mejores.

    ### Más información
    Para conocer más sobre el desarrollo del modelo puede ingresar al siguiente link de nuestro documento en Google Colab: ____
    """
)

st.header("Autores", divider="rainbow")
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
