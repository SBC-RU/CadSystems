import pygame as pg
import Colors

pg.init()

workpanel_width = 100  # ширина рабочей области
workpanel_height = 100  # высота рабочей области

coord_x = 280
coord_y = workpanel_height
#Загрузка картинок
img_vectors = pg.image.load('D:/my projects/Start Brick Co/CadSystems/img/vectors.png')

def create_field (sc, workpanel_width, workpanel_height):
    #pg.draw.line(sc, Colors.grey, [num1, num2], [num1+num3, num2+num3], 3)
    pg.draw.rect(sc, Colors.grey, (280, 130, workpanel_width, workpanel_height), 1)
def view(sc, width, height):
    workpanel_width = width - 280 * 2
    workpanel_height = height - 130 * 2
    create_field(sc, workpanel_width, workpanel_height)
    coord_y = workpanel_height+2
    sc.blit(img_vectors, (coord_x, coord_y))
    return coord_y  # Возвращаем новое значение coord_y

