import pygame

from constants import *
from helpers import screen



class Comment:
    def __init__(self, text):
        self.text = text

    def display(self, comment_num):
        comment_font = pygame.font.SysFont("chalkduster.ttf", 15)
        display_to_comment = comment_font.render(self.text, True, BLACK)
        screen.blit(display_to_comment, (FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + comment_num * COMMENT_LINE_HEIGHT))