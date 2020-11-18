import numpy
import cv2
import time
import os
import datetime
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
def estimate_fps(cap,startnum=100,totalnum=100):
    for i in range(startnum):
        ret,frame = cap.read()
    tstart = time.time()
    for i in range(totalnum):
        ret,frame = cap.read()
    tend = time.time()
    fps = totalnum / (tend - tstart)
    print("Estimated fps:{0}".format(fps))
    return fps
def add_timestamp(image,timestamp):
#    im=Image.fromarray(image)
#    draw=ImageDraw.Draw(im)
#    font=ImageFont.truetype("ARIAL.TTF",16)
#    draw.text((300,300),"ddd")
    strtime=time.strftime("%H:%M:%S ",time.localtime(timestamp))
    ms=int((float(timestamp) - int(timestamp)) * 1000)
    if ms < 100:
        strtime=strtime+":0{0}".format(ms)
    else:
        strtime=strtime+":{0}".format(ms)
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image,strtime,(500,350),font,0.5,(255,255,255))#,2,cv2.LINE_AA)
#    print(strtime)
#    draw.text((400,200),strtime,font=font)
#    image_mod=numpy.array(im)
    return (image,timestamp)
cap = cv2.VideoCapture(0)
cap.open(0,apiPreference=cv2.CAP_V4L2)
if not cap.isOpened():
    print("CAMERA not open")
    quit()
cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G'))
WIDTH=640
HEIGHT=480
FPS=120
cap.set(cv2.CAP_PROP_FRAME_WIDTH,WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,HEIGHT)
cap.set(cv2.CAP_PROP_FPS,FPS)
ret = True
count=0
fourcc=cv2.VideoWriter_fourcc(*'MJPG')
true_fps = estimate_fps(cap)
out = cv2.VideoWriter("tmp/out.avi",fourcc,true_fps,(WIDTH,HEIGHT))
trealstart=tstart=time.time()
while True:
    ret,frame = cap.read()
    timestamp = time.time()
    image=add_timestamp(frame,timestamp)
    out.write(image[0])
#    if count % 100 == 0:
    cv2.imshow('frame',image[0])
    count += 1
    if count % 100 == 0:
        fps = 100 / (time.time() - tstart)
        tstart = time.time()
        print("fps:{0},now time {1},last time {2}".format(fps,datetime.datetime.now(),tstart-trealstart))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
out.release()
cap.release()
cv2.destroyAllWindows()   
