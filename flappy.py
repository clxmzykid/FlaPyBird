import random
import sys

import pygame
from pygame.locals import *

FPS = 30
SCREENWIDTH = 144
SCREENHEIGHT = 256

# list of players (tuple of 3 positions of flap)
PLAYERS_LIST = (
    # yellow bird
    (
        'assets/sprites/yellowbird-upflap.png',
        'assets/sprites/yellowbird-midflap.png',
        'assets/sprites/yellowbird-downflap.png',
    ),
)

# list of backgrounds
BACKGROUNDS_LIST = (
    'assets/sprites/background_day.png',
    'assets/sprites/background_night.png',
)

# list of pipes
PIPES_LIST = (
    'assets/sprites/pipe-green.png',
)

def main():
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('Flappy Bird')

    # sprites
    bgindex = random.randint(0, len(BACKGROUNDS_LIST) - 1)
    BACKGROUND = pygame.image.load(BACKGROUNDS_LIST[bgindex]).convert()

    playerindex = random.randint(0, len(PLAYERS_LIST) - 1)
    PLAYER = (
        pygame.image.load(PLAYERS_LIST[playerindex][0]).convert_alpha(),
        pygame.image.load(PLAYERS_LIST[playerindex][1]).convert_alpha(),
        pygame.image.load(PLAYERS_LIST[playerindex][2]).convert_alpha(),
    )

    pipeindex = random.randint(0, len(PIPES_LIST) - 1)
    PIPE = pygame.image.load(PIPES_LIST[pipeindex]).convert_alpha()

    NUMBERS = (
        pygame.image.load('assets/sprites/0.png').convert_alpha(),
        pygame.image.load('assets/sprites/1.png').convert_alpha(),
        pygame.image.load('assets/sprites/2.png').convert_alpha(),
        pygame.image.load('assets/sprites/3.png').convert_alpha(),
        pygame.image.load('assets/sprites/4.png').convert_alpha(),
        pygame.image.load('assets/sprites/5.png').convert_alpha(),
        pygame.image.load('assets/sprites/6.png').convert_alpha(),
        pygame.image.load('assets/sprites/7.png').convert_alpha(),
        pygame.image.load('assets/sprites/8.png').convert_alpha(),
        pygame.image.load('assets/sprites/9.png').convert_alpha()
    )

    # sounds
    DIE    = pygame.mixer.Sound('assets/audio/die.ogg')
    HIT    = pygame.mixer.Sound('assets/audio/hit.ogg')
    POINT  = pygame.mixer.Sound('assets/audio/point.ogg')
    SWOOSH = pygame.mixer.Sound('assets/audio/swoosh.ogg')
    WING   = pygame.mixer.Sound('assets/audio/wing.ogg')

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    main()