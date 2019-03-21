
import pygame


class Menu:
    """
    Basic menu class.
    """
    surface = None
    options = []
    running = True

    def __init__(self, surface, options=None):
        """
        Constructor.

        :param surface:  The surface to display the menu on
        """
        pygame.init()

        self.surface = surface

        if options is not None:
            options = options

    def handle(self):
        """
        Display all of the options on the surface
        """
        while self.running:
            for option in self.options:
                option.draw(self.surface)

                # Events
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        if option.contains(event.pos):
                            option.set_color((0, 255, 0))
                        else:
                            option.set_color((255, 255, 255))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if option.contains(event.pos):
                                option.select()
                            else:
                                option.select()

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

            pygame.display.update()


class MainMenu(Menu):
    """
    The main menu that pops up when the game is first launched and in between rounds
    """
    __game_mode = None

    def __init__(self, surface):
        """
        Constructor.

        :param surface:  The surface to display the menu on
        """
        super(MainMenu, self).__init__(surface)

        # Draw the title
        pygame.font.init()
        title_font = pygame.font.SysFont('Verdana', 80)
        title = title_font.render('Snake', False, (0, 255, 0))
        width, height = title_font.size('Snake')
        pygame.Surface.blit(self.surface, title, ((self.surface.get_width() // 2) - (width // 2), 120))

        # Set up the menu options
        option_singleplayer = MenuOption('Singleplayer', function=self.singleplayer)
        width, height = option_singleplayer.get_size()
        option_singleplayer.set_pos(((self.surface.get_width() // 2) - (width // 2), 230))
        self.options.append(option_singleplayer)

        option_multiplayer = MenuOption('Multiplayer', function=self.multiplayer)
        width, height = option_multiplayer.get_size()
        option_multiplayer.set_pos(((self.surface.get_width() // 2) - (width // 2), 275))
        self.options.append(option_multiplayer)

    def singleplayer(self):
        """
        Logic for when the singleplayer option is selected.
        """
        self.__game_mode = 'singleplayer'
        self.running = False

    def multiplayer(self):
        """
        Logic for when the multiplayer option is selected.
        """
        self.__game_mode = 'multiplayer'
        # TODO: Start the multiplayer menu
        self.running = False

    def get_game_mode(self):
        """
        :return:  The user-selected game mode (either singleplayer or multiplayer)
        """
        return self.__game_mode


class MultiplayerMenu(Menu):
    """
    The multiplayer menu that pops up when 'Multiplayer' is selected on the main menu
    """
    def __init__(self, surface):
        super(MultiplayerMenu, self).__init__(surface)

    def handle(self):
        pass


class MenuOption:
    """
    An selectable option from the menu
    """
    __text = ''
    __pos = ()
    __option_font = None
    __function = None
    __size = ()
    __surface = None

    def __init__(self, text, pos=None, option_font=None, function=None):
        """
        Constructor.

        :param text:         The text displayed for the menu option
        :param pos:          The position of the menu option on the screen as a tuple of x and y
        :param option_font:  The pygame font object for the menu option
        """
        self.__text = text
        self.__pos = pos
        if option_font is not None:
            self.__option_font = option_font
        else:
            self.__option_font = pygame.font.SysFont('Verdana', 30)
        self.__function = function
        self.__size = self.__option_font.size(text)
        self.__surface = self.__option_font.render(text, False, (255, 255, 255))

    def set_color(self, color):
        self.__surface = self.__option_font.render(self.__text, False, color)

    def draw(self, surface):
        x, y = self.__pos
        pygame.Surface.blit(surface, self.__surface, (x, y))

    def get_pos(self):
        """
        :return:  The position of the menu option
        """
        return self.__pos

    def get_size(self):
        """
        :return:  The size of the menu option
        """
        return self.__size

    def set_pos(self, pos):
        """
        :param pos:  The new position
        """
        self.__pos = pos

    def contains(self, point):
        """
        Returns True if the given point lies within the bounds of the option.

        :param point:  The point that is potentially contained
        :return:       True if the point is within the bounds of the option and False otherwise
        """
        x, y = point
        option_x, option_y = self.__pos
        option_width, option_height = self.__size
        if option_x <= x <= option_x + option_width and option_y <= y <= option_y + option_height:
            return True
        return False

    def select(self):
        """Runs the function associated with this menu option"""
        try:
            self.__function()
        except TypeError:
            print(f"There is no function associated with menu option {self.__text}")
