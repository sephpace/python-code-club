
import pygame
from Menu import MainMenu


class GUI:
    """Handles all of the graphical elements of the game"""

    # Member variables
    __screen = None  # The Pygame display window

    def __init__(self, size):
        """Constructor"""
        # Setup the screen
        pygame.init()
        pygame.font.init()
        self.__screen = pygame.display.set_mode((size, size))

    def clear(self):
        """Sets the screen's color to black"""
        self.__screen.fill((0, 0, 0))

    def draw(self, objects):
        """Draws all of the given objects to the screen"""
        try:
            for obj in objects:
                obj.draw(self.__screen)
        except TypeError:
            objects.draw(self.__screen)

    def game_over(self, winning_player_name, winning_color, game_mode):
        """Displays the game over screen then goes back to the title"""
        self.clear()

        font = pygame.font.SysFont('Verdana', 50)
        if game_mode == 'singleplayer':
            game_over_text = font.render('GAME OVER', False, winning_color)
            text_width, text_height = font.size('GAME OVER')
            pygame.Surface.blit(self.__screen, game_over_text, ((self.__screen.get_width() // 2) - (text_width // 2), (self.__screen.get_height() // 2) - (text_height // 2) - 50))
        elif game_mode == 'multiplayer':
            game_over_text = font.render(f'{winning_player_name} WINS', False, winning_color)
            text_width, text_height = font.size(f'{winning_player_name} WINS')
            pygame.Surface.blit(self.__screen, game_over_text, ((self.__screen.get_width() // 2) - (text_width // 2), (self.__screen.get_height() // 2) - (text_height // 2) - 50))
        self.update()

        milliseconds = 0  # The amt of milliseconds delayed

        # Handle quit event and delay for a little bit
        while True:
            # Event handler
            for event in pygame.event.get():
                # Quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            milliseconds += pygame.time.delay(1)

            if milliseconds >= 2000:
                break

        # Clear the screen
        self.clear()
        self.update()

    def show_menu(self):
        """Displays the game title and menu"""
        # Start the menu(s)
        menu = MainMenu(self, self.__screen)
        menu.handle()

        # Clear the menu from the screen
        self.clear()
        self.update()

    def update(self):
        """Updates the display"""
        pygame.display.update()

