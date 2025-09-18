
import pygame as pg
import sys
import Colors
import TopNavigationPanel
import WorkPanel
from WelcomeWindow import WelcomeWindow

# Инициализация Pygame
pg.init()

infoObject = pg.display.Info()
screen_width = infoObject.current_w
screen_height = infoObject.current_h

pg.display.set_caption('ConstantaCad')
width, height = screen_width - 50, screen_height - 50

print(f"Width: {screen_width}, Height: {screen_height}")

# Создание окна
sc = pg.display.set_mode((width, height))

# Создание экземпляра окна приветствия
welcome_window = WelcomeWindow(width, height)  # Укажите координаты для текста

# Основной цикл программы
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # Обработка событий для панели навигации
        TopNavigationPanel.action(event)
        if welcome_window.check:
            # Обработка событий для окна приветствия
            welcome_window.handle_event(event)

    # Если окно приветствия открыто, отображаем его
    if welcome_window.check:
        sc.fill(Colors.blue)  # Задаем фон только если окно приветствия не активно
        welcome_window.show(sc)  # Отображение окна приветствия
    else:
        # Заполнение фона цветом и отображение панелей только после закрытия окна приветствия
        sc.fill(Colors.blue)
        TopNavigationPanel.view(sc, width, height)
        WorkPanel.view(sc, width, height)

    # Обновление дисплея
    pg.display.update()

    # Задержка на 200 миллисекунд
    pg.time.delay(200)

# Завершение Pygame
pg.quit()
sys.exit()


