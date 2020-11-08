import cv2 as cv
import sys
class Player:

    def __init__(self):
        self.history_paint = []
        self.cap = cv.VideoCapture(sys.argv[1])
        self.ix = 0
        self.iy = 0
        self.frame = 0
        self.drawing = False
        self.quit = False
        self.pause = False
        self.cap.set(cv.CAP_PROP_FPS, 30)
        cv.namedWindow("Player",cv.WINDOW_GUI_NORMAL)
        cv.resizeWindow("Player", 1000,1000)

    def init_GUI(self):
        return 0

    def run(self):
        cv.setMouseCallback("Player",self.handle_paint)
        while self.quit == False:
            if self.pause == False:
                ret, frame = self.cap.read()
                if ret:
                    self.frame=frame
                    self.add_circles_to_frame()
                    cv.imshow("Player",self.frame)
                    self.handle_clicks()
                    # get current positions of four trackbars
                else:
                    self.cap.set(cv.CAP_PROP_POS_FRAMES,0)
            else:
                self.add_circles_to_frame()
                cv.imshow("Player",self.frame)
                self.handle_clicks()
        self.cap.release()
        cv.destroyAllWindows()

    def add_circles_to_frame(self):
        for i in self.history_paint:
            cv.circle(self.frame,i,5,(0,0,255),-1)

    def handle_clicks(self):
        key = cv.waitKey(30) #framerate limit 
        if key == ord('q'):
            self.quit = True
        elif key == ord('c'):
            self.clear_frame()
        elif key == ord('p'):
            self.pause_video()

    def set_frame_rate_limit(self):
        return 0

    def add_frame(self):
        self.frame = self.cap.read()[1]

    def clear_frame(self):
        self.history_paint = []
        self.add_frame()

    def pause_video(self):
        self.pause = not self.pause

    def handle_paint(self,event,x,y,flags,param):
        if event == cv.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.ix, self.iy = x,y
        elif event == cv.EVENT_MOUSEMOVE:
            if self.drawing == True:
                    cv.circle(self.frame,(x,y),1,(0,0,255))
                    self.history_paint.append((x,y))
        elif event == cv.EVENT_LBUTTONUP:
            self.drawing = False
            cv.circle(self.frame,(x,y),1,(0,0,255))
            self.history_paint.append((x,y))