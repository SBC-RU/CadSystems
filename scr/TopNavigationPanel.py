import pygame as pg
import Colors
from Button import Button
pg.init()

# Загрузка картинок
img_logo = pg.image.load('D:/my projects/Start Brick Co/CadSystems/img/logo.png')

# картинки построения
img_line = pg.image.load('D:/my projects/Start Brick Co/CadSystems/img/navi/line.png')
img_arc = pg.image.load('D:/my projects/Start Brick Co/CadSystems/img/navi/arc.png')
img_circle = pg.image.load('D:/my projects/Start Brick Co/CadSystems/img/navi/circle.png')
# картинки выполнения
img_cancel = pg.image.load('D:/my projects/Start Brick Co/CadSystems/img/navi/cancel.png')
img_save = pg.image.load('D:/my projects/Start Brick Co/CadSystems/img/navi/save.png')

button_x=260 # положение кнопки по X
button_y=12 # положение кнопки по Y
button_indent=10
button_width = 64  # Новая ширина
button_height = 64  # Новая высота

# Масштабирование изображений
img_line_scaled = pg.transform.scale(img_line, (button_width, button_height))
img_arc_scaled = pg.transform.scale(img_arc, (button_width, button_height))
img_circle_scaled = pg.transform.scale(img_circle, (button_width, button_height))
img_cancel_scaled = pg.transform.scale(img_cancel, (button_width, button_height))
img_save_scaled = pg.transform.scale(img_save, (button_width, button_height))

#Инициализация кнопок
button = Button(button_x, button_y, button_width, button_height, "Отрезок", 'Элементы построения','Consolas', 12)
button2 = Button(button_x+button_width+button_indent, button_y, button_width, button_height, "Дуга", 'Элементы построения', 'Consolas',12)
button3 = Button(button_x+(button_width+button_indent)*2, button_y, button_width, button_height, "Окружность", 'Элементы построения', 'Consolas',12)

button4 = Button(button_x+(button_width+button_indent)*3+64, button_y, button_width, button_height, "Отмена", 'Отмена действия','Consolas', 12)
button5 = Button(button_x+(button_width+button_indent)*4+64, button_y, button_width, button_height, "Экспорт", 'Сохранить проект', 'Consolas',12)
def buttons_show(sc):
    # кнопки построения
    button.draw(sc)
    sc.blit(img_line_scaled, (button_x, button_y))
    button2.draw(sc)
    sc.blit(img_arc_scaled, (button_x+button_width+button_indent, button_y))
    button3.draw(sc)
    sc.blit(img_circle_scaled, (button_x+(button_width+button_indent) * 2, button_y))
    # кнопки выполнения
    button4.draw(sc)
    sc.blit(img_cancel_scaled, (button_x + (button_width + button_indent) * 3 + 64, button_y))
    button5.draw(sc)
    sc.blit(img_save_scaled, (button_x + (button_width + button_indent) * 4 + 64, button_y))
    # отображение подсказок
    button.update(pg.mouse.get_pos())
    button2.update(pg.mouse.get_pos())
    button3.update(pg.mouse.get_pos())
    button4.update(pg.mouse.get_pos())
    button5.update(pg.mouse.get_pos())
def action(event):
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:  # Левый клик мыши
            if button.is_clicked(event.pos):
                print("---")
            elif button2.is_clicked(event.pos):
                print('(=')
            elif button3.is_clicked(event.pos):
                print("(О)")
    # Создаем кнопку
def view(sc, width, height):
    pg.draw.polygon(sc, Colors.white, [[0, 0], [0, 90], [width, 90], [width, 0]])
    pg.draw.polygon(sc, Colors.grey, [[0, 90], [0, height], [240, height], [240, 90]])
    sc.blit(img_logo, (0, 0))
    buttons_show(sc)
