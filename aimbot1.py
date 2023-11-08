import torch
import numpy as np
import pyautogui
import win32api, win32con, win32gui
import cv2
import math
import time

print(torch.cuda.is_available())
detector = torch.hub.load('WongKinYiu/yolov7', 'custom', './best.pt', force_reload=True, trust_repo=True)
detector.to_device('cuda')
classes = ['enemy1', 'enemy2', 'enemy3']
while True:
    # Get rect of Window
    hwnd = win32gui.FindWindow(None, 'GTA: San Andreas')

    rect = win32gui.GetWindowRect(hwnd)
    region = rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1]

    # Get image of screen
    ori_img = np.array(pyautogui.screenshot(region=region))
    ori_img = cv2.cvtColor(ori_img, cv2.IMREAD_COLOR)


    image= cv2.resize(ori_img, (640,480))
    image = np.expand_dims(image, 0)
    img_w, img_h = image.shape[2], image.shape[1]

    # Detection
    result = detector(ori_img)

    labels, cord = result.xyxyn[0][:, -1].cpu().numpy(), result.xyxyn[0][:,:-1].cpu().numpy()
    n= len(labels)

    for i in range(n):
        row= cord[i]
        if row[4] >= 0.65:
            x1, y1, x2, y2 = int(row[0]*img_w), int(row[1]*img_h), int(row[2]*img_w), int(row[3]*img_h)
            if int(labels[i])==0:
                color= (0,255,0)
            if int(labels[i])==1:
                color= (255,0,0)
            if int(labels[i])==2:
                color= (0,0,255)
            cv2.rectangle(ori_img, (x1,y1), (x2,y2), color, 2)
            cv2.putText(ori_img, classes[int(labels[i])], (x1,y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    ori_img = cv2.cvtColor(ori_img, cv2.COLOR_BGR2RGB)
    cv2.imshow("YOLOv7", ori_img)

    key = cv2.waitKey(1)
    if key == ord("q"):
        cv2.destroyAllWindows()
        break

    # Check Closest
    #if len(detected_boxes) >= 1:
        #min = 99999
        #at = 0
        #centers = []
        #for i, box in enumerate(detected_boxes):
            #x1, x2, y1, y2 = box
            #c_x = ((x2 - x1) / 2) + x1
            #c_y = ((y2 - y1) / 2) + y1
            #centers.append((c_x, c_y))
            #dist = math.sqrt(math.pow(img_w/2 - c_x, 2) + math.pow(img_h/2 - c_y, 2))
            #if dist < min:
                #min = dist
                #at = i

        # Pixel difference between crosshair(center) and the closest object
        #x = centers[at][0] - img_w/2
        #y = centers[at][1] - img_h/2 - (detected_boxes[at][3] - detected_boxes[at][2]) * 0.45

        # Move mouse and shoot
        #scale = 1700 * size_scale
        #x = int(x * scale)
        #y = int(y * scale)
        #win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
        #time.sleep(0.05)
        #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        #time.sleep(0.1)
        #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    #ori_img = cv2.cvtColor(ori_img, cv2.COLOR_BGR2RGB)
    #cv2.imshow("ori_img", ori_img)
    #cv2.waitKey(1)

    #time.sleep(0.1)
