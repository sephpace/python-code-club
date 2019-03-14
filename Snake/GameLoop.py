
import pygame
import random

from GUI import GUI
from Player import Player
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
    __player1 = None    # The player 1 object
    __player2 = None    # The player 2 object
    __player3 = None    # The player 3 object
    __players = None    # A list of all the players
    __foods = None      # A list of food objects
    __border = None     # The border object

    def __init__(self):
        """Constructor"""
        self.__gui = GUI(SCREEN_SIZE)
        self.__clock = pygame.time.Clock()
        self.setup()

    def setup(self):
        """Setup everything in the game to get it ready to start"""
        self.__player1 = Player((100, 100), (0, 255, 0), direction=RIGHT)
        self.__player2 = Player((SCREEN_SIZE - 100, 100), (255, 0, 0), direction = DOWN)
        self.__player3 = Player((100, SCREEN_SIZE - 100), (0, 0, 255), direction = UP)
        self.__player4 = Player((SCREEN_SIZE - 100, SCREEN_SIZE - 100), (255, 255, 0), direction=LEFT)
        self.__players = [self.__player1, self.__player2, self.__player3, self.__player4]
        self.__foods = [Food(self.get_rand_pos()), Food(self.get_rand_pos()), Food(self.get_rand_pos()), Food(self.get_rand_pos())]
        self.__border = Border(SCREEN_SIZE, GRID_SIZE)

    def start(self):
        """Start the game loop"""
        self.__gui.show_menu()  # Run the menu first
        self.run()

    def run(self):
        """Run the logic of the loop"""
        while True:
            # Event handler
            for event in pygame.event.get():
                # Key events
                if event.type == pygame.KEYDOWN:
                    key = event.key

                    # --- Player 1 ---
                    if self.__player1.is_alive():
                        if key == pygame.K_UP:
                            if self.__player1.get_direction() != DOWN:
                                self.__player1.set_direction(UP)
                        if key == pygame.K_LEFT:
                            if self.__player1.get_direction() != RIGHT:
                                self.__player1.set_direction(LEFT)
                        if key == pygame.K_DOWN:
                            if self.__player1.get_direction() != UP:
                                self.__player1.set_direction(DOWN)
                        if key == pygame.K_RIGHT:
                            if self.__player1.get_direction() != LEFT:
                                self.__player1.set_direction(RIGHT)

                    # --- Player 2 ---
                    if self.__player2.is_alive():
                        if key == pygame.K_w:
                            if self.__player2.get_direction() != DOWN:
                                self.__player2.set_direction(UP)
                        if key == pygame.K_a:
                            if self.__player2.get_direction() != RIGHT:
                                self.__player2.set_direction(LEFT)
                        if key == pygame.K_s:
                            if self.__player2.get_direction() != UP:
                                self.__player2.set_direction(DOWN)
                        if key == pygame.K_d:
                            if self.__player2.get_direction() != LEFT:
                                self.__player2.set_direction(RIGHT)

                    # --- Player 3 ---
                    if self.__player3.is_alive():
                        if key == pygame.K_UP:
                            if self.__player3.get_direction() != DOWN:
                                self.__player3.set_direction(UP)
                        if key == pygame.K_LEFT:
                            if self.__player3.get_direction() != RIGHT:
                                self.__player3.set_direction(LEFT)
                        if key == pygame.K_DOWN:
                            if self.__player3.get_direction() != UP:
                                self.__player3.set_direction(DOWN)
                        if key == pygame.K_RIGHT:
                            if self.__player3.get_direction() != LEFT:
                                self.__player3.set_direction(RIGHT)

                    # --- Player 4 ---
                    if self.__player4.is_alive():
                        if key == pygame.K_w:
                            if self.__player4.get_direction() != DOWN:
                                self.__player4.set_direction(UP)
                        if key == pygame.K_a:
                            if self.__player4.get_direction() != RIGHT:
                                self.__player4.set_direction(LEFT)
                        if key == pygame.K_s:
                            if self.__player4.get_direction() != UP:
                                self.__player4.set_direction(DOWN)
                        if key == pygame.K_d:
                            if self.__player4.get_direction() != LEFT:
                                self.__player4.set_direction(RIGHT)


                # Quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Clear the screen
            self.__gui.clear()

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

            # Check for a winner
            if len(self.__players) == 1:
                self.__gui.game_over(self.__players[0].get_color())
                self.restart()
    
    def get_rand_pos(self):
        return random.randint(2, SCREEN_SIZE // GRID_SIZE - 2) * GRID_SIZE, random.randint(2,SCREEN_SIZE // GRID_SIZE - 2) * GRID_SIZE

    def restart(self):
        """Restarts the game from the menu"""
        self.__gui.show_menu()
        self.setup()
