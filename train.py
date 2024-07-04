import warnings

import torch.cuda

from ultralytics import YOLO
warnings.filterwarnings('ignore')
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'


if __name__ == '__main__':

    model = YOLO('/root/autodl-tmp/cv_task_yolov8/ultralytics/cfg/models/v8/yolov8m-sat.yaml')
    model.load("./yolov8m.pt")
    torch.cuda.empty_cache()
    # for name, param in model.model.named_parameters():
    #     if not name.startswith('model.0'):
    #         if not name.startswith('model.23'):
    #             param.requires_grad = False
    #             print(f"Froze layer: {name}")
    model.train(
                data=r'/root/autodl-tmp/cv_task_yolov8/datasets/VOC.yaml',
                name='model_large_sat_960_111111',
                cache=True,
                imgsz=960,
                epochs=200,
                batch=-1,
                device='0',
                optimizer='SGD',
                hsv_h=0.05,
                hsv_s=0.8,
                hsv_v=0.5,
                flipud=0.1,
                fliplr=0.5,
                mixup=0.1,
                conf=0.3,
                )