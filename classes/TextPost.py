from classes.Post import *


class TextPost(Post):

    def __init__(self, location, description, background_color, text, text_color):
        Post.__init__(self, location, description)
        self.background_color = background_color
        self.text_color = text_color
        self.text_array = from_text_to_array(text)

    def display_content(self):
        pygame.draw.rect(screen, self.background_color, pygame.Rect(
            POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT))
        font_text = pygame.font.SysFont('ttf.chalkduster', TEXT_POST_FONT_SIZE, bold=True)
        for i in range(len(self.text_array)):
            display_to_text = font_text.render(self.text_array[i], True, self.text_color)
            text_loc = center_text(len(self.text_array), display_to_text, i)
            screen.blit(display_to_text, text_loc)
