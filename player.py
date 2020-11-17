from tkinter import ttk
from PIL import ImageTk, Image
from draw import Draw
import cv2
class Player:
    def __init__(self,video_path,window,width,height):
        self.play = True
        self.frame = 0
        self.actual_duration =0
        self.update= False
        self.videoFrame = ttk.Frame(window,width=width, height=height)
        self.videoFrame.grid(row=0,column=0, padx=10, pady=2)
        self.VideoWindow = ttk.Label(self.videoFrame)
        self.VideoWindow.grid(row=0,column=0)
        self.set_video_duration(video_path)
        self.draw = Draw(self.VideoWindow)

    def set_video_duration(self,video_path):
        self.cap = cv2.VideoCapture(video_path)
        fps = self.cap.get(cv2.CAP_PROP_FPS)      # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
        print(fps)
        frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(frame_count)
        duration = frame_count/fps
        print(duration)
        minutes = int(duration/60)
        seconds = duration%60
        print('duration (M:S) = ' + str(minutes) + ':' + str(seconds))
        self.duration = duration
        self.minutes = minutes # future variables
        self.seconds = seconds

    def get_video_actual_time(self,duration):
        self.actual_duration = duration/1000
    
    def set_new_msc(self,milisc):
        self.cap.set(cv2.CAP_PROP_POS_MSEC,milisc)
        self.frame =  self.cap.read()[1]

    def nextFrame(self):
        self.update=True
        self.play=True
        actual_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, actual_frame+5)
        self.frame = self.cap.read()[1]

    def previousFrame(self):
        self.play = True
        self.update = True
        actual_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES) 
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, actual_frame-10)

    def render(self):
        if (self.play):
            ref, frame = self.cap.read()
            self.frame = frame
            self.get_video_actual_time(self.cap.get(cv2.CAP_PROP_POS_MSEC))
            self.update = True        
            if ref: 
                self.draw.draw_lines(self.frame)
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
            self.draw.draw_lines(self.frame)
            cv2image= cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.VideoWindow.imgtk = imgtk
            self.VideoWindow.configure(image=imgtk)
            self.VideoWindow.after(10,self.render)