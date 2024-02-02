from PIL import Image

from .siamese import Siamese


def predict(model_path, image_1, image_2):
    model = Siamese(model_path=model_path)

    # probability = model.detect_image(image_1, image_2)
    # return probability


predict("model_data/siamese.h5", "", "")
