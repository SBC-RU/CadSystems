from scr import Colors
import pygame as pg
from scr.Button import Button
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.button = Button(self.x-5, self.y-5, 10, 10, " ", 'x:'+ str(x) +' y:' + str(y), 'Consolas', 12)

        print('+++')
    def draw(self,sc):
        self.button.draw(sc)
        self.button.update(pg.mouse.get_pos())