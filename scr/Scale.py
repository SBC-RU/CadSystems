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
    keys = pg.key.get_pressed()
    if keys[pg.K_PLUS] or keys[pg.K_EQUALS]:
        update_scale(0.1)
    if keys[pg.K_MINUS] or keys[pg.K_UNDERSCORE]:
        update_scale(-0.1)