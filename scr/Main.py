import pygame
import pygame as pg
import sys
import Colors
import TopNavigationPanel
# Инициализация Pygame
pg.init()
pg.display.set_caption('ConstantaCad')
width, height = 800, 600
# Создание окна
sc = pg.display.set_mode((width, height))

num1 = 0
num2 = 0
num3 = 0

#Загрузка картинок
#img_logo = pg.image.load('D:/my projects/Start Brick Co/CadSystems/img/logo.png')
img_vectors = pg.image.load('D:/my projects/Start Brick Co/CadSystems/img/vectors.png')
# Ввод нескольких переменных через запятую
user_input = '100, 100, 100' #input("Введите координаты начала отрезка и длину, разделенные запятой: ")

# Разделение строки на отдельные значения
values = user_input.split(',')

# Удаление лишних пробелов
values = [float(value.strip()) for value in values] # Преобразуем в float

# Присваиваем значения переменным num1, num2 и num3
if len(values) >= 3:
    num1 = values[0]
    num2 = values[1]
    num3 = values[2]
else:
    print("Ошибка: введите как минимум 3 значения.")
# Вывод результатов
#print("num1:", num1)
#print("num2:", num2)
#print("num3:", num3)

# Основной цикл программы
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Заполнение фона цветом
    sc.fill(Colors.blue)
    TopNavigationPanel.view(sc, width, height)
    #pg.draw.polygon(sc, Colors.white, [[0, 0], [0, 64], [width, 64], [width, 0]])

    #sc.blit(img_logo, (0, 0))
    sc.blit(img_vectors, (0, height-133))

    # Рисование линий на поверхности sc
    pg.draw.line(sc, Colors.black, [num1, num2], [num1+num3, num2+num3], 3)  # Черная линия
    pg.draw.line(sc, Colors.black, [10, 50], [290, 35])  # Черная линия
    pg.draw.aaline(sc, Colors.black, [10, 70], [18, 70])  # Черная линия
    pg.draw.polygon(sc, Colors.black,[[250, 110],[280, 150],[190, 190],[130, 130],[100, 130]])

    # Обновление дисплея
    pg.display.update()

    # Задержка на 1000 миллисекунд (1 секунда)
    pg.time.delay(1000)

# Завершение Pygame
pg.quit()
sys.exit()


