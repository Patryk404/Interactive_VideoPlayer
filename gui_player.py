from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import cv2 

window = Tk()
window.title("Player")
videoFrame = ttk.Frame(window, width=600, height=500)
videoFrame.grid(row=0, column=0, padx=10, pady=2)

LIST=[]

def handle_mouse_click(event):
    LIST.append((event.x,event.y))

#Capture video frames

lmain = ttk.Label(videoFrame)
lmain.grid(row=0, column=0)
lmain.bind("<B1-Motion>", handle_mouse_click)
lmain.pack()
cap = cv2.VideoCapture('./video.mp4')

def show_frame():
    ref, frame = cap.read()
    if ref:
        for i in LIST:
            cv2.circle(frame,i,5,(0,0,255),thickness=-1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame) 
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
        lmain.after(10, show_frame) 
show_frame()
window.mainloop()