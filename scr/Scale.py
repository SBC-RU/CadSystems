import pygame as pg

# Инициализация Pygame
pg.init()

# Начальное значение scale
value = 1.0

def update_scale(increment):
    """Обновить значение scale с учетом ограничений."""
    global value
    value += increment
    # Округление до одного знака после запятой
    value = round(value, 1)
    # Ограничения для scale
    if value < 0.1:
        value = 0.1
    elif value > 2.1:
        value = 2.1
    return value

def action(event):
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 4:  # Прокрутка вверх (колесо вверх)
            update_scale(0.1)
        elif event.button == 5:  # Прокрутка вниз (колесо вниз)
            update_scale(-0.1)