from tkinter import ttk
from PIL import ImageTk, Image
import cv2
class Player:
    def __init__(self,video_path,window,width,height):
        self.history_circles = []
        self.play = True
        self.frame = 0
        self.videoFrame = ttk.Frame(window,width=width, height=height)
        self.videoFrame.grid(row=0,column=0, padx=10, pady=2)
        self.VideoWindow = ttk.Label(self.videoFrame)
        self.VideoWindow.grid(row=0,column=0)
        self.VideoWindow.bind("<B1-Motion>",self.handle_mouse)
        self.VideoWindow.pack()
        self.cap = cv2.VideoCapture(video_path)
    def handle_mouse(self,event):
        self.history_circles.append((event.x,event.y))
    def clear_screen(self):
        self.history_circles= []
        frame = self.cap.read()[1]
        self.frame = frame
    def render(self):
        if (self.play):
            ref, frame = self.cap.read()
            self.frame = frame
            if ref: 
                for position in self.history_circles:
                    cv2.circle(frame,position,5,(0,0,255),thickness=-1)
                cv2image= cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)
                img = Image.fromarray(cv2image)
                imgtk = ImageTk.PhotoImage(image=img)
                self.VideoWindow.imgtk = imgtk
                self.VideoWindow.configure(image=imgtk)
                self.VideoWindow.after(10,self.render)
            else:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES,0)
                self.VideoWindow.after(10, self.render)
        else:
            for position in self.history_circles:
                cv2.circle(self.frame,position,5,(0,0,255),thickness=-1)
            cv2image= cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.VideoWindow.imgtk = imgtk
            self.VideoWindow.configure(image=imgtk)
            self.VideoWindow.after(10,self.render)
