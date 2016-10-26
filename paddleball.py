from tkinter import *
import random
import time
class Ball:
    def _init_(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        
