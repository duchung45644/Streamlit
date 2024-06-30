import cv2
import numpy as np
import streamlit as st
from PIL import Image

MODEL = 'model/MobileNetSSD_deploy.caffemodel'
PROTOTXT = 'model/MobileNetSSD_deploy.prototxt.txt'

CLASSES = {0: 'background',
              1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
              5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
              10: 'cow', 11: 'diningtable', 12: 'dog', 13: 'horse',
              14: 'motorbike', 15: 'person', 16: 'pottedplant',
              17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tv/monitor'}


def process_image(image):
    blob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5
    )
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
    net.setInput(blob)
    detections = net.forward()
    return detections


def annotate_image(image, detections, confidence_threshold=0.5):
    (h, v) = image.shape[:2]
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > confidence_threshold:
            idx = int(detections[0, 0, i, 1])
            class_name = CLASSES[idx]
            box = detections[0, 0, i, 3:7] * np.array([v, h, v, h])
            (start_x, start_y, end_x, end_y) = box.astype("int")
            cv2.rectangle(image, (start_x, start_y), (end_x, end_y), 70, 2)

            label = f"{class_name}: {confidence:.2f}"

            cv2.putText(image, label, (start_x + 15, start_y + 20),
                        cv2.FONT_ITALIC, 0.7, (225, 0, 0), 2)
    return image


def main():
    st.title('Object Detection for Images')
    file = st.file_uploader('Upload Image', type=['jpg', 'png', 'jpeg'])
    if file is not None:
        col1, col2 = st.columns(2)
        with col1:
            st.image(file, caption="Uploaded Image")

        image = Image.open(file)
        image = np.array(image)
        detections = process_image(image)
        processed_image = annotate_image(image, detections)
        with col2:
            st.image(processed_image, caption="Processed Image")


if __name__ == "__main__":
    main()
