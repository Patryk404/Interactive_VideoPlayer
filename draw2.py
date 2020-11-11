from tkinter import *
from PIL import Image, ImageTk
class Draw:
    def __init__(self,window):
        self.history_cicles = []
        window.bind("<B1-Motion>",self.draw)
    def draw(self,event):
        self.history_cicles.append((event.x,event.y))
    def update(self,canvas):
        if not len(self.history_cicles):
            canvas.after(1,self.update)  
        else:
            canvas.create_oval(self.history_cicles[len(self.history_cicles)-1][0],self.history_cicles[len(self.history_cicles)-1][1],self.history_cicles[len(self.history_cicles)-1][0]+5,self.history_cicles[len(self.history_cicles)-1][1]+5,fill="#000000")
            canvas.after(1,self.update)  