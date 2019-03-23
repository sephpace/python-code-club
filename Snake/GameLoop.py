
import pygame
import random

from GUI import GUI
from Food import Food
from Border import Border


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
    __joysticks = None  # A list of all the joysticks currently connected to the computer
    __players = None    # A list of all the players
    __foods = None      # A list of food objects
    __border = None     # The border object

    def __init__(self):
        """Constructor"""
        self.__gui = GUI(SCREEN_SIZE)
        self.__clock = pygame.time.Clock()

    def setup(self):
        """Setup everything in the game to get it ready to start"""
        self.__foods = [Food(self.get_rand_pos()), Food(self.get_rand_pos()), Food(self.get_rand_pos()), Food(self.get_rand_pos())]
        self.__border = Border(SCREEN_SIZE, GRID_SIZE)

    def start(self):
        """Start the game loop"""
        while True:
            self.setup()
            self.__players, game_mode = self.__gui.show_menu()  # Run the menu first
            self.run(game_mode)

    def run(self, game_mode):
        """Run the logic of the loop"""
        running = True
        while running:
            # Clear the screen
            self.__gui.clear()

            # Event handler
            for event in pygame.event.get():
                # Key events
                if event.type == pygame.KEYDOWN:
                    for player in self.__players:
                        if player.is_alive():
                            key = event.key
                            if key == player.up_button:
                                if player.get_direction() != DOWN:
                                    player.set_direction(UP)
                            if key == player.left_button:
                                if player.get_direction() != RIGHT:
                                    player.set_direction(LEFT)
                            if key == player.down_button:
                                if player.get_direction() != UP:
                                    player.set_direction(DOWN)
                            if key == player.right_button:
                                if player.get_direction() != LEFT:
                                    player.set_direction(RIGHT)

                if event.type == pygame.JOYHATMOTION:
                    for player in self.__players:
                        if player.is_alive():
                            if player.get_joystick() is not None:
                                if event.joy == player.get_joystick().get_id():
                                    x_axis, y_axis = event.value
                                    if y_axis == 1:
                                        if player.get_direction() != DOWN:
                                            player.set_direction(UP)
                                    if x_axis == -1:
                                        if player.get_direction() != RIGHT:
                                            player.set_direction(LEFT)
                                    if y_axis == -1:
                                        if player.get_direction() != UP:
                                            player.set_direction(DOWN)
                                    if x_axis == 1:
                                        if player.get_direction() != LEFT:
                                            player.set_direction(RIGHT)

                # Quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            for player in self.__players:
                if player.is_alive():
                    # Move the snake
                    player.move()

                    # Check for collisions with self and border
                    if player.is_colliding(self.__border.get_positions() + player.get_body_positions()[1:]):
                        player.kill()
                        self.__players.remove(player)

                    # Check for collisions with other players
                    for other_player in self.__players:
                        if other_player == player:
                            continue
                        else:
                            if player.is_colliding(other_player.get_body_positions()):
                                player.kill()
                                self.__players.remove(player)

                    # Check for collisions with the food pieces
                    for food in self.__foods:
                        if player.is_colliding([food.get_pos()]):
                            # Move the food
                            food.set_pos(self.get_rand_pos())

                            # Add a new body segment to the snake
                            player.add_segment()

                    # Draw each player
                    self.__gui.draw(player)

            # Draw all of the game objects
            self.__gui.draw(self.__foods)
            self.__gui.draw(self.__border)

            # Update the screen
            self.__gui.update()

            # Set the speed of each frame
            self.__clock.tick(10)

            # Check for singleplayer game over
            if game_mode == 'singleplayer':
                if len(self.__players) == 0:
                    self.__gui.game_over((255, 255, 255), game_mode)
                    running = False

            # Check for a winner
            if game_mode == 'multiplayer':
                if len(self.__players) == 1:
                    self.__gui.game_over(self.__players[0].get_color(), game_mode)
                    running = False
    
    def get_rand_pos(self):
        return random.randint(2, SCREEN_SIZE // GRID_SIZE - 2) * GRID_SIZE, random.randint(2,SCREEN_SIZE // GRID_SIZE - 2) * GRID_SIZE
