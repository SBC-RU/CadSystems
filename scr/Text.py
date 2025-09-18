import Colors
import pygame as pg

# Класс для текста
class Text:
    def __init__(self, x, y, text, color=(0, 0, 0), font_name="Arial", font_size=36):
        self.rect = pg.Rect(x, y, 0, 0)  # Укажите ширину и высоту для rect
        self.text = text
        self.color = color  # Добавлен параметр цвета
        self.font = pg.font.Font(pg.font.match_font(font_name), font_size)

    def draw(self, surface):
        # Создаем текст
        text_surface = self.font.render(self.text, True, self.color)
        # Получаем прямоугольник текста для правильного позиционирования
        text_rect = text_surface.get_rect(topleft=(self.rect.x, self.rect.y))
        # Отображаем текст на экране
        surface.blit(text_surface, text_rect)
