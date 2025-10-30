import cv2

def overlay_prediction(frame, label, confidence, fps=None):
    banner = "AI Vision by Deepthi RG"
    cv2.putText(frame, banner, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)
    text = f"{label}: {confidence*100:.2f}%"
    cv2.putText(frame, text, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    if fps is not None:
        cv2.putText(frame, f"FPS: {fps:.1f}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    return frame
