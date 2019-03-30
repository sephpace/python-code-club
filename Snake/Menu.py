
import pygame
from Player import Player
from GameLoop import GameLoop


# Global constants
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3


class Menu:
    """
    Basic menu class.
    """
    gui = None      # The game's main GUI
    surface = None  # The surface to display the menu onto
    options = None  # A list of MenuOption objects associated with this menu
    running = None  # A boolean that is True if the menu is running

    def __init__(self, gui, surface):
        """
        Constructor.

        :param surface:  The surface to display the menu on
        """
        pygame.init()

        self.gui = gui
        self.surface = surface
        self.options = []
        self.running = True

        # Clear and update the surface
        self.surface.fill((0, 0, 0))
        pygame.display.update()

    def handle(self):
        """
        Display all of the options on the surface.
        """
        while self.running:
            for option in self.options:
                option.draw(self.surface)

            # Events
            for event in pygame.event.get():
                # Mouse motion event
                if event.type == pygame.MOUSEMOTION:
                    for option in self.options:
                        if type(option) != ArrowBar:
                            if option.contains(event.pos):
                                option.set_color((0, 255, 0))
                            else:
                                option.set_color((255, 255, 255))

                # Mouse clicked event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for option in self.options:
                            if type(option) != ArrowBar:
                                if option.contains(event.pos):
                                    option.select()

                # Quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Update the screen
            pygame.display.update()


class MainMenu(Menu):
    """
    The main menu that pops up when the game is first launched and in between rounds.
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
        Logic for when the 'singleplayer' option is selected.

        Starts a single player game.
        """
        customization_menu = CustomizationMenu(self.gui, self.surface, 1)
        customization_menu.handle()

        # Reset surface (only runs when the user hits 'back' on the following menu
        self.surface.fill((0, 0, 0))
        self.__init__(self.gui, self.surface)

    def multiplayer(self):
        """
        Logic for when the 'multiplayer' option is selected.

        Starts a multiplayer game.
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

        # Set up the menu options
        # Two players
        option_two_player = MenuOption("2 PLAYER", function=self.two_player)
        width, height = option_two_player.get_size()
        option_two_player.set_pos(((self.surface.get_width() // 2) - (width // 2), 185))
        self.options.append(option_two_player)

        # Three players
        option_three_player = MenuOption("3 PLAYER", function=self.three_player)
        width, height = option_three_player.get_size()
        option_three_player.set_pos(((self.surface.get_width() // 2) - (width // 2), 230))
        self.options.append(option_three_player)

        # Four players
        option_four_player = MenuOption("4 PLAYER", function=self.four_player)
        width, height = option_four_player.get_size()
        option_four_player.set_pos(((self.surface.get_width() // 2) - (width // 2), 275))
        self.options.append(option_four_player)

        # The back option
        option_back = MenuOption("BACK", (10, 450), function=self.back)
        self.options.append(option_back)

    def two_player(self):
        """
        Logic for when the 'two player' option is selected.

        Starts a two player game
        """
        self.start_customization_menu(2)

    def three_player(self):
        """
        Logic for when the 'three player' option is selected.

        Starts a three player game.
        """
        self.start_customization_menu(3)

    def four_player(self):
        """
        Logic for when the 'four player' option is selected.

        Starts a four player game.
        """
        self.start_customization_menu(4)

    def start_customization_menu(self, player_amt):
        """
        Starts the customization menu with the given amount of players.

        :param player_amt:  The amount of players that will be in the game
        """
        customization_menu = CustomizationMenu(self.gui, self.surface, player_amt)
        customization_menu.handle()

        # Reset surface (only runs when the user hits 'back' on the following menu)
        self.surface.fill((0, 0, 0))
        self.__init__(self.gui, self.surface)

    def back(self):
        """
        Logic for when the 'back' option is selected.

        Displays the previous menu.
        """
        self.running = False


class CustomizationMenu(Menu):
    """
    Allows players to customize their snake color and set their controls.
    """
    __players = None           # A list of players in the game
    __player_count = None      # The amount of player in the game
    __joysticks = None         # All of the connected joysticks that are detected
    __colors = None            # A list of possible color choices
    __color_surfaces = None    # A list of pygame surfaces with rectangles of each color drawn onto them
    __controls = None          # A list of possible control choices
    __control_surfaces = None  # A list of pygame surfaces with pictures representing each selectable controller type drawn onto them
    __color_bars = None        # A list of ArrowBar objects showing the selected color for each player in the game
    __control_bars = None      # A list of ArrowBar objects showing the selected controls for each player in the game

    def __init__(self, gui, surface, player_count):
        """
        Constructor.

        :param gui:           # The game's main GUI
        :param surface:       # The surface to display the menu onto
        :param player_count:  # The amount of players in the game
        """
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

        # Draw all of the objects onto the screen
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

        # Add the rest of the menu options
        # The start option
        option_start = MenuOption("START", (380, 450), function=self.start)
        self.options.append(option_start)

        # The back option
        option_back = MenuOption("BACK", (10, 450), function=self.back)
        self.options.append(option_back)

    def start(self):
        """
        Logic for when the 'start' option is selected.

        Creates the player data and starts the game.
        """
        # Player 1
        # Set up their joystick if they have one
        joystick = None
        if 'JOYSTICK' in self.__control_bars[0].get():
            joystick = self.__joysticks[int(self.__control_bars[0].get()[-1])]

        # Create the player object
        if self.__player_count > 1:
            # Single player settings
            player1 = Player("Player 1", (100, 100), self.__color_bars[0].get(), direction=RIGHT, controls=self.__control_bars[0].get(), joystick=joystick)
        else:
            # Multi player settings
            player1 = Player("Player 1", (self.surface.get_width() // 2, 400), self.__color_bars[0].get(), direction=UP, controls=self.__control_bars[0].get(), joystick=joystick)
        self.__players.append(player1)

        # Player 2
        if self.__player_count >= 2:
            # Set up their joystick if they have one
            joystick = None
            if 'JOYSTICK' in self.__control_bars[1].get():
                joystick = self.__joysticks[int(self.__control_bars[1].get()[-1])]

            # Create the player object
            player2 = Player("Player 2", (self.surface.get_width() - 100, 100), self.__color_bars[1].get(), direction=DOWN, controls=self.__control_bars[1].get(), joystick=joystick)
            self.__players.append(player2)

        # Player 3
        if self.__player_count >= 3:
            # Set up their joystick if they have one
            joystick = None
            if 'JOYSTICK' in self.__control_bars[2].get():
                joystick = self.__joysticks[int(self.__control_bars[2].get()[-1])]

            # Create the player object
            player3 = Player("Player 3", (100, self.surface.get_width() - 100), self.__color_bars[2].get(), direction=UP, controls=self.__control_bars[2].get(), joystick=joystick)
            self.__players.append(player3)

        # Player 4
        if self.__player_count == 4:
            # Set up their joystick if they have one
            joystick = None
            if 'JOYSTICK' in self.__control_bars[3].get():
                joystick = self.__joysticks[int(self.__control_bars[3].get()[-1])]

            # Create the player object
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
        Logic for when the 'back' option is selected.

        Displays the previous menu.
        """
        self.running = False


