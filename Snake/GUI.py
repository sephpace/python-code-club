
import pygame
import time
from Menu import MainMenu


class GUI:
    """
    Handles all of the graphical elements of the game.
    """
    # Member variables
    __screen = None  # The Pygame display window
    __size = 0       # The size of the screen

    def __init__(self, size):
        """
        Constructor.

        :param size:  The size of both sides of the screen
        """
        # Setup the screen
        pygame.init()
        pygame.font.init()
        self.__screen = pygame.display.set_mode((size, size))
        self.__size = size

    def clear(self):
        """
        Clears everything from teh screen and sets the color to black.
        """
        self.__screen.fill((0, 0, 0))

    def draw(self, objects):
        """
        Draws all of the given objects onto the screen.

        :param objects:  The objects to draw onto the screen.  Can be a single object or a list of objects
        """
        try:
            for obj in objects:
                obj.draw(self.__screen)
        except TypeError:
            objects.draw(self.__screen)

    def count_down(self, seconds=3):
        """
        Shows a count down timer for the given amount of seconds.

        :param time:  The amount of time to count down from in seconds
        """

        font = pygame.font.SysFont('Verdana', 40)

        stop_time = time.time() + seconds + 1

        # Handle quit event and delay for a little bit
        while True:
            # Event handler
            for event in pygame.event.get():
                # Quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            seconds_left = stop_time - time.time()

            if seconds_left >= 1:
                number = font.render(str(int(seconds_left)), False, (255, 255, 255))
            elif 0 < seconds_left < 1:
                number = font.render('Start!', False, (255, 255, 255))
            else:
                break

            pygame.draw.rect(self.__screen, (0, 0, 0), ((self.__screen.get_width() // 2) - (number.get_width() // 2), (self.__screen.get_height() // 2) - (number.get_height() // 2), number.get_width(), number.get_height()))
            pygame.Surface.blit(self.__screen, number, ((self.__screen.get_width() // 2) - (number.get_width() // 2), (self.__screen.get_height() // 2) - (number.get_height() // 2)))
            self.update()

        # Update the screen
        self.update()

    def game_over(self, winning_player_name, winning_color, game_mode):
        """
        Displays the game over screen.

        :param winning_player_name:  The name of the player who won the game
        :param winning_color:        The color of the player who won the game
        :param game_mode:            The game mode of that game that is being ended
        """
        # Create the font object
        font = pygame.font.SysFont('Verdana', 50)

        # Figure out the game mode and display the game over message
        if game_mode == 'singleplayer':
            game_over_text = font.render('GAME OVER', False, winning_color)
            text_width, text_height = font.size('GAME OVER')
            pygame.draw.rect(self.__screen, (0, 0, 0), ((self.__screen.get_width() // 2) - (text_width // 2), (self.__screen.get_height() // 2) - (text_height // 2) - 50, text_width, text_height))
            pygame.Surface.blit(self.__screen, game_over_text, ((self.__screen.get_width() // 2) - (text_width // 2), (self.__screen.get_height() // 2) - (text_height // 2) - 50))
        elif game_mode == 'multiplayer':
            game_over_text = font.render(winning_player_name+ ' WINS', False, winning_color)
            text_width, text_height = font.size(winning_player_name + ' WINS')
            pygame.draw.rect(self.__screen, (0, 0, 0), ((self.__screen.get_width() // 2) - (text_width // 2), (self.__screen.get_height() // 2) - (text_height // 2) - 50, text_width, text_height))
            pygame.Surface.blit(self.__screen, game_over_text, ((self.__screen.get_width() // 2) - (text_width // 2), (self.__screen.get_height() // 2) - (text_height // 2) - 50))

        # Update the screen
        self.update()

        # Delay the screen for about 2 seconds
        milliseconds = 0  # The amt of milliseconds delayed

        while True:
            # Event handler
            for event in pygame.event.get():

                # Quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Increase the amount of milliseconds passed
            milliseconds += pygame.time.delay(1)

            # Stop delaying it once the desired value is reached
            if milliseconds >= 2000:
                break

        # Clear and update the screen
        self.clear()
        self.update()

    def show_menu(self):
        """
        Displays the game title and menu.
        """
        # Start the menu(s)
        menu = MainMenu(self, self.__screen)
        menu.handle()

        # Clear the menu from the screen and update it
        self.clear()
        self.update()

    @staticmethod
    def update():
        """
        Updates the display.
        """
        pygame.display.update()
