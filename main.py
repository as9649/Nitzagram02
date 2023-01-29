import os

from buttons import like_button, comment_button, click_post_button, view_more_comments_button
from classes.Filter import *
from classes.ImagePost import ImagePost
from classes.TextPost import TextPost
from classes.Post import *

import pygame

from constants import BLACK, WINDOW_WIDTH, WINDOW_HEIGHT
from helpers import screen


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))
    purple_filter = Filter((30, 12, 121), 80)

    post_omer = ImagePost("Images/omer_adam.png", "Israel", "Check out my new NFT")
    post_noa = ImagePost("Images/noa_kirel.jpg", "Israel", "Check out my new NFT", purple_filter)
    post_ronaldo = ImagePost("Images/ronaldo.jpg", "Israel", "Check out my new NFT", purple_filter)
    text_post = TextPost("Israel", "How cool is text post",
                         (71, 144, 205), "This is Text Post on Nitzagram!!", (216, 79, 81))
    posts_list = [post_omer, post_noa, post_ronaldo, text_post]
    current_post_index = 0
    current_post = posts_list[current_post_index]

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if mouse_in_button(like_button, mouse_pos):
                    current_post.add_like()
                elif mouse_in_button(comment_button, mouse_pos):
                    user_comment = read_comment_from_user()
                    current_post.add_comment(user_comment)
                elif mouse_in_button(click_post_button, mouse_pos):
                    current_post_index = (current_post_index + 1) % len(posts_list)
                    current_post = posts_list[current_post_index]
                    current_post.reset_comments_display_index()
                elif mouse_in_button(view_more_comments_button, mouse_pos):
                    current_post.view_more_comments()

        # Display the background, presented Image, likes, comments, tags and
        # location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        current_post.display()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(60)
    pygame.quit()
    quit()


main()
