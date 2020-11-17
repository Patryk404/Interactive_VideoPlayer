import cv2

RED = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
PURPLE = (128, 0, 128) 

class Draw:
    def __init__(self,video):
        self.history = [[]]
        self.line_i = 0
        self.color= GREEN
        video.bind("<B1-Motion>",self.draw)
        video.bind("<ButtonRelease-1>",self.handle_drawing)

    def clear_screen(self):
        self.history = [[]]
        self.line_i = 0

    def handle_drawing(self,event):
        self.history.append([])
        self.line_i += 1 

    def draw(self,event):
        self.history[self.line_i].append((event.x,event.y))

    def set_color(self,color):
        if color=="RED":
            self.color = RED
        elif color =="GREEN":
            self.color = GREEN
        elif color =="BLACK":
            self.color = BLACK
        elif color =="PURPLE":
            self.color = PURPLE

    def draw_lines(self,frame):
        for i in enumerate(self.history):
            for j in enumerate(i[1]):
                try:
                    cv2.line(frame,self.history[i[0]][j[0]],self.history[i[0]][j[0]+1],self.color,thickness=2)
                except:
                    pass
