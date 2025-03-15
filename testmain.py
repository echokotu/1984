# main.py
import pygame
import sys
from button import ImageButton
from navigation import handle_navigation, update_button_states, handle_keydown_event  # Импортируем функции навигации

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 320, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1984 BETA")

# Создание кнопок
beta_button = ImageButton(WIDTH / 2 - (280 / 2), 50, 150, 50, "", "Key.png", "Key_hover.png", "dydy.mp3.mp3")
beta_button2 = ImageButton(WIDTH / 2 - (280 / 2), 110, 150, 50, "", "Key.png", "Key_hover.png", "netak-—-сделано-в-Clipchamp_1.mp3")

# Список кнопок для навигации
buttons = [beta_button, beta_button2]
selected_index = 0  # Индекс выбранной кнопки

# Основное меню
def main_menu():
    global selected_index

    running = True
    while running:
        screen.fill((94, 139, 107))  # Цвет рабочего окна

        # Рисуем линии на рабочей области
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(200, 10, 5, 460))  # Правая линия
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 10, 200, 4))  # Верхняя линия
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 466, 200, 4))  # Нижняя линия

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            # Обработка нажатий клавиш
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                selected_index = handle_navigation(selected_index, keys, len(buttons))
                handle_keydown_event(event, buttons, selected_index)  # Обработка нажатия Enter

            # Обработка нажатий мыши
            for button in buttons:
                button.check_hower(pygame.mouse.get_pos())
                button.handline_event(event)

        # Обновление состояния кнопок
        update_button_states(buttons, selected_index, pygame.mouse.get_pos())

        # Отрисовка кнопок
        for button in buttons:
            button.draw(screen)

        pygame.display.flip()

# Запуск меню
main_menu()