import cv2

def get_video_stream(source=0):
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise Exception("Could not open webcam. Check camera permissions.")
    return cap
