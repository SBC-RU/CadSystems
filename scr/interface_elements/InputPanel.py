import pygame as pg
from scr import Colors

from scr.interface_elements.Text import Text

class InputPanel:
    def __init__(self, x, y, header, i_count, btn_count):
        self.x = x
        self.y = y
        self.header = Text(self.x + 10, self.y + 10, str(header), Colors.dark_grey, 'Consolas', 16)
        self.input_count = i_count
        self.btn_count = btn_count
    def active(self, sc):
        height = 200
        pg.draw.polygon(sc, Colors.white, [[self.x, self.y], [self.x, height], [220, height], [220, self.y]])  # отрисовка фона окна ввода
        self.header.draw(sc) # отрисовка заголовка
        #if self.input_count == 0:


