import os
import time
import cv2
import numpy as np
from PIL import Image
from threading import Thread

HAARCASCADE_PATH = "haarcascade_frontalface_default.xml"
TRAINING_IMAGE_PATH = "TrainingImage"
TRAINING_IMAGE_LABEL_PATH = "TrainingImageLabel"
TRAINNER_FILE_NAME = "Trainner.yml"

def get_labels_and_images(image_path):
    """
    Get the path of all the files in the folder and extract the enrollment numbers and the images.
    :param image_path: Path of the folder containing the images.
    :return: faces, enrollment_no
    """
    image_paths = [os.path.join(image_path, f) for f in os.listdir(image_path)]

    faces = []
    enrollment_no = []

    for image_path in image_paths:
        # Load image and convert to grayscale
        gray_image = Image.open(image_path).convert('L')

        # Convert image into numpy array
        image_np = np.array(gray_image, 'uint8')

        # Get the enrollment no from the image
        enrol_no = int(os.path.split(image_path)[-1].split(".")[1])

        # Extract the face from the training image sample
        faces.append(image_np)
        enrollment_no.append(enrol_no)

    return faces, enrollment_no


def train_images():
    """
    Train the images and save the trainner file.
    """
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    detector = cv2.CascadeClassifier(HAARCASCADE_PATH)
    faces, id_ = get_labels_and_images(TRAINING_IMAGE_PATH)
    Thread(target=recognizer.train(faces, np.array(id_))).start()

    # Optional for a visual counter effect
    Thread(target=counter_img(TRAINING_IMAGE_PATH)).start()

    recognizer.save(os.path.join(TRAINING_IMAGE_LABEL_PATH, TRAINNER_FILE_NAME))
    print("All Images Trained")


def counter_img(image_path):
    """
    Optional, adds a counter for images trained.
    :param image_path: Path of the folder containing the images.
    """
    img_counter = 1
    image_paths = [os.path.join(image_path, f) for f in os.listdir(image_path)]
    for image_path in image_paths:
        print(f"{img_counter} Images Trained", end="\r")
        time.sleep(0.008)
        img_counter += 1


