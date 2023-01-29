from classes.Post import *
from classes.Filter import *


class ImagePost(Post):

    def __init__(self, image_src, location, description, filter=None):
        image = pygame.image.load(image_src)
        image = pygame.transform.scale(image, (POST_WIDTH, POST_HEIGHT))
        self.filter = filter
        Post.__init__(self, location, description)
        self.image = image

    def display_content(self):
        screen.blit(self.image, (POST_X_POS, POST_Y_POS))
        if self.filter is not None:
            Filter.apply_filter(self.filter)
