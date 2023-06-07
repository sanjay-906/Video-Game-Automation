import cv2
import matplotlib.pyplot as plt

config_file='ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model= 'frozen_inference_graph.pb'

model= cv2.dnn_DetectionModel(frozen_model, config_file)
model.setInputParams(size=(150,150), scale=1/255, swapRB=True)
classlabels=[]
file_name= 'labels.txt'
with open(file_name, 'rt') as f:
    classlabels= f.read().rstrip('\n').split('\n')


cap= cv2.VideoCapture('ip.mp4')
if not cap.isOpened():
    cap= cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open the video")



while True:
    ret, frame= cap.read()
    class_idx, conf, bbox= model.detect(frame, confThreshold= 0.55 )

    print(class_idx)
    if len(class_idx)!=0:
        for ci, cf, bb in zip(class_idx.flatten(), conf.flatten(), bbox):
            if ci<=80:
                cv2.rectangle(frame, bb, (0,255,0),2)
                cv2.putText(frame, classlabels[ci-1], (bb[0]+10, bb[1]+40), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 2)
    cv2.imshow('Object Detection', frame)

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
