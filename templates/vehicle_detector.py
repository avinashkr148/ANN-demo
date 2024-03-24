class VehicleDetector:
    def __init__(self):
        net = cv2.readNet("dnn_model/yolo4.weights",)