import pygame
from helpers import screen
from constants import *


class Filter:
    def __init__(self, color, alpha):
        self.color = color
        self.alpha = alpha

    def apply_filter(self):
        square = pygame.Surface((POST_WIDTH, POST_HEIGHT))
        square.set_alpha(self.alpha, 0)
        square.fill(self.color)
        screen.blit(square, (POST_X_POS, POST_Y_POS))

