
import pygame
from Player import Player
from GameLoop import GameLoop


UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3


class Menu:
    """
    Basic menu class.
    """
    gui = None
    surface = None
    options = None
    running = True

    def __init__(self, gui, surface):
        """
        Constructor.

        :param surface:  The surface to display the menu on
        """
        pygame.init()

        self.gui = gui
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
                        if type(option) != ArrowBar:
                            if option.contains(event.pos):
                                option.set_color((0, 255, 0))
                            else:
                                option.set_color((255, 255, 255))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for option in self.options:
                            if type(option) != ArrowBar:
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

    def __init__(self, gui, surface):
        """
        Constructor.

        :param surface:  The surface to display the menu on
        """
        super(MainMenu, self).__init__(gui, surface)

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
        customization_menu = CustomizationMenu(self.gui, self.surface, 1)
        customization_menu.handle()

        # Reset surface (only runs when the user hits 'back' on the following menu
        self.surface.fill((0, 0, 0))
        self.__init__(self.gui, self.surface)

    def multiplayer(self):
        """
        Logic for when the multiplayer option is selected.
        """
        multiplayer_menu = MultiplayerMenu(self.gui, self.surface)
        multiplayer_menu.handle()

        # Reset surface (only runs when the user hits 'back' on the following menu
        self.surface.fill((0, 0, 0))
        self.__init__(self.gui, self.surface)


class MultiplayerMenu(Menu):
    """
    The menu that allows selection of the amount of players in the game
    """
    def __init__(self, gui, surface):
        super(MultiplayerMenu, self).__init__(gui, surface)

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

        # Add the back option
        option_back = MenuOption("BACK", (10, 450), function=self.back)
        self.options.append(option_back)

    def twoplayer(self):
        self.start_customization_menu(2)

    def threeplayer(self):
        self.start_customization_menu(3)

    def fourplayer(self):
        self.start_customization_menu(4)

    def start_customization_menu(self, player_amt):
        customization_menu = CustomizationMenu(self.gui, self.surface, player_amt)
        customization_menu.handle()

        # Reset surface (only runs when the user hits 'back' on the following menu
        self.surface.fill((0, 0, 0))
        self.__init__(self.gui, self.surface)

    def back(self):
        """
        Displays the previous menu.
        """
        self.running = False


