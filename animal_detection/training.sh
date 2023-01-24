#!/bin/bash

NOTEBOOK="CNN-animal_image-classification"

papermill --progress-bar -p epochs 3 -p example_image "single_prediction/cat_or_dog_2.jpg" "${NOTEBOOK}.ipynb" "${NOTEBOOK}_output.ipynb"
