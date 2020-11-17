from tkinter import *
from player import Player

class Gui:
    def __init__(self,title,path_video):
        self.window = Tk()
        self.window.geometry("1500x800")
        self.window.title(title)
        self.player = Player(path_video,self.window,600,800)
        self.button_frame = Frame(self.window)
        self.button_frame.configure(bg="grey")
        self.button_frame.grid(row=1, column=0)
        self.scale_widget = 0
        self.choose_color_list_box= 0

    def create_Interface(self):
        self.scale_widget=Scale(self.window,from_=0, to=self.player.duration, resolution=0.1, length=800, orient=HORIZONTAL)
        self.scale_widget.grid(row=2,column=0) 
        self.choose_color_list_box = Listbox(self.window, width=20, height = 4)
        self.choose_color_list_box.insert(END,"RED")
        self.choose_color_list_box.insert(END,"GREEN")
        self.choose_color_list_box.insert(END,"BLACK")
        self.choose_color_list_box.insert(END,"PURPLE")
        self.choose_color_list_box.select_set(1)
        self.choose_color_list_box.place(x=1300,y=20)
        self.scale_widget.bind('<ButtonPress>',self.handle_Scale_click)   
        self.scale_widget.bind('<ButtonRelease>',self.handle_Scale_release)      
        self.choose_color_list_box.bind('<<ListboxSelect>>',self.handle_listbox_click)
        Button(self.button_frame,text="Play/Stop",width=10,bg="black", fg="white", command=self.handle_playButton_stopButton).grid(row=2, column=2)
        Button(self.button_frame,text="<<", width=5,bg="black", fg="white",command=self.handle_previousframeButton).grid(row=2,column =1)
        Button(self.button_frame,text=">>", width=5,bg="black", fg="white",command=self.handle_nextframeButton).grid(row=2,column =3)
        Button(self.button_frame,text="Reset", width=5,bg="black", fg="white", command=self.handle_resetButton).grid(row=2,column = 20)
        self.player.render()

    def handle_playButton_stopButton(self):
        self.player.play = not self.player.play

    def handle_listbox_click(self,event):
        cs = event.widget.curselection()

        for  list in cs:
            if list == 0:
                self.player.draw.set_color("RED")
            elif list == 1:
                self.player.draw.set_color("GREEN")
            elif list == 2:
                self.player.draw.set_color("BLACK")
            elif list == 3:
                self.player.draw.set_color("PURPLE")


    def handle_resetButton(self):
        self.player.nextFrame()
        self.player.play = False
        self.player.draw.clear_screen()

    def handle_nextframeButton(self):
        self.player.nextFrame()

    def handle_previousframeButton(self):
        self.player.previousFrame()

    def update_interface(self):
        if self.player.update:
            self.scale_widget.set(self.player.actual_duration)
            self.window.after(100,self.update_interface)
        else:
            self.player.set_new_msc(self.scale_widget.get()*1000)
            self.window.after(100,self.update_interface)

    def handle_Scale_click(self,event):
        self.player.update = False
        self.player.play = False

    def handle_Scale_release(self,event):
        self.player.update = True

    def loop(self):
        self.window.mainloop()