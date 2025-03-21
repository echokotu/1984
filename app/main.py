import pygame
import sys
from app.src.components.button import ImageButton

pygame.init()

WIDTH, HEIGTH = 320, 480

screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("1984 BETA")
rect = pygame.Rect(40, 40, 120, 120)


#beta_button = ImageButton(WIDTH/2-(252/2), 100, 252, 74 , "", "Key.png", "Key_hover.png", "dydy.mp3.mp3")
#beta_button2 = ImageButton(WIDTH/2-(252/2), 200, 252, 74 , "", "Key.png", "Key_hover.png", "netak-—-сделано-в-Clipchamp_1.mp3")

beta_button = ImageButton(WIDTH / 2 - (280/2), 50, 150, 50, "", "assets/images/Key.png",
                          "app/assets/images/Key_hover.png",
                          "app/assets/sounds/dydy.mp3.mp3")
beta_button2 = ImageButton(WIDTH / 2 - (280/2), 110, 150, 50, "", "assets/images/Key.png",
                           "app/assets/images/Key_hover.png", "app/assets/video/netak-—-сделано-в-Clipchamp_1.mp3")




def main_menu():
    running = True
    while running:
        screen.fill((94, 139, 107)) #Цвет рабочего окна

        ##Линии на рабочей области

        # (Правая линия)
        window_rect = pygame.Rect(200, 10, 5, 460)  # (x, y, ширина, высота)
        pygame.draw.rect(screen, (0, 0, 0), window_rect)  # Цвет окна

        # (Вверхняя линия)
        window_rect = pygame.Rect(0, 10, 200, 4)  # (x, y, ширина, высота)
        pygame.draw.rect(screen, (0, 0, 0), window_rect)  # Цвет окна

        # (Нижняя линия)
        window_rect = pygame.Rect(0, 466, 200, 4)  # (x, y, ширина, высота)
        pygame.draw.rect(screen, (0, 0, 0), window_rect)  # Цвет окна

        ##end


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()


            #beta_button.handline_event(event) #Выключил звук
            #beta_button2.handline_event(event)

        beta_button.check_hower(pygame.mouse.get_pos())
        beta_button.draw(screen)

        beta_button2.check_hower(pygame.mouse.get_pos())
        beta_button2.draw(screen)

        pygame.display.flip()

main_menu()