class MenuOption:
    """
    An selectable option from the menu.
    """
    __text = None         # The text displayed for the menu option
    __pos = None          # A tuple containing the xy coordinates of the menu option on the surface
    __option_font = None  # The font that the text for the menu option is written in
    __function = None     # The function that is called by the menu option once selected
    __size = None         # A tuple of integers containing the width and height of the menu option
    surface = None        # The pygame surface that the menu option is drawn onto

    def __init__(self, text, pos=None, function=None):
        """
        Constructor.

        :param text:         The text displayed for the menu option
        :param pos:          A tuple containing the xy coordinates of the menu option on the surface
        """
        self.__text = text
        self.__pos = pos
        self.__option_font = pygame.font.SysFont('Verdana', 30)
        self.__function = function
        if text is not None:
            self.size = self.__option_font.size(text)
            self.surface = self.__option_font.render(text, False, (255, 255, 255))

    def set_color(self, color):
        """
        Sets the color of the text of the menu option to the given RGB value.

        :param color:  A tuple of integers containing the new RGB values of the text of the menu option
        """
        self.surface = self.__option_font.render(self.__text, False, color)

    def draw(self, surface):
        """
        Draws the menu option onto the given surface.

        :param surface:  The surface to draw the menu option onto
        """
        x, y = self.__pos
        pygame.Surface.blit(surface, self.surface, (x, y))

    def get_pos(self):
        """
        Returns the position of the menu option.

        :return:  A tuple of integers containing the xy coordinates of the position of the menu option on the surface
        """
        return self.__pos

    def get_size(self):
        """
        Returns the size of the menu option.

        :return:  A tuple of integers containing the width and height of the menu option
        """
        return self.size

    def set_pos(self, pos):
        """
        Sets the position of the menu option to the given value.

        :param pos:  A tuple of integers containing the new xy coordinates of the menu option on the surface
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
        """
        Calls the function associated with this menu option.
        """
        self.__function()


class ArrowOption(MenuOption):
    """
    A selectable menu option in the shape of an arrow.
    """
    __direction = None  # The direction the arrow is facing (either 'UP', 'LEFT', 'RIGHT', or 'DOWN')
    __color = ()        # A tuple of integers containing the RGB values of the color of the arrow option

    def __init__(self, direction, pos=None, function=None):
        """
        Constructor.

        :param direction:   The direction the arrow is facing (either 'UP', 'LEFT', 'RIGHT', or 'DOWN')
        :param pos:         A tuple of integers containing the xy coordinates of the position of the arrow option
        :param function:    The function associated with this arrow option
        """
        super(ArrowOption, self).__init__(None, pos, function)

        self.size = (30, 30)
        self.surface = pygame.Surface(self.size)
        self.__direction = direction
        self.set_color((255, 255, 255))
        self.__value_index = 0

    def __draw_arrow(self):
        """
        Draws the Arrow Option onto it's surface.
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
        Sets the color the arrow option to the given color.

        :param color:  A tuple of integers containing the RGB value of the color of the arrow option
        """
        self.__color = color
        self.__draw_arrow()


class ArrowBar:
    """
    Two arrows options that face opposite directions and change the same value back and forth.

    The value has a surface (image) associated with it that is displayed between the arrows.
    """
    __pos = None          # A tuple containing the xy coordinates of the menu option on the surface
    __values = None       # A list of values that can be iterated through when the arrows are selected
    __value_index = None  # The index of the currently selected value
    __surfaces = None     # A list of surfaces that can be iterated through when the arrows are selected (in unison with the values)
    __surface = None      # The surface to draw the arrow bar onto
    __gap = None          # The gap between each arrow in the arrow bar
    __left_arrow = None   # The arrow option that is displayed to the left of the selected value
    __right_arrow = None  # The arrow option that is displayed to the right of the selected value
    __arrows = None       # A list containing each arrow option in the arrow bar (in pixels)

    def __init__(self, pos, values, surfaces, gap=60):
        """
        Constructor.

        :param pos:       A tuple containing the xy coordinates of the menu option on the surface
        :param values:    A list of values that can be iterated through when the arrows are selected
        :param surfaces:  A list of surfaces that can be iterated through when the arrows are selected (in unison with the values)
        :param gap:       The gap between each arrow in the arrow bar (in pixels)
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
        Sets the index of the currently selected value to that of the previous value in the list of values associated with this arrow bar.
        """
        if self.__value_index > 0:
            self.__value_index -= 1
        else:
            self.__value_index = len(self.__values) - 1
        self.__surface = self.__surfaces.get(self.__values[self.__value_index])

    def __right(self):
        """
        Sets the index of the currently selected value to that of the next value in the list of values associated with this arrow bar.
        """
        if self.__value_index < len(self.__values) - 1:
            self.__value_index += 1
        else:
            self.__value_index = 0
        self.__surface = self.__surfaces.get(self.__values[self.__value_index])

    def draw(self, surface):
        """
        Draws the arrow bar onto the given surface.

        :param surface:  The surface to draw the arrow bar onto
        """
        x = self.__pos[0] + self.__arrows[0].size[0] + 10
        y = self.__pos[1]
        pygame.draw.rect(surface, (0, 0, 0), (x, y, self.__surface.get_width(), self.__surface.get_height()))
        pygame.Surface.blit(surface, self.__surface, (x, y))

    def get(self):
        """
        Returns the currently selected value in the value list.

        :return: The currently selected value in the value list
        """
        return self.__values[self.__value_index]

    def get_arrows(self):
        """
        Returns the arrows associated with this arrow bar.

        :return:  The list of arrow options associated with this arrow bar
        """
        return self.__arrows

    def get_width(self):
        """
        Returns the width of the arrow bar.

        :return:  An integer representing the width of the arrow bar
        """
        width = 0
        for arrow in self.__arrows:
            width += arrow.size[0]
        width += self.__surface.get_width()
        width += 20
        return width

    def get_height(self):
        """
        Returns the height of the arrow bar.

        :return:  An iteger representing the height of the arrow bar
        """
        return self.__surface.get_height()
