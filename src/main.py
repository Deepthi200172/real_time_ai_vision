import cv2
from model_loader import load_model
from video_stream import get_video_stream
from predictor import predict_frame
from visualizer import overlay_prediction
from utils import FPSCounter
import pyttsx3
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def main():
    print("🚀 Loading model...")
    model = load_model()

    print("🎥 Starting webcam...")
    cap = get_video_stream()
    fps_counter = FPSCounter()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        label, conf = predict_frame(model, frame)
        if conf > 0.75:       # only speak if confidence > 75%
            speak(f"{label}")
        fps = fps_counter.get_fps()
        frame = overlay_prediction(frame, label, conf, fps)

        cv2.imshow("AI Vision - Live (Press Q to quit)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("👋 Exiting...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
