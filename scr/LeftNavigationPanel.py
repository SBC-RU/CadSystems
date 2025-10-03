import pygame as pg
import Colors
from scr.interface_elements.InputPanel import InputPanel

pg.init()
# положение для InputPanel
front_x = 10
front_y = 90 + 20
# переменная хранит номер активной вкладки
index_input_panel = 0

# Инициализация
line = InputPanel(front_x, front_y,'Отрезок', 0, 2 )
arc = InputPanel(front_x, front_y,'Дуга', 0, 2 )
circle = InputPanel(front_x, front_y,'Окружность', 0, 2 )

def show_input_panel(sc):
    if index_input_panel == 1:
        #панель ввода значений - прямой
        line.active(sc)
    elif index_input_panel == 2:
        # панель ввода значений - дуги
        arc.active(sc)
    elif index_input_panel == 3:
        # панель ввода значений - окружности
        circle.active(sc)

def view(sc, width, height):
    pg.draw.polygon(sc, Colors.grey, [[0, 90], [0, height], [240, height], [240, 90]]) #отрисовка фона
    #print(index_input_panel)
    show_input_panel(sc)