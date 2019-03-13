
import pygame
from Player import Player


class GUI:
    """Handles all of the graphical elements of the game"""

    # Member variables
    __screen = None  # The Pygame display window
    __size = 0       # The size of the screen

    def __init__(self, size):
        """Constructor"""
        # Setup the screen
        pygame.init()
        pygame.font.init()
        self.__screen = pygame.display.set_mode((size, size))
        self.__size = size

    def clear(self):
        """Sets the screen's color to black"""
        self.__screen.fill((0, 0, 0))

    def draw(self, objects):
        """Draws all of the given objects to the screen"""
        for obj in objects:
            obj.draw(self.__screen)

    def game_over(self):
        """Displays the game over screen then goes badk to the title"""
        self.clear()
        font = pygame.font.SysFont('Verdana', 50)
        game_over_text = font.render("Game Over", False, (255, 255, 255))
        pygame.Surface.blit(self.__screen, game_over_text, (100, 170))
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

    def customization_menu(self):
        """Displays the customization menu"""
        # Set up the menu options
        font = pygame.font.SysFont('Verdana', 30)

        # The name of the player
        name = ""
        max_letter_amount = 15

        # Event loop
        draw_menu = True
        while draw_menu:
            # Clear the display
            self.clear()

            # Draw the menu
            text_width, text_height = font.size("Player Name")
            pygame.Surface.blit(self.__screen, font.render("Player Name", False, (255, 255, 255)), ((self.__size // 2) - (text_width // 2), (self.__size // 2) - text_height))
            text_width, text_height = font.size(name)
            pygame.Surface.blit(self.__screen, font.render(name, False, (255, 255, 255)), ((self.__size // 2) - (text_width // 2), (self.__size // 2) + text_height))

            # Update the display
            self.update()

            # Event handler
            for event in pygame.event.get():
                # Key events
                if event.type == pygame.KEYDOWN:
                    key = event.key

                    # Print the letters of the name
                    # Regular lower-cased letters
                    if pygame.K_a <= key <= pygame.K_z:
                        if len(name) < max_letter_amount:
                            name += pygame.key.name(key)
                    # Spaces
                    if key == pygame.K_SPACE:
                        if len(name) < max_letter_amount:
                            name += " "

                    # Allow backspacing
                    if key == pygame.K_BACKSPACE:
                        name = name[:-1]

                    # Join or host the game
                    if key == pygame.K_RETURN:
                        draw_menu = False

                # Quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        # Clear the menu from the screen
        self.clear()
        self.update()
        return name

    def main_menu(self):
        """Displays the game title and menu"""
        # Draw the title
        font = pygame.font.SysFont('Verdana', 80)
        title = font.render("Snake", False, (0, 255, 0))
        text_width, text_height = font.size("Snake")
        pygame.Surface.blit(self.__screen, title, ((self.__size // 2) - (text_width // 2), 200 - text_height))

        # Set up the menu options
        font = pygame.font.SysFont('Verdana', 30)
        options = ["Single Player", "Multiplayer Host", "Multiplayer Join"]
        selected = 0

        # Event loop
        draw_menu = True
        while draw_menu:
            # Draw the menu options
            for i in range(len(options)):
                color = (255, 255, 255)
                if i == selected:
                    color = (0, 0, 255)
                text_width, text_height = font.size(options[i])
                pygame.Surface.blit(self.__screen, font.render(options[i], False, color), ((self.__size // 2) - (text_width // 2), 250 + (i * (text_height + 10))))

            # Update the display
            self.update()

            # Event handler
            for event in pygame.event.get():
                # Key events
                if event.type == pygame.KEYDOWN:
                    key = event.key
                    # Select the current option
                    if key == pygame.K_RETURN or key == pygame.K_SPACE:
                        draw_menu = False

                    # Select different options
                    if key == pygame.K_UP:
                        if selected > 0:
                            selected -= 1
                    if key == pygame.K_DOWN:
                        if selected < len(options) - 1:
                            selected += 1

                # Quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        # Clear the menu from the screen
        self.clear()
        self.update()
        return selected

    def multiplayer_menu(self, game_mode, client_name):
        players = []

        draw_menu = True

        if game_mode == 1:  # Hosting (Master)
            # TODO: Add the first player to the game
            pass
        elif game_mode == 2:  # Joining (Slave)
            pass

        # TODO: Get the playerdata from the server

        while draw_menu:
            pass

    def update(self):
        """Updates the display"""
        pygame.display.update()

