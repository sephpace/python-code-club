
import pygame


class GUI:
    SCREEN_SIZE = 500
    GRID_SIZE = SCREEN_SIZE / 100

    def __init__(self):
        pygame.init()
        self.__display = pygame.display.set_mode((self.SCREEN_SIZE, self.SCREEN_SIZE))

        pygame.display.update()  # Implement double-buffering, etc.

        self.__clock = pygame.time.Clock()

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