class CustomizationMenu(Menu):
    """
    Allows players to customize their snake color and set their controls
    """
    __players = None
    __player_count = None
    __joysticks = None
    __colors = None
    __color_surfaces = None
    __controls = None
    __control_surfaces = None
    __color_bars = None
    __control_bars = None

    def __init__(self, gui, surface, player_count):
        super(CustomizationMenu, self).__init__(gui, surface)

        self.__players = []
        self.__player_count = player_count

        self.__joysticks = []

        self.__colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128), (255, 20, 147)]
        self.__color_surfaces = {}
        self.__controls = ['ARROW_KEYS', 'WASD']
        self.__control_surfaces = {}

        self.__color_bars = []
        self.__control_bars = []

        # Populate color_surfaces
        for color in self.__colors:
            color_surface = pygame.Surface((60, 40))
            pygame.draw.rect(color_surface, color, (0, 0, color_surface.get_width(), color_surface.get_height()))
            self.__color_surfaces[color] = color_surface

        # Setup joysticks
        pygame.joystick.init()
        self.__joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

        # Populate control_surfaces
        self.__control_surfaces['ARROW_KEYS'] = pygame.image.load('arrowkeys.png')
        self.__control_surfaces['WASD'] = pygame.image.load('wasd.png')
        for joystick in self.__joysticks:
            controller_image = pygame.image.load('controller.png')
            font = pygame.font.SysFont('Verdana', 20)
            controller_number = font.render(str(joystick.get_id() + 1), False, (255, 255, 255))
            pygame.Surface.blit(controller_image, controller_number, (23, 3))
            self.__control_surfaces[f'JOYSTICK{joystick.get_id()}'] = controller_image
            self.__controls.append(f'JOYSTICK{joystick.get_id()}')

        font = pygame.font.SysFont('Verdana', 40)
        for i in range(player_count):
            # Add the player name for each player
            width, height = font.size(f'Player {i + 1}')
            player_name = font.render(f'Player {i + 1}', False, (255, 255, 255))
            draw_x = 10
            draw_y = (self.surface.get_height() // 2) - (height * player_count) + (height * i) + 50
            pygame.Surface.blit(self.surface, player_name, (draw_x, draw_y))

            # Add the color bar for each player
            color_bar = ArrowBar((draw_x + width + 10, draw_y), self.__colors, self.__color_surfaces)
            self.options.append(color_bar)
            for arrow in color_bar.get_arrows():
                self.options.append(arrow)
            self.__color_bars.append(color_bar)

            # Add the control bar for each player
            control_bar = ArrowBar((draw_x + width + color_bar.get_width() + 20, draw_y), self.__controls, self.__control_surfaces)
            self.options.append(control_bar)
            for arrow in control_bar.get_arrows():
                self.options.append(arrow)
            self.__control_bars.append(control_bar)

        # Add the start option
        option_start = MenuOption("START", (380, 450), function=self.start)
        self.options.append(option_start)

        # Add the back option
        option_back = MenuOption("BACK", (10, 450), function=self.back)
        self.options.append(option_back)

    def start(self):
        """
        Creates the player data and starts the game
        """
        # Player 1
        joystick = None
        if 'JOYSTICK' in self.__control_bars[0].get():
            joystick = self.__joysticks[int(self.__control_bars[0].get()[-1])]
        player1 = Player("Player 1", (100, 100), self.__color_bars[0].get(), direction=RIGHT, controls=self.__control_bars[0].get(), joystick=joystick)
        self.__players.append(player1)

        # Player 2
        if self.__player_count >= 2:
            joystick = None
            if 'JOYSTICK' in self.__control_bars[1].get():
                joystick = self.__joysticks[int(self.__control_bars[1].get()[-1])]
            player2 = Player("Player 2", (self.surface.get_width() - 100, 100), self.__color_bars[1].get(), direction=DOWN, controls=self.__control_bars[1].get(), joystick=joystick)
            self.__players.append(player2)

        # Player 3
        if self.__player_count >= 3:
            joystick = None
            if 'JOYSTICK' in self.__control_bars[2].get():
                joystick = self.__joysticks[int(self.__control_bars[2].get()[-1])]
            player3 = Player("Player 3", (100, self.surface.get_width() - 100), self.__color_bars[2].get(), direction=UP, controls=self.__control_bars[2].get(), joystick=joystick)
            self.__players.append(player3)

        # Player 4
        if self.__player_count == 4:
            joystick = None
            if 'JOYSTICK' in self.__control_bars[3].get():
                joystick = self.__joysticks[int(self.__control_bars[3].get()[-1])]
            player4 = Player("Player 4", (self.surface.get_width() - 100, self.surface.get_width() - 100), self.__color_bars[3].get(), direction=LEFT, controls=self.__control_bars[3].get(), joystick=joystick)
            self.__players.append(player4)

        # Start the game
        if self.__player_count > 1:
            game_mode = 'multiplayer'
        else:
            game_mode = 'singleplayer'
        game_loop = GameLoop(self.gui, self.__players, game_mode)
        game_loop.run()

        # Reset surface (only runs when the user game has ended)
        self.surface.fill((0, 0, 0))

        # Redraw player names
        font = pygame.font.SysFont('Verdana', 40)
        for i in range(self.__player_count):
            width, height = font.size(f'Player {i + 1}')
            player_name = font.render(f'Player {i + 1}', False, (255, 255, 255))
            draw_x = 10
            draw_y = (self.surface.get_height() // 2) - (height * self.__player_count) + (height * i) + 50
            pygame.Surface.blit(self.surface, player_name, (draw_x, draw_y))

        # Reset player list
        self.__players = []

    def back(self):
        """
        Displays the previous menu.
        """
        self.running = False


class MenuOption:
    """
    An selectable option from the menu
    """
    __text = ''
    __pos = ()
    __option_font = None
    __function = None
    __size = ()
    surface = None

    def __init__(self, text, pos=None, function=None):
        """
        Constructor.

        :param text:         The text displayed for the menu option
        :param pos:          The position of the menu option on the screen as a tuple of x and y
        """
        self.__text = text
        self.__pos = pos
        self.__option_font = pygame.font.SysFont('Verdana', 30)
        self.__function = function
        if text is not None:
            self.size = self.__option_font.size(text)
            self.surface = self.__option_font.render(text, False, (255, 255, 255))

    def set_color(self, color):
        self.surface = self.__option_font.render(self.__text, False, color)

    def draw(self, surface):
        x, y = self.__pos
        pygame.Surface.blit(surface, self.surface, (x, y))

    def get_pos(self):
        """
        :return:  The position of the menu option
        """
        return self.__pos

    def get_size(self):
        """
        :return:  The size of the menu option
        """
        return self.size

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
        option_width, option_height = self.size
        if option_x <= x <= option_x + option_width and option_y <= y <= option_y + option_height:
            return True
        return False

    def select(self):
        """Runs the function associated with this menu option"""
        self.__function()


class ArrowOption(MenuOption):
    """
    A selectable menu option in the shape of an arrow.
    """
    __direction = None
    __color = ()

    def __init__(self, direction, pos=None, function=None):
        """
        Constructor.

        :param direction:   The direction the arrow is facing
        :param pos:         The position of the arrow
        :param function:    The function associated with this arrow
        """
        super(ArrowOption, self).__init__(None, pos, function)

        self.size = (30, 30)
        self.surface = pygame.Surface(self.size)
        self.__direction = direction
        self.set_color((255, 255, 255))
        self.__value_index = 0

    def __draw_arrow(self):
        """
        Draws the Arrow Option onto it's surface
        """
        width, height = self.size
        if self.__direction == UP:
            pygame.draw.polygon(self.surface, self.__color, ((width // 2, 0), (width, height), (width // 2, height - 10), (0, height), (width // 2, 0)))
        elif self.__direction == LEFT:
            pygame.draw.polygon(self.surface, self.__color, ((0, height // 2), (width, 0), (width - 10, height // 2), (width, height), (0, height // 2)))
        elif self.__direction == DOWN:
            pygame.draw.polygon(self.surface, self.__color, ((width // 2, height), (0, 0), (width // 2, 10), (width, 0), (width // 2, height)))
        elif self.__direction == RIGHT:
            pygame.draw.polygon(self.surface, self.__color, ((width, height // 2), (0, 0), (10, height // 2), (0, height), (width, height // 2)))

    def set_color(self, color):
        """
        Sets the color the Arrow Option to the given color.

        :param color:  The color to set the Arrow Option to
        """
        self.__color = color
        self.__draw_arrow()


class ArrowBar:
    """
    Two arrows options that face opposite directions and change the same value back and forth
    """
    __pos = None
    __values = None
    __value_index = None
    __surfaces = None
    __surface = None
    __gap = None
    __orientation = None
    __left_arrow = None
    __right_arrow = None
    __arrows = None

    def __init__(self, pos, values, surfaces, gap=60):
        """
        Constructor.

        :param pos:       The position of the arrow bar
        :param values:    A list of values to be changed back and forth with the arrow bar
        :param surfaces:  The surfaces that correspond to each value in the list of values
        :param gap:       The gap between each arrow in the arrow bar
        """
        self.__pos = pos
        self.__values = values
        self.__value_index = 0
        self.__surfaces = surfaces
        self.__surface = surfaces.get(self.__values[self.__value_index])
        self.__gap = gap
        self.__arrows = []

        # Create the arrows
        self.__left_arrow = ArrowOption(LEFT, (pos[0], pos[1] + 5), self.__left)
        self.__arrows.append(self.__left_arrow)

        self.__right_arrow = ArrowOption(RIGHT, (pos[0] + self.__left_arrow.size[0] + gap + 20, pos[1] + 5), self.__right)
        self.__arrows.append(self.__right_arrow)

    def __left(self):
        """
        Go to the previous value in the list of values associated with this arrow bar.
        """
        if self.__value_index > 0:
            self.__value_index -= 1
        else:
            self.__value_index = len(self.__values) - 1
        self.__surface = self.__surfaces.get(self.__values[self.__value_index])

    def __right(self):
        """
        Go to the next value in the list of values associated with this arrow bar.
        """
        if self.__value_index < len(self.__values) - 1:
            self.__value_index += 1
        else:
            self.__value_index = 0
        self.__surface = self.__surfaces.get(self.__values[self.__value_index])

    def draw(self, surface):
        x = self.__pos[0] + self.__arrows[0].size[0] + 10
        y = self.__pos[1]
        pygame.draw.rect(surface, (0, 0, 0), (x, y, self.__surface.get_width(), self.__surface.get_height()))
        pygame.Surface.blit(surface, self.__surface, (x, y))

    def get(self):
        """
        :return: The currently selected value in the value list
        """
        return self.__values[self.__value_index]

    def get_arrows(self):
        """
        :return:  The arrows associated with this arrow bar
        """
        return self.__arrows

    def get_width(self):
        width = 0
        for arrow in self.__arrows:
            width += arrow.size[0]
        width += self.__surface.get_width()
        width += 20
        return width

    def get_height(self):
        return self.__surface.get_height()
