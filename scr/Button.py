import Colors
import pygame as pg


# Класс для кнопки
class Button:
    def __init__(self, x, y, width, height, text, tooltip="", font_name="Arial", font_size=36):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.tooltip = tooltip  # Подсказка
        self.font = pg.font.Font(pg.font.match_font(font_name), font_size)  # Указываем название шрифта
        self.hovered = False  # Состояние наведения мыши

    def draw(self, surface):
        # Изменяем цвет кнопки при наведении
        color = Colors.grey2 if self.hovered else Colors.grey
        pg.draw.rect(surface, color, self.rect)  # Рисуем кнопку

        # Создаем текст для кнопки
        text_surface = self.font.render(self.text, True, Colors.black)
        text_rect = text_surface.get_rect(center=(self.rect.centerx,
                                                  self.rect.bottom + text_surface.get_height() // 2))  # Центрируем текст под кнопкой
        # Отображаем текст на экране
        surface.blit(text_surface, text_rect)

        # Если кнопка наведена, показываем подсказку
        if self.hovered and self.tooltip:
            tooltip_surface = self.font.render(self.tooltip, True, Colors.black)
            tooltip_rect = tooltip_surface.get_rect(center=(self.rect.centerx,
                                                            self.rect.bottom + tooltip_surface.get_height() // 2 + 20))  # Позиция подсказки под кнопкой
            pg.draw.rect(surface, Colors.grey, tooltip_rect.inflate(10, 10))  # Рисуем фон для подсказки
            surface.blit(tooltip_surface, tooltip_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)  # Проверяем, была ли нажата кнопка

    def update(self, mouse_pos):
        # Обновляем состояние наведения мыши
        self.hovered = self.rect.collidepoint(mouse_pos)

