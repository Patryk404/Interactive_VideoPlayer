from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import cv2 

window = Tk()
window.title("Player")

videoFrame = ttk.Frame(window, width=600, height=500)
videoFrame.grid(row=0, column=0, padx=10, pady=2)

#Capture video frames
lmain = ttk.Label(videoFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture('./video.mp4')
def show_frame():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame) 


show_frame()
window.mainloop()