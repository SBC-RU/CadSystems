import pygame as pg
from scr import Colors
from scr.interface_elements.Button import Button


# Дочерний класс для поля ввода значений
class InputField(Button):
    def __init__(self, x, y, width, height, tooltip="", font_name="Arial", font_size=36):
        super().__init__(x, y, width, height, "", tooltip, font_name, font_size)  # Вызываем конструктор родительского класса
        self.text = ""  # Изначально текст пустой
        self.active = False  # Состояние активности поля ввода

    def draw(self, surface):
        super().draw(surface)  # Рисуем кнопку (или поле ввода)

        # Рисуем текстовое поле с введенным текстом
        text_surface = self.font.render(self.text, True, Colors.black)
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + (self.rect.height - text_surface.get_height()) // 2))

    def is_clicked(self, pos):
        if super().is_clicked(pos):  # Проверяем нажатие как у кнопки
            self.active = not self.active  # Переключаем активность поля ввода
        else:
            self.active = False  # Деактивируем поле ввода при клике вне его

    def update(self, mouse_pos):
        super().update(mouse_pos)  # Обновляем состояние наведения мыши

    def handle_event(self, event):
        if self.active:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    print(f'Введенное значение: {self.text}')  # Можно добавить обработку значения
                    self.text = ''  # Очистить поле после нажатия Enter
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]  # Удаление последнего символа
                else:
                    if event.unicode.isprintable():  # Проверяем на возможность ввода символа
                        self.text += event.unicode  # Добавляем символ в текст