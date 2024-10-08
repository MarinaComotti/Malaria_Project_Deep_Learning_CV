import tensorflow as tf
from keras.preprocessing import image
import numpy as np
from PIL import Image
import io
from paths import Path


IMG_WIDTH = 132
IMG_HEIGHT = 133


def open_model():
    path = Path()
    model_path = path.get_model_path()
    model_path_str = str(model_path)

    interpreter = tf.lite.Interpreter(model_path=model_path_str)
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    return input_details, output_details, interpreter


def open_image(file):
    image_bytes = file.read()
    return Image.open(io.BytesIO(image_bytes))


def preprocess_image(img):
    img_array = image.img_to_array(img)
    if img_array.shape[-1] == 4:
        img_array = img_array[..., :3]
    img_array = np.expand_dims(img_array, axis=0)
    return tf.image.resize(img_array, size=(IMG_HEIGHT, IMG_WIDTH))


def make_prediction(image):
    img = preprocess_image(image)
    input_details, output_details, interpreter = open_model()
    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    return output_data
