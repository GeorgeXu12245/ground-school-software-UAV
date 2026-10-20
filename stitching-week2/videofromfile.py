import numpy as np
import cv2

cap = cv2.VideoCapture('stitching-week2/Minecraft_stitch_test.mp4')
video_fps = cap.get(cv2.CAP_PROP_FPS)
t_1 = 0
t_2 = 120
t = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if t == t_1 or t == t_2:
        cv2.imwrite(f'sampled_frame_{t}.png', frame)
    t+=1
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
