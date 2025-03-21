# navigation.py
import pygame

def handle_navigation(selected_index, keys, button_count):
    """
    Обрабатывает нажатия клавиш для навигации между кнопками.
    Возвращает новый индекс выбранной кнопки.
    """
    if keys[pygame.K_UP]:  # Перемещение вверх
        selected_index = (selected_index - 1) % button_count
    if keys[pygame.K_DOWN]:  # Перемещение вниз
        selected_index = (selected_index + 1) % button_count
    return selected_index

def update_button_states(buttons, selected_index, mouse_pos):
    """
    Обновляет состояние кнопок (is_hovered) в зависимости от выбора клавиатуры и наведения мыши.
    """
    for i, button in enumerate(buttons):
        # Если кнопка выбрана с помощью клавиатуры, меняем её состояние
        if i == selected_index:
            button.is_hovered = True
        else:
            button.is_hovered = button.rect.collidepoint(mouse_pos)  # Состояние hover только при наведении мыши

def handle_keydown_event(event, buttons, selected_index):
    """
    Обрабатывает событие KEYDOWN для активации кнопки (например, нажатие Enter).
    """
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:  # Клавиша Enter
            buttons[selected_index].is_hovered = True
            # Эмулируем нажатие кнопки
            if buttons[selected_index].sound:
                buttons[selected_index].sound.play()
            # Отправляем событие нажатия кнопки
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=buttons[selected_index]))