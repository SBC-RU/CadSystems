import Colors
import pygame as pg
# Класс для кнопки
class Button:
    def __init__(self, x, y, width, height, text, font_name="Arial", font_size=36):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.font = pg.font.Font(pg.font.match_font(font_name), font_size)  # Указываем название шрифта

    def draw(self, surface):
        pg.draw.rect(surface, Colors.grey, self.rect)  # Рисуем кнопку
        # Создаем текст
        text_surface = self.font.render(self.text, True, Colors.black)
        text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.bottom + text_surface.get_height() // 2))  # Центрируем текст под кнопкой
        # Отображаем текст на экране
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)  # Проверяем, была ли нажата кнопка
