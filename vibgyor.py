import pygame
from pygame.locals import *

pygame.init()


try:
    W = int(input("Width (natural no.): "))
    H = int(input("Height (natural no.): "))

    print("Type any V , I , B , G , O , R  to see effect ")

    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("VIBGYOR")
    background = (200, 00, 00)
except:
    print("INVALID INPUT")

color_dict = {
    K_v: (140, 0, 211),  # violet
    K_i: (75, 0, 130),  # indigo
    K_b: (0, 0, 255),  # blue
    K_g: (0, 255, 0),  # gr̥̥een
    K_y: (255, 255, 0),  # yellow
    K_o: (255, 127, 0),  # orange
    K_r: (255, 0, 0),  # red
}
# print(color_dict)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key in color_dict:
                background = color_dict[event.key]
                screen.fill(background)
                pygame.display.set_caption("background = " + str(background))
                pygame.display.update()

pygame.quit()
