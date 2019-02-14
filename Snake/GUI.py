
import pygame

from Snake import Snake


class GUI:
    # Size constants
    SCREEN_SIZE = 500
    GRID_SIZE = 20

    def __init__(self):
        pygame.init()

        self.__display = pygame.display.set_mode((self.SCREEN_SIZE, self.SCREEN_SIZE))

        pygame.display.update()  # Implement double-buffering, etc.

        self.__clock = pygame.time.Clock()

        # Add game objects
        self.__game_objects = []
        self.__game_objects.append(Snake(12, 9, (0, 0, 255)))

    def start(self):
        # -- Main Loop --
        while True:
            for event in pygame.event.get():

                if event.type == pygame.KEYUP:
                    pass

                if event.type == pygame.KEYDOWN:
                    pass

                # Quit event
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()

            self.__clock.tick(60)
