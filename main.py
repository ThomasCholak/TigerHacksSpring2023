# Thomas Cholak
# 2023 Pickhacks Rolla S&T

# Used code from https://www.youtube.com/watch?v=jO6qQDNa2UY&t=1156s
# Also used some code from: https://www.youtube.com/watch?v=93Ao51_2MF0

import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Sets width and height of game screen

FPS = 60  # locks FPS at 60 frames per second
BACKGROUND_IMAGE = pygame.image.load(
    os.path.join('Assets', 'background.jpg'))
BANANA_ANIMATION = [pygame.image.load(
    os.path.join('Assets', 'banana1.png')),
                pygame.image.load(os.path.join('Assets', 'banana2.png')),
                pygame.image.load(os.path.join('Assets', 'banana3.png')),
                pygame.image.load(os.path.join('Assets', 'banana4.png')),
                pygame.image.load(os.path.join('Assets', 'banana5.png')),
                pygame.image.load(os.path.join('Assets', 'banana6.png')),
                pygame.image.load(os.path.join('Assets', 'banana7.png')),
                pygame.image.load(os.path.join('Assets', 'banana8.png')),
                pygame.image.load(os.path.join('Assets', 'banana9.png')),
                pygame.image.load(os.path.join('Assets', 'banana10.png')),
                pygame.image.load(os.path.join('Assets', 'banana11.png')),
                pygame.image.load(os.path.join('Assets', 'banana12.png')),
                pygame.image.load(os.path.join('Assets', 'banana13.png')),
                pygame.image.load(os.path.join('Assets', 'banana14.png')),
                pygame.image.load(os.path.join('Assets', 'banana15.png'))]


def main():

    clock = pygame.time.Clock()
    run = True
    bgx = 0
    value = 0

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if value >= len(BANANA_ANIMATION):
            value = 0

        player = pygame.transform.rotozoom(BANANA_ANIMATION[value], 0, 1)
        WIN.blit(BACKGROUND_IMAGE, (bgx - 900, 0))
        WIN.blit(BACKGROUND_IMAGE, (bgx, 0))
        WIN.blit(BACKGROUND_IMAGE, (bgx + 900, 0))
        bgx = bgx - 1
        if bgx <= -900:
            bgx = 0

        WIN.blit(player, (50, 237))
        value += 1
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
