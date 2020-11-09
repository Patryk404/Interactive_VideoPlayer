from tkinter import *
from player2 import Player
class Gui:
    def __init__(self,title,path_video):
        self.window = Tk()
        self.window.title(title)
        self.player = Player(path_video,self.window,600,800)
        self.button_frame = Frame(self.window)
        self.button_frame.configure(bg="grey")
        self.button_frame.grid(row=1, column=0)
    def create_Interface(self):
        Button(self.button_frame,text="Play/Stop",width=10,bg="black", fg="white", command=self.handle_playButton_stopButton).grid(row=2, column=2)
        Button(self.button_frame,text="<<", width=5,bg="black", fg="white").grid(row=2,column =1)
        Button(self.button_frame,text=">>", width=5,bg="black", fg="white").grid(row=2,column =3)
        Button(self.button_frame,text="Reset", width=5,bg="black", fg="white", command=self.handle_resetButton).grid(row=2,column = 20)
        self.player.render()
    def handle_playButton_stopButton(self):
        self.player.play = not self.player.play
    def handle_resetButton(self):
        self.player.clear_screen()
    def loop(self):
        self.window.mainloop()