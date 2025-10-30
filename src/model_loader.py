from keras.applications.mobilenet_v2 import MobileNetV2,preprocess_input, decode_predictions
def load_model():
    """Load pretrained MobileNetV2 model"""
    return MobileNetV2(weights='imagenet')
