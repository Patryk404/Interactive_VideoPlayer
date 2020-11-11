import cv2
class Draw:
    def __init__(self,video):
        self.history = [[]]
        self.line_i = 0
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

    def draw_lines(self,frame):
        for i in enumerate(self.history):
            for j in enumerate(i[1]):
                try:
                    cv2.line(frame,self.history[i[0]][j[0]],self.history[i[0]][j[0]+1],(0,255,0),thickness=2)
                except:
                    pass