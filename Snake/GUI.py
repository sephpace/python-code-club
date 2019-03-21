
import pygame
from Menu import MainMenu, MultiplayerMenu


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

    def game_over(self, winning_color):
        """Displays the game over screen then goes badk to the title"""
        self.clear()
        color_string = ''
        if winning_color == (255, 0, 0):
            color_string = 'RED'
        elif winning_color == (0, 255, 0):
            color_string = 'GREEN'
        elif winning_color == (0, 0, 255):
            color_string = 'BLUE'
        elif winning_color == (255, 255, 0):
            color_string = 'YELLOW'
        font = pygame.font.SysFont('Verdana', 50)
        game_over_text = font.render(f'{color_string} WINS', False, winning_color)
        text_width, text_height = font.size(f'{color_string} WINS')
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
        main_menu = MainMenu(self.__screen)
        main_menu.handle()
        # # Draw the title
        # font = pygame.font.SysFont('Verdana', 80)
        # title = font.render("Snake", False, (0, 255, 0))
        # font = pygame.font.SysFont('Verdana', 30)
        # subtitle = font.render("Press enter to start", False, (255, 255, 255))
        # pygame.Surface.blit(self.__screen, title, (120, 150))
        # pygame.Surface.blit(self.__screen, subtitle, (100, 240))
        #
        # # Update the display
        # self.update()
        #
        # # Event loop
        # draw_menu = True
        # while draw_menu:
        #
        #     # Event handler
        #     for event in pygame.event.get():
        #         # Key events
        #         if event.type == pygame.KEYDOWN:
        #             key = event.key
        #             if key == pygame.K_RETURN:
        #                 draw_menu = False
        #         # Quit event
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             exit()

        # Clear the menu from the screen
        self.clear()
        self.update()

    def update(self):
        """Updates the display"""
        pygame.display.update()

