
import pygame

from Snake import Snake


# Size constants
SCREEN_SIZE = 500
GRID_SIZE = 20


class GUI:
    def __init__(self):
        pygame.init()

        self.__display = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

        pygame.display.update()  # Implement double-buffering, etc.

        self.__clock = pygame.time.Clock()

        # Add game objects
        self.__game_objects = []
        snake = Snake(12, 9, GRID_SIZE, (0, 0, 255))
        self.__game_objects.append(snake)

    def start(self):
        # -- Main Loop --
        while True:
            # Handle events
            for event in pygame.event.get():

                if event.type == pygame.KEYUP:
                    pass

                if event.type == pygame.KEYDOWN:
                    pass

                # Quit event
                if event.type == pygame.QUIT:
                    pygame.quit()

            # Draw all game objects
            for game_object in self.__game_objects:
                game_object.draw(self.__display)

            # Update the display
            pygame.display.update()

            # Delay 60 ms
            self.__clock.tick(60)
