import numpy as np
import cv2
import time
WIDTH=640
HEIGHT=480
TIME=20
cap = cv2.VideoCapture(0)
while not cap.isOpened():
    cap.open()
try:
    cap.set(3,WIDTH)
    cap.set(4,HEIGHT)
except Exception:
    print("cap set {0}*{1} failed".format(WIDTH,HEIGHT))
    quit()
print("width"+str(cap.get(3))+"height"+str(cap.get(4)))
frames = []
count = 0
while(True):
    ret, frame = cap.read()
    if ret != True:
        print("Video capture failed")
        quit()
    frames.append(frame)
    count += 1
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter("output.avi",fourcc,fps,(WIDTH,HEIGHT))
for frame in frames:
    out.write(frame)
cap.release()
cv2.destroyAllWindows()
