import pygame

from pygame.locals import (
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
    K_6,
    K_7,
    K_8,
    K_9,
    K_ESCAPE,
    K_RETURN,
    KEYDOWN,
    QUIT,
)

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True
while running:

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        if event.type == pygame.QUIT:
            running = False

    screen.fill((15, 15, 15))

    pygame.display.flip()

pygame.quit()
