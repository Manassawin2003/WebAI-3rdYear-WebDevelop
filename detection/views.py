# detection/views.py
from django.shortcuts import render
from django.http import StreamingHttpResponse
import cv2
import tensorflow as tf
import numpy as np
import os


MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models/keras_model.h5')
LABELS_PATH = os.path.join(os.path.dirname(__file__), 'models/labels.txt')


model = tf.keras.models.load_model(MODEL_PATH)

label_map = {}
with open(LABELS_PATH, 'r') as file:
    for line in file:
        class_id, class_name = line.strip().split()
        label_map[int(class_id)] = class_name


def process_frame(frame):
    img = cv2.resize(frame, (224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)


    predictions = model.predict(img_array)
    predicted_class_id = np.argmax(predictions, axis=1)[0]
    predicted_class_label = label_map[predicted_class_id]


    cv2.putText(frame, f'Prediction: {predicted_class_label}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    return frame


def gen_frames():
    cap = cv2.VideoCapture(1) #เปลี่ยนกล้องตามไอดี 0 กล้องNOTEBOOK 1กล้องIruin
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame = process_frame(frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()



def video_feed(request):
    return StreamingHttpResponse(gen_frames(), content_type='multipart/x-mixed-replace; boundary=frame')



def index(request):
    return render(request, 'detection/index.html')
