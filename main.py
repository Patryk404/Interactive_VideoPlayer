from tkinter import *
import sys
from GUI import Gui

GUI = Gui("Player",sys.argv[1])
        
GUI.create_Interface()

GUI.update_interface()

GUI.loop()