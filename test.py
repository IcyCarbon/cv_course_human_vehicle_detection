from ultralytics import YOLO


if __name__ == '__main__':

    model = YOLO("runs/detect/model_large_sat_960_111111/weights/best.pt")
    model.predict('/root/autodl-tmp/cv_task_yolov8/datasets/JPEGImages/00311.jpg', save=True, name='311', line_width=2)