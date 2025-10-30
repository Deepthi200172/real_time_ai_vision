import cv2
import numpy as np
from keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def predict_frame(model, frame):
    """Predict the top class label for a frame"""
    frame_resized = cv2.resize(frame, (224, 224))
    x = np.expand_dims(frame_resized, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    decoded = decode_predictions(preds, top=1)[0][0]
    label, confidence = decoded[1], float(decoded[2])
    return label, confidence
