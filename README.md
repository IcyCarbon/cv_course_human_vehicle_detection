# Human Vehicle Detection

The purpose of this task is to combine the cutting-edge technologies in the field of computer vision to carry out high-precision human-vehicle detection under the top-down view for the images captured at the high and medium positions of the pylons. Through teamwork, students will learn skills such as analyzing experimental results, adjusting model hyperparameters, optimizing network structure, etc., to improve teamwork and practical ability.

## 1 Dataset

> Dataset: This task provides 500 image data and labeled files from multiple day/night roadway pedestrian and vehicle scenes.
>
> ├──dataset：
>
> ​       ├── Annotations: All images (500)
>
> ​       └── JPEGImages: All annotated documents (500)

## 2 Model

Use ultralytics YOLOv8 [ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) with add modules (see  ./ultralytics/nn/Addmodules).



## 3 Outcome

| Model                   | mAP@50 | Car mAP@50 | Person mAP@50 | FPS  |
| ----------------------- | ------ | ---------- | ------------- | ---- |
| YOLOv8m                 | 83.9%  | 85.3%      | 82.5%         | 79.4 |
| YOLOv8m-SENetV2-DA      | 85.3%  | 86.2%      | 84.4%         | 49.8 |
| YOLOv8m-SENetV2-DA(960) | 90.8%  | 90.2%      | 91.5%         | 35.5 |

