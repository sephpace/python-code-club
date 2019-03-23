
import pygame
from Player import Player


UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3


class Menu:
    """
    Basic menu class.
    """
    surface = None
    options = None
    running = True

    def __init__(self, surface):
        """
        Constructor.

        :param surface:  The surface to display the menu on
        """
        pygame.init()

        self.surface = surface
        self.surface.fill((0, 0, 0))
        pygame.display.update()

        self.options = []

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
                    for option in self.options:
                        if option.contains(event.pos):
                            option.set_color((0, 255, 0))
                        else:
                            option.set_color((255, 255, 255))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for option in self.options:
                            if option.contains(event.pos):
                                option.select()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.update()


class MainMenu(Menu):
    """
    The main menu that pops up when the game is first launched and in between rounds
    """
    __players = []
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
        self.__players.append(Player((self.surface.get_width() / 2, self.surface.get_height() / 2), (0, 255, 0), direction=UP, controls='ARROW_KEYS'))
        self.__game_mode = 'singleplayer'
        self.running = False

    def multiplayer(self):
        """
        Logic for when the multiplayer option is selected.
        """
        # TODO: Move this temporary code into the Customization Menu somewhere
        # pygame.joystick.init()
        # joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        # player1 = Player((100, 100), (0, 255, 0), direction=RIGHT, controls='ARROW_KEYS')
        # self.__players.append(player1)
        # player2 = Player((self.surface.get_width - 100, 100), (255, 0, 0), direction=DOWN, controls='WASD')
        # self.__players.append(player2)
        # if len(joysticks) >= 1:
        #     player3 = Player((100, self.surface.get_width - 100), (0, 0, 255), direction=UP, controls='JOYSTICK', joystick=self.__joysticks[0])
        #     self.__players.append(player3)
        # if len(joysticks) >= 2:
        #     player4 = Player((self.surface.get_width - 100, self.surface.get_width - 100), (255, 255, 0), direction=LEFT, controls='JOYSTICK', joystick=self.__joysticks[1])
        #     self.__players.append(player4)
        multiplayer_menu = MultiplayerMenu(self.surface)
        multiplayer_menu.handle()
        self.__players = multiplayer_menu.get_players()
        self.__game_mode = 'multiplayer'
        self.running = False

    def get_players(self):
        """
        :return:  The player data for each player as selected by the user
        """
        return self.__players

    def get_game_mode(self):
        """
        :return:  The game mode selected by the user
        """
        return self.__game_mode


class MultiplayerMenu(Menu):
    """
    The menu that allows selection of the amount of players in the game
    """
    __players = []

    def __init__(self, surface):
        super(MultiplayerMenu, self).__init__(surface)

        # Two players
        option_twoplayer = MenuOption("2 PLAYER", function=self.twoplayer)
        width, height = option_twoplayer.get_size()
        option_twoplayer.set_pos(((self.surface.get_width() // 2) - (width // 2), 185))
        self.options.append(option_twoplayer)

        # Three players
        option_threeplayer = MenuOption("3 PLAYER", function=self.threeplayer)
        width, height = option_threeplayer.get_size()
        option_threeplayer.set_pos(((self.surface.get_width() // 2) - (width // 2), 230))
        self.options.append(option_threeplayer)

        # Four players
        option_fourplayer = MenuOption("4 PLAYER", function=self.fourplayer)
        width, height = option_fourplayer.get_size()
        option_fourplayer.set_pos(((self.surface.get_width() // 2) - (width // 2), 275))
        self.options.append(option_fourplayer)

    def twoplayer(self):
        self.start_customization_menu(2)

    def threeplayer(self):
        self.start_customization_menu(3)

    def fourplayer(self):
        self.start_customization_menu(4)

    def start_customization_menu(self, player_amt):
        customization_menu = CustomizationMenu(self.surface, player_amt)
        customization_menu.handle()
        self.__players = customization_menu.get_players()
        self.running = False

    def get_players(self):
        """
        :return:  The player data for each player as selected by the user
        """
        return self.__players


class CustomizationMenu(Menu):
    """
    Allows players to customize their snake color and set their controls
    """
    def __init__(self, surface, player_count):
        super(CustomizationMenu, self).__init__(surface)

        print(player_count)



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
        self.__function()
