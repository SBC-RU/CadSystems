import pygame as pg
import Colors

pg.init()

workspace_width = 100  # ширина рабочей области
workspace_height = 100  # высота рабочей области

mark_x = 280 # Координата начала поля по Х
mark_y = 130 # Координата начала поля по У

coord_x = 280 # Координата начала Ох
coord_y = workspace_height # Координата начала Оу
#Загрузка картинок
img_vectors = pg.image.load('D:/my projects/Start Brick Co/CadSystems/img/vectors.png')

def create_field (sc, workspace_width, workspace_height):
    pg.draw.rect(sc, Colors.grey, (mark_x, mark_y, workspace_width, workspace_height), 1)

def spatial_positioning(): #функция расстановки точек пространственного позиционирования
    print('Point')

def view(sc, width, height):
    workspace_width = width - mark_x * 2
    workspace_height = height - mark_y * 2
    create_field(sc, workspace_width, workspace_height)
    coord_y = workspace_height+mark_y
    # print(coord_x, coord_y)
    sc.blit(img_vectors, (coord_x, coord_y-128)) #где 128 - это высота png
    pg.draw.line(sc, Colors.grey, [coord_x, coord_y], [coord_x+100, coord_y-100], 3)
    return coord_y  # Возвращаем новое значение coord_y


