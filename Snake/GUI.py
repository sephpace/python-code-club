
import pygame


class GUI(pygame.display):
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.set_mode((screen_width, screen_height))

    def start(self):

        # -- Main Loop --
        while True:
            pygame.update()
