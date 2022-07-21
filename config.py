# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

#TODO: move to DB
MODELS_CONFIG = {
    "PRODUCT_DETECTION": {
        "instance": "InferenceDetection",
        "checkpoint_path": "yolov5l-nutifood.pt",
    },
    "SHELF_DETECTION": {
        "instance": "InferenceDetection",
        "checkpoint_path": "yolov5s-nutifood-shelf.pt",
    },
    "CAN_DETECTION": {
        "instance": "InferenceDetection",
        "checkpoint_path": "yolov5s-milk-can.pt",
    },
    "ANTI_SPOOFING_CLASSIFICATION": {
        "instance": "InferenceClassification",
        "checkpoint_path": "",
        # "checkpoint_path": "mixnet_s-anti-spoofing.pth",
    },
}