import sys
import numpy as np
from tensorflow import keras
from tensorflow.keras.utils import load_img, img_to_array


def main(argv):
    classifier = keras.models.load_model("model")
    test_image = load_img(argv[1], target_size=(64, 64))

    test_image = img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)

    result = classifier.predict(test_image)

    if result[0][0] == 1:
        print("Dog")
    else:
        print("Cat")


if __name__ == "__main__":
    main(sys.argv)
