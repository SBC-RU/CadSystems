import pygame as pg
from scr.interface_elements.Text import Text
from scr.interface_elements.Button import Button
import Colors

# Инициализация Pygame
pg.init()

# Загрузка картинок
img_promo = pg.image.load('D:/my projects/Start Brick Co/CadSystems/img/promo.png')
img_2d = pg.image.load('D:/my projects/Start Brick Co/CadSystems/img/navi/2d.png')
img_3d = pg.image.load('D:/my projects/Start Brick Co/CadSystems/img/navi/3d.png')

# Класс всплывающего окна
class WelcomeWindow:
    def __init__(self, width, height):  # Исправлено на __init__
        window_width = 600  # ширина окна
        window_height = 300  # высота окна

        window_x = width // 2 - window_width // 2
        window_y = height // 2 - window_height // 2
        self.text_x = window_x + 220  # Исправлено на правильное значение
        self.text_y = window_y + 40
        self.check = True  # Открыто ли окно приветствия #для запуска ИСПРАВЬ на TRUE

        # Инициализация текста и кнопок
        self.text = Text(self.text_x, self.text_y + 20, "Добро пожаловать!", Colors.black, 'Consolas', 28)
        self.text2 = Text(self.text_x, self.text_y + 70, "Выбор прост:", Colors.dark_grey, 'Consolas', 22)
        self.button = Button(self.text_x, self.text_y + 110, 64, 64, " ", 'Новый 2D проект', 'Consolas',16)
        self.button2 = Button(self.text_x + 74, self.text_y + 110, 64, 64, " ", 'Новый 3D проект', 'Consolas',16)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левый клик мыши
                if self.button.is_clicked(event.pos):
                    print("2D button clicked")
                    self.check = False  # Закрываем окно при нажатии на кнопку
                elif self.button2.is_clicked(event.pos):
                    print("3D button clicked")
                    self.check = False  # Закрываем окно при нажатии на кнопку

    def show(self, sc):
        window_width = 600  # ширина окна
        window_height = 300  # высота окна

        window_x = sc.get_width() // 2 - window_width // 2
        window_y = sc.get_height() // 2 - window_height // 2

        # Отображение фона окна
        pg.draw.polygon(sc, Colors.white, [[window_x, window_y],
                                            [window_x, window_y + window_height],
                                            [window_x + window_width, window_y + window_height],
                                            [window_x + window_width, window_y]])
        pg.draw.polygon(sc, Colors.dark_grey, [[window_x + 200, window_y],
                                                 [window_x + 200, window_y + 40],
                                                 [window_x + window_width, window_y + 40],
                                                 [window_x + window_width, window_y]])

        sc.blit(img_promo, (window_x, window_y))
        self.text.draw(sc)
        self.text2.draw(sc)
        self.button.draw(sc)
        sc.blit(img_2d, (self.text_x, self.text_y + 110))
        self.button2.draw(sc)
        sc.blit(img_3d, (self.text_x + 74, self.text_y + 110))
        self.button.update(pg.mouse.get_pos())
        self.button2.update(pg.mouse.get_pos())