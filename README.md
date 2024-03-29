# Malaria Image Classification Project 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1axlsmSISJnFnXoOWlggPWBin-7SzdURA?usp=sharing)    [![Open In Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://malariaprojectdeeplearningcv-st.streamlit.app/)


<img src="./images_test_sample/collage_readme.png" alt="cells" style="max-width: 200px; height: 332px; display: block; margin: auto;">


## Welcome! 

### About proyect 
This project aims to detect malaria using deep learning techniques. To address this issue, we focus on implementing a supervised learning approach. For model training, we utilize the "Malaria" dataset from TensorFlow Datasets, which contains 27,558 images of blood cells, both parasitized and uninfected. The main purpose is to create a binary classification model aimed at improving malaria diagnosis.
Using tools such as TensorFlow and Keras, we thoroughly explore deep learning techniques. The project covers everything from data acquisition and preprocessing to model implementation and evaluation. Our comprehensive approach is not only geared towards developing an efficient solution for malaria image classification but also understanding in-depth the complexities and challenges associated with the practical application of artificial intelligence in a medical context.

The exploration and processing of data, along with the construction, training, and evaluation of the model, were developed in Google Colab. To access the document, click on this [link](https://malariaprojectdeeplearningcv-st.streamlit.app/)
 
### About model
This model was created using Tensorflow and Keras. Different techniques were applied in its development, including CNN, Image Augmentation, Transfer Learning (with VGG16), and Fine-Tuning. During the evaluation stage, it achieved an accuracy of about 96% on the test set.

### About data
Training was performed using the "Malaria" dataset from TFDS, consisting of 27,558 images taken from thin blood smear samples of segmented cells. The images are divided into 2 classes: 'Parasitized' and 'Uninfected', with an equal number of samples in each. The 'Parasitized' class contains samples of cells infected by the parasite that causes malaria, while the 'Uninfected' class has images of healthy cells. For more information about the dataset, you can visit the [official TFDS page](https://www.tensorflow.org/datasets/catalog/malaria.)

### Getting started
The model deployment is carried out through a web interface using the Streamlit platform. You can use this platform to access the model and make predictions with both preloaded images from the test set and your own images. To access the Streamlit app, please click [here](https://malariaprojectdeeplearningcv-st.streamlit.app/). 

You can also download the project from GitHub if you want to explore the source code. To access the model on Github, enter the following:

``` 
# Create a directory 
mkdir clon_malaria

# Enter the directory.
cd clon_malaria

# Perform the clone.
git clone https://github.com/MarinaComotti/Malaria_Project_Deep_Learning_CV.git

# Install dependencies 
pip install -r requirements.txt

#To run Streamlit locally on your PC:
streamlit run main/Home_🏠.py
```

## Authors

Marina Comotti and Catriel Ramirez


## License
MIT License

Copyright (c) 2024 Marina Comotti, Catriel Ramirez

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


## Project status
This project is under constant development and active maintenance. Here are the current status and other relevant details:

- **Current Version:** 1.0.0.

- **Active Development:** Yes.

- **Last Update:** [02-02-2024](https://github.com/MarinaComotti/Malaria_Project_Deep_Learning_CV.git).

This project remains active and welcomes contributions and feedback from the community. Thank you for your interest!

