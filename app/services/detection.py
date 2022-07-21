from app.models.object_detection.yolov5.detect import Inference

class InferenceDetection:
    """Inference Detection model"""
    
    def __init__(self,
                 checkpoint_path: str,
                 conf_thres: float = 0.45, 
                 iou_thres: float = 0.45, 
                ) -> None:
        self.conf_thres = conf_thres
        self.iou_thres = iou_thres
        self.model = Inference(checkpoint_path)
    
    def __call__(self, source):
        return self.model.run(source=source, conf_thres=self.conf_thres, iou_thres=self.iou_thres)