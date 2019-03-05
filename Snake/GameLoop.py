
import pygame
import random

from GUI import GUI
from Player import Player
from Food import Food
from Border import Border
from ScoreBar import ScoreBar


SCREEN_SIZE = 500
GRID_SIZE = 10

UP = 0
LEFT = 1
RIGHT = 2
DOWN = 3


class GameLoop:
    """The main loop of the game.  Calculates all of the non-visual logic"""

    # Member variables
    __gui = None        # The game's Graphical User Interface
    __clock = None      # The game clock used to set the fps of the game
    __player = None     # The player object
    __foods = None      # A list of food objects
    __border = None     # The border object
    __score_bar = None  # The score bar object

    def __init__(self):
        """Constructor"""
        self.__gui = GUI(SCREEN_SIZE)
        self.__clock = pygame.time.Clock()
        self.setup()

    def setup(self):
        """Setup everything in the game to get it ready to start"""
        self.__player = Player((SCREEN_SIZE // 2, SCREEN_SIZE // 2), (0, 255, 0))
        self.__foods = [Food(self.get_rand_pos()), Food(self.get_rand_pos()), Food(self.get_rand_pos()), Food(self.get_rand_pos())]
        self.__border = Border(SCREEN_SIZE, GRID_SIZE)
        self.__score_bar = ScoreBar()

    def start(self):
        """Start the game loop"""
        while True:
            game_mode = self.__gui.show_menu()  # Run the menu first
            self.run(game_mode)
            self.__gui.game_over()
            self.setup()

    def run(self, game_mode):
        """Run the logic of the loop"""
        while True:
            # Event handler
            for event in pygame.event.get():
                # Key events
                if event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_UP:
                        if self.__player.get_direction() != DOWN:
                            self.__player.set_direction(UP)
                    if key == pygame.K_LEFT:
                        if self.__player.get_direction() != RIGHT:
                            self.__player.set_direction(LEFT)
                    if key == pygame.K_DOWN:
                        if self.__player.get_direction() != UP:
                            self.__player.set_direction(DOWN)
                    if key == pygame.K_RIGHT:
                        if self.__player.get_direction() != LEFT:
                            self.__player.set_direction(RIGHT)
                # Quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Clear the screen
            self.__gui.clear()

            # Move the snake
            self.__player.move()

            # Check for collisions with self and border
            if self.__player.is_colliding(self.__border.get_positions() + self.__player.get_body_positions()[1:]):
                # Stop the game loop
                break

            # Check for collisions with the food pieces
            for food in self.__foods:
                if self.__player.is_colliding([food.get_pos()]):
                    # Move the food
                    food.set_pos(self.get_rand_pos())

                    # Add a new body segment to the snake
                    self.__player.add_segment()

                    # Update the score
                    self.__score_bar.increment()

            # Draw all of the game objects
            self.__gui.draw(self.__foods + [self.__border, self.__player, self.__score_bar])

            # Update the screen
            self.__gui.update()

            # Set the speed of each frame
            self.__clock.tick(10)
    
    def get_rand_pos(self):
        return random.randint(2, SCREEN_SIZE // GRID_SIZE - 2) * GRID_SIZE, random.randint(2,SCREEN_SIZE // GRID_SIZE - 2) * GRID_SIZE
