from tkinter import *
from player import Player

class Gui:
    def __init__(self,title,path_video):
        self.window = Tk()
        self.window.title(title)
        self.player = Player(path_video,self.window,600,800)
        self.button_frame = Frame(self.window)
        self.button_frame.configure(bg="grey")
        self.button_frame.grid(row=1, column=0)
        self.scaleWidget = 0
    def create_Interface(self):
        self.scaleWidget=Scale(self.window,from_=0, to=self.player.duration, resolution=0.1, length=800, orient=HORIZONTAL) # repair this
        self.scaleWidget.grid(row=2,column=0)    
        self.scaleWidget.bind('<ButtonPress>',self.handle_Scale_click)   
        self.scaleWidget.bind('<ButtonRelease>',self.handle_Scale_release)                
        Button(self.button_frame,text="Play/Stop",width=10,bg="black", fg="white", command=self.handle_playButton_stopButton).grid(row=2, column=2)
        Button(self.button_frame,text="<<", width=5,bg="black", fg="white").grid(row=2,column =1)
        Button(self.button_frame,text=">>", width=5,bg="black", fg="white").grid(row=2,column =3)
        Button(self.button_frame,text="Reset", width=5,bg="black", fg="white", command=self.handle_resetButton).grid(row=2,column = 20)
        self.player.render()
    def handle_playButton_stopButton(self):
        self.player.play = not self.player.play
    def update_interface(self):
        if self.player.update:
            self.scaleWidget.set(self.player.actual_duration)
            self.window.after(100,self.update_interface)
        else:
            self.player.set_new_msc(self.scaleWidget.get()*1000)
            self.window.after(100,self.update_interface)
    def handle_Scale_click(self,event):
        self.player.update = False
        self.player.play = False
    def handle_Scale_release(self,event):
        self.player.update = True
    def handle_resetButton(self):
        self.player.clear_screen()
    def loop(self):
        self.window.mainloop()