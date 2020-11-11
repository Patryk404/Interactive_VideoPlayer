from tkinter import *
from PIL import Image, ImageTk
class Draw:
    def __init__(self,window):
        self.history_cicles = []
        window.bind("<ButtonPress-1>",self.handle_button)
        window.bind("<ButtonRelease-1>",self.handle_button)
        window.bind("<B1-Motion>",self.draw)
    def draw(self,event,line_i):
        self.history_cicles[line_i].append((event.x,event.y))
    def handle_button(self,event,line_i):
        if event.type == event.type.ButtonRelease:
            line_i += 1