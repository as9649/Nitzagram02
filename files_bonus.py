from classes.TextPost import *
from classes.ImagePost import *


class files_bonus:

    def save_post(post, post_id, posts_file, comments_file):
        with open(posts_file, "w") as my_file:
            lines = ImagePost.to_list(post)
            my_file.writelines(lines)

    def load_all_posts(posts_file, comments_file):
        with open(posts_file, "r") as my_file:
            list_of_lines = my_file.readlines()

