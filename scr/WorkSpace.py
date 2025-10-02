import pygame as pg
import Colors
import Scale
import math
from Text import Text
from elements.Point import Point
pg.init()

# 1x100px = 10мм
cell_size = 100 #размер ячейки (клетки) 100px на 100px
workspace_width = 100  # ширина рабочей области
workspace_height = 100  # высота рабочей области

mark_x = 280 # Координата начала поля по Х
mark_y = 130 # Координата начала поля по У

coord_x = 280 # Координата начала Ох
coord_y = workspace_height # Координата начала Оу
#Загрузка картинок
img_vectors = pg.image.load('D:/my projects/Start Brick Co/CadSystems/img/vectors.png')

elements_list = [] #список геометрических объектов на доске


def add_element(element):
    """Добавляет элемент в список."""
    elements_list.append(element)
    print(f'Элемент "{element}" добавлен в список.')

point = Point(400, 200)
add_element(point)

def traverse_list(sc):
    """Проходит по всем элементам списка и выводит их на экран."""
    for item in elements_list:
        item.draw(sc)

def create_field (sc, workspace_width, workspace_height):
    pg.draw.rect(sc, Colors.grey, (mark_x, mark_y, workspace_width, workspace_height), 1)

def spatial_positioning(): #функция сетки пространственного позиционирования
    print('Point')
def scale_grid(sc, workspace_width, workspace_height, coord_y):
    new_cell_size=math.floor(Scale.value * cell_size)
    scale_text = Text(mark_x, mark_y - 20, "Масштаб: x"+str(Scale.value), Colors.black, 'Consolas', 20)
    scale_text.draw(sc)
    count_X = workspace_width // new_cell_size
    count_Y = workspace_height // new_cell_size
    print('X', count_X, 'Y', count_Y)
    for x in range(count_X+1):
        if x>0:
            pg.draw.line(sc, Colors.grey, [coord_x+new_cell_size*x, coord_y], [coord_x+new_cell_size*x, mark_y], 1)
    for y in range(count_Y+1):
        if y>0:
            pg.draw.line(sc, Colors.grey, [coord_x, coord_y-new_cell_size*y], [coord_x+workspace_width, coord_y-new_cell_size*y], 1)



def view(sc, width, height):
    workspace_width = width - mark_x * 2
    workspace_height = height - mark_y * 2
    create_field(sc, workspace_width, workspace_height)
    coord_y = workspace_height+mark_y
    scale_grid(sc, workspace_width, workspace_height, coord_y)
    sc.blit(img_vectors, (coord_x, coord_y-128)) #где 128 - это высота png
    pg.draw.line(sc, Colors.grey, [coord_x, coord_y], [coord_x+100, coord_y-100], 3)

    #point.draw(sc)
    traverse_list(sc)
    
    return coord_y  # Возвращаем новое значение coord_y


