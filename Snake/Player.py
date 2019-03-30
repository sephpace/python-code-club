
from pygame import draw, K_UP, K_LEFT, K_DOWN, K_RIGHT, K_w, K_a, K_s, K_d


# Global constants
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3


class Player:
    """
    The player game object.

    Each player is a snake of length four segments that can grow longer when they eat food by touching it.

    If a player's head touches the rest of their body, the border, or another player, it will die.
    """

    # Member variables
    __name = None            # The player's name
    __body_positions = None  # A list of tuples containing the xy coordinates of each segment of the player on the screen
    __color = None           # A tuple of ints representing the color of the player in RGB (Red, Green, and Blue)
    __size = None            # The size of each segment in the player (default is 10)
    __direction = None       # The direction the player is moving
    __alive = None           # A boolean that determines if the player is alive or not
    __joystick = None        # The joystick associated with this player (if any)
    up_button = None         # The button that makes the player turn upward
    left_button = None       # The button that makes the player turn leftward
    down_button = None       # The button that makes the player turn downward
    right_button = None      # The button that makes the player turn rightward

    def __init__(self, name, start_pos, color, size=10, direction=UP, controls='ARROW_KEYS', joystick=None):
        """Constructor"""
        self.__name = name

        if direction == UP:
            self.__body_positions = [start_pos,
                                    (start_pos[0], start_pos[1] + size),
                                    (start_pos[0], start_pos[1] + size * 2),
                                    (start_pos[0], start_pos[1] + size * 3)]
        elif direction == LEFT:
            self.__body_positions = [start_pos,
                                     (start_pos[0] + size, start_pos[1]),
                                     (start_pos[0] + size * 2, start_pos[1]),
                                     (start_pos[0] + size * 3, start_pos[1])]
        elif direction == DOWN:
            self.__body_positions = [start_pos,
                                     (start_pos[0], start_pos[1] - size),
                                     (start_pos[0], start_pos[1] - size * 2),
                                     (start_pos[0], start_pos[1] - size * 3)]
        elif direction == RIGHT:
            self.__body_positions = [start_pos,
                                     (start_pos[0] - size, start_pos[1]),
                                     (start_pos[0] - size * 2, start_pos[1]),
                                     (start_pos[0] - size * 3, start_pos[1])]

        self.__color = color
        self.__size = size
        self.__direction = direction
        self.__alive = True

        # Set up the joystick if there is one given
        if joystick is not None:
            joystick.init()
            self.__joystick = joystick

        # Set up the player's control bindings
        if controls == 'ARROW_KEYS':
            self.up_button = K_UP
            self.left_button = K_LEFT
            self.down_button = K_DOWN
            self.right_button = K_RIGHT
        elif controls == 'WASD':
            self.up_button = K_w
            self.left_button = K_a
            self.down_button = K_s
            self.right_button = K_d

    def add_segment(self):
        """
        Adds a new segment to the end of the player.
        """
        self.__body_positions.append(self.__body_positions[-1])

    def is_alive(self):
        """
        Returns True if the player is alive.

        :return:  True if the player is alive and False otherwise
        """
        return self.__alive

    def is_colliding(self, positions):
        """
        Returns True if the player's head collides with any of the given positions.

        :param positions:  A list of tuples containing xy coordinates on the screen
        :return:  True if the player's head is colliding with the given positions and false otherwise
        """
        if self.__body_positions[0] in positions:
            return True
        else:
            return False

    def draw(self, surface):
        """
        Draws all of the player's segments onto the given surface.

        :param surface:  The surface to draw the player onto
        """
        for pos in self.__body_positions:
            draw.rect(surface, self.__color, (pos[0], pos[1], self.__size, self.__size))

    def get_body_positions(self):
        """
        Returns the list of the positions of the segments of the player
        :return:  A list of tuples containing the xy coordinates of each segment of the player on the screen
        """
        return self.__body_positions

    def get_color(self):
        """
        Returns the color of the player.

        :return:  A tuple of integers containing the RGB (Red, Green, and Blue) values of the color of the player.
        """
        return self.__color

    def get_direction(self):
        """
        Returns the direction that the player is moving.

        :return:  An integer representing the direction of the player
        """
        return self.__direction

    def get_joystick(self):
        """
        Returns the joystick associated with this player and None if there are none.
        :return:  The pygame joystick object associated with this player and None if there are none
        """
        return self.__joystick

    def get_name(self):
        """
        Returns the name of the player.

        :return:  A string representing the name of the player
        """
        return self.__name

    def get_size(self):
        """
        Returns the size of the player.

        :return:  An int representing the size of each segment (or cell) in the player in pixels (default is 10)
        """
        return self.__size

    def kill(self):
        """
        Kills the player.
        """
        self.__alive = False

    def move(self):
        """
        Moves the player and all of their body segments in whatever direction they're facing.
        """
        for i in range(len(self.__body_positions) - 1, -1, -1):
            # Update the positions
            if i == 0:
                if self.__direction == UP:
                    self.__body_positions[i] = (self.__body_positions[i][0], self.__body_positions[i][1] - self.__size)
                elif self.__direction == LEFT:
                    self.__body_positions[i] = (self.__body_positions[i][0] - self.__size, self.__body_positions[i][1])
                elif self.__direction == DOWN:
                    self.__body_positions[i] = (self.__body_positions[i][0], self.__body_positions[i][1] + self.__size)
                elif self.__direction == RIGHT:
                    self.__body_positions[i] = (self.__body_positions[i][0] + self.__size, self.__body_positions[i][1])
            else:
                self.__body_positions[i] = self.__body_positions[i - 1]

    def set_direction(self, direction):
        """
        Changes the direction the player is moving to the given direction.

        :param direction:  The new direction the player will move in
        """
        self.__direction = direction
