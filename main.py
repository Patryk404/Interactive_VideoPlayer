import cv2 
import numpy as np
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve

cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Video', 1000,1000)
cap = cv2.VideoCapture('./video.mp4')
# Create a black image
LIST=[]

def clear_frame():
    LIST.clear()

def add_circles_to_frame():
    for i in LIST:
        cv2.circle(FRAME,i,5,(0,0,255),-1)

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.circle(FRAME,(x,y),5,(0,0,255),-1)
                LIST.append((x,y))
            else:
                cv2.circle(FRAME,(x,y),5,(0,0,255),-1)
                LIST.append((x,y))
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.circle(FRAME,(x,y),5,(0,0,255),-1)
            LIST.append((x,y))
        else:
            cv2.circle(FRAME,(x,y),5,(0,0,255),-1)
            LIST.append((x,y))

cv2.setMouseCallback('Video',draw_circle)
while True:
    ret, frame = cap.read()
    if ret:
        FRAME=frame
        add_circles_to_frame()
        cv2.imshow('Video',FRAME)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('c'):
            clear_frame()
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)

cap.release()
cv2.destroyAllWindows()