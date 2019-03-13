
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
    __players = None    # A list of player options
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
        self.__players = []
        self.__foods = [Food(self.get_rand_pos()), Food(self.get_rand_pos()), Food(self.get_rand_pos()), Food(self.get_rand_pos())]
        self.__border = Border(SCREEN_SIZE, GRID_SIZE)
        self.__score_bar = ScoreBar()

    def start(self):
        """Start the game loop"""
        while True:
            game_mode = self.__gui.main_menu()  # Run the menu first
            if game_mode == 0:  # Single player
                this_player = Player((SCREEN_SIZE // 2, SCREEN_SIZE // 2), (0, 255, 0))
                self.__players.append(this_player)
                self.run(game_mode, this_player)
            else:  # Multiplayer
                player_name = self.__gui.customization_menu()
                this_player, other_players = self.__gui.multiplayer_menu(game_mode, player_name)
                self.__players.append(this_player)
                self.__players.append(other_players)
                self.run(game_mode, this_player)
            self.__gui.game_over()
            self.setup()

    def run(self, game_mode, this_player):
        """Run the logic of the loop"""
        running = True
        while running:
            # Clear the screen
            self.__gui.clear()

            # Event handler
            for event in pygame.event.get():
                # Key events
                if event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_UP:
                        if this_player.get_direction() != DOWN:
                            this_player.set_direction(UP)
                    if key == pygame.K_LEFT:
                        if this_player.get_direction() != RIGHT:
                            this_player.set_direction(LEFT)
                    if key == pygame.K_DOWN:
                        if this_player.get_direction() != UP:
                            this_player.set_direction(DOWN)
                    if key == pygame.K_RIGHT:
                        if this_player.get_direction() != LEFT:
                            this_player.set_direction(RIGHT)
                # Quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            for player in self.__players:
                # Move the players
                player.move()

                # Check for collisions with self and border
                if player.is_colliding(self.__border.get_positions() + player.get_body_positions()[1:]):
                    # Stop the game loop
                    running = False

                # Check for collisions with the food pieces
                for food in self.__foods:
                    if player.is_colliding([food.get_pos()]):
                        # Move the food
                        food.set_pos(self.get_rand_pos())

                        # Add a new body segment to the snake
                        player.add_segment()

                        # Update the score
                        self.__score_bar.increment()

            # Draw all of the game objects
            self.__gui.draw(self.__foods)
            self.__gui.draw([self.__border, self.__score_bar])
            self.__gui.draw(self.__players)

            # Update the screen
            self.__gui.update()

            # Set the speed of each frame
            self.__clock.tick(10)
    
    def get_rand_pos(self):
        return random.randint(2, SCREEN_SIZE // GRID_SIZE - 2) * GRID_SIZE, random.randint(2,SCREEN_SIZE // GRID_SIZE - 2) * GRID_SIZE
