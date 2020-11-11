from tkinter import ttk
from PIL import ImageTk, Image
import cv2
class Player:
    def __init__(self,video_path,window,width,height):
        self.history_circles = [[]]
        self.play = True
        self.frame = 0
        self.line_i = 0
        self.actual_duration =0
        self.update= False
        self.videoFrame = ttk.Frame(window,width=width, height=height)
        self.videoFrame.pack()
        self.VideoWindow = ttk.Label(self.videoFrame)
        self.VideoWindow.pack()
        self.set_video_duration(video_path)
        self.VideoWindow.bind("<B1-Motion>",self.draw)
        self.VideoWindow.bind("<ButtonRelease-1>",self.handle_drawing)

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
        self.minutes = minutes
        self.seconds = seconds

    def handle_drawing(self,event):
        self.history_circles.append([])
        self.line_i+=1
        #print(self.history_circles)

    def get_video_actual_time(self,duration):
        self.actual_duration = duration/1000
    
    def set_new_msc(self,milisc):
        self.cap.set(cv2.CAP_PROP_POS_MSEC,milisc)
        self.frame =  self.cap.read()[1]

    def draw_lines(self,frame):
        for i in enumerate(self.history_circles):
            for j in enumerate(i[1]):
                try:
                    cv2.line(frame,self.history_circles[i[0]][j[0]],self.history_circles[i[0]][j[0]+1],(0,255,0),thickness=2)
                except:
                    0

    def draw(self,event):
        self.history_circles[self.line_i].append((event.x,event.y))
    def render(self):
        if (self.play):
            ref, frame = self.cap.read()
            self.frame = frame
            self.get_video_actual_time(self.cap.get(cv2.CAP_PROP_POS_MSEC))
            self.update = True        
            if ref: 
                self.draw_lines(self.frame)
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
            self.update=False
            self.draw_lines(self.frame)
            cv2image= cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.VideoWindow.imgtk = imgtk
            self.VideoWindow.configure(image=imgtk)
            self.VideoWindow.after(10,self.render)