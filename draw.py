from tkinter import *

LIST = []
def draw(event):
    LIST.append((event.x,event.y))

def update():
    if not len(LIST):
        canvas.after(1,update)  
    else:
        canvas.create_oval(LIST[len(LIST)-1][0],LIST[len(LIST)-1][1],LIST[len(LIST)-1][0]+5,LIST[len(LIST)-1][1]+5,fill="#000000")
        canvas.after(1,update)  
window = Tk()
window.title("Player")
canvas = Canvas(window,width=800,height=600)
canvas.grid(row=0,column=0, padx=10, pady=2)
canvas.bind("<B1-Motion>",draw)
update()


window.mainloop()