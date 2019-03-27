
from pygame import quit, draw, K_UP, K_LEFT, K_DOWN, K_RIGHT, K_w, K_a, K_s, K_d


UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3


class Player:
    """A snake controlled by a player"""

    # Member variables
    __body_positions = []  # A list of tuples containing x and y coordinates of each segment of the snake
    __color = ()           # The color of the snake
    __size = 0             # The size of each segment in the snake
    __direction = 0        # The direction the snake is moving
    __alive = True         # A boolean that determines if the snake is alive or not
    __joystick = None
    up_button = None
    left_button = None
    down_button = None
    right_button = None

    def __init__(self, start_pos, color, size=10, direction=UP, controls='ARROW_KEYS', joystick=None):
        """Constructor"""
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
        if joystick is not None:
            joystick.init()
            self.__joystick = joystick

    def add_segment(self):
        """Adds a new segment to the end of the snake"""
        self.__body_positions.append(self.__body_positions[-1])

    def is_alive(self):
        return self.__alive

    def is_colliding(self, positions):
        """Returns True if the snake's head collides with any of the given positions"""
        if self.__body_positions[0] in positions:
            return True
        else:
            return False

    def draw(self, surface):
        """Draws all of the snake segments onto the given surface"""
        for pos in self.__body_positions:
            draw.rect(surface, self.__color, (pos[0], pos[1], self.__size, self.__size))

    def get_body_positions(self):
        """Returns the list of segements of the snake"""
        return self.__body_positions

    def get_color(self):
        """Returns the color of the snake"""
        return self.__color

    def get_direction(self):
        """Returns the direction that the snake is moving"""
        return self.__direction

    def get_joystick(self):
        """Returns the pygame joystick object associated with this player and None if there are no joysticks associated with this player"""
        return self.__joystick

    def get_size(self):
        """Returns the size of the snake"""
        return self.__size

    def kill(self):
        self.__alive = False

    def move(self):
        """Moves the snake in whatever direction it's facing"""
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
        """Changes the direction the snake is moving to the given direction"""
        self.__direction = direction
