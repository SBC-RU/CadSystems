import pygame as pg
import Colors

# Загрузка картинок
img_logo = pg.image.load('D:/my projects/Start Brick Co/CadSystems/img/logo.png')

def view(sc, width, height):
    pg.draw.polygon(sc, Colors.white, [[0, 0], [0, 64], [width, 64], [width, 0]])
    sc.blit(img_logo, (0, 0))