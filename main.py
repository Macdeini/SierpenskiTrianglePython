import pygame
import math
import random


def chaos_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    positions = [[100, 900], [900, 900], [500, 100]]
    radius = 1
    colors = ["white", "yellow", "blue", "red", "green", "purple", "orange"]
    pygame.draw.line(screen, colors[0], positions[0], positions[1])
    pygame.draw.line(screen, colors[0], positions[1], positions[2])
    pygame.draw.line(screen, colors[0], positions[2], positions[0])
    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render('Click within the Triangle to start', True, colors[0], (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (200, 100)
    screen.blit(text, textRect)
    pygame.display.update()
    chosen = False
    while not chosen:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                start = [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]]
                chosen = True

    screen.fill("black")
    pygame.draw.circle(screen, colors[0], positions[0], radius)
    pygame.draw.circle(screen, colors[0], positions[1], radius)
    pygame.draw.circle(screen, colors[0], positions[2], radius)
    for _ in range(100000):
        vertex = random.choice(positions)
        start[0] += (vertex[0] - start[0]) / 2
        start[1] += (vertex[1] - start[1]) / 2
        pygame.draw.circle(screen, random.choice(colors), start, radius)
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    chaos_game()
