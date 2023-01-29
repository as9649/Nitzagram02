import pygame

from classes.Comment import Comment
from constants import *
from helpers import *


class Post:
    """
    A class used to represent post on Nitzagram
    """
    user_name = "Omer Adam"

    def __init__(self,  location, description):
        # image = pygame.image.load(image_src)
        # image = pygame.transform.scale(image, (POST_WIDTH, POST_HEIGHT))
        # self.image = image
        self.location = location
        self.likes_counter = 0
        self.comments = []
        self.description = description
        self.comments_display_index = 0

    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        self.display_content()
        self.display_header()
        self.display_likes()
        self.display_comments()

    def display_content(self):
        pass

    def display_header(self):
        # User Name  TODO new

        font_username = pygame.font.SysFont('ttf.chalkduster', 16)
        display_to_username = font_username.render(self.user_name, True, (50, 50, 50))
        screen.blit(display_to_username, (USER_NAME_X_POS, USER_NAME_Y_POS))

        # Location

        font_location = pygame.font.SysFont('ttf.chalkduster', UI_FONT_SIZE)
        display_to_location = font_location.render(self.location, True, LIGHT_GRAY)
        screen.blit(display_to_location, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

        # Description

        font_description = pygame.font.SysFont('ttf.chalkduster', UI_FONT_SIZE, bold=True)
        display_to_description = font_description.render(self.description, True, GREY)
        screen.blit(display_to_description, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))

    def display_likes(self):
        font_location = pygame.font.SysFont('ttf.chalkduster', 15)
        display_to_likes = font_location.render("Liked by " + str(self.likes_counter) + " users", True, BLACK)
        screen.blit(display_to_likes, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               int(COMMENT_TEXT_SIZE))
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break

    def add_like(self):
        self.likes_counter += 1

    def add_comment(self, user_comment):
        new_comment = Comment(user_comment)
        self.comments.append(new_comment)

    def view_more_comments(self):
        self.comments_display_index = (self.comments_display_index + 1) % len(self.comments)

    def reset_comments_display_index(self):
        self.comments_display_index = 0