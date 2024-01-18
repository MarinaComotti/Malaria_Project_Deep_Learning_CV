import pathlib


class Path:
    def __init__(self):
        self.path_structure = pathlib.Path(__file__).parent.parent.resolve()
        self.model_path = pathlib.Path(
            self.path_structure, "model", "malaria_model_classification.tflite"
        )
        self.model_compress_path = pathlib.Path(
            self.path_structure, "model", "malaria_model_classification.h5.gz"
        )
        self.images_folder_path = pathlib.Path(
            self.path_structure, "images_test_sample"
        )
        self.parasitized_images_path = pathlib.Path(
            self.images_folder_path, "0-parasitized"
        )
        self.uninfected_images_path = pathlib.Path(
            self.images_folder_path, "1-uninfected"
        )

    def get_model_compress_path(self):
        return self.model_compress_path

    def get_model_path(self):
        return self.model_path

    def get_images_forlder_path(self):
        return self.images_folder_path

    def get_parasitized_images_path(self):
        return self.parasitized_images_path

    def get_uninfected_images_path(self):
        return self.uninfected_images_path

    def get_image_complete_path(self, image_folder, image_name):
        return pathlib.Path(image_folder, image_name)
