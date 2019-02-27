
from pygame import draw


UP = 0
LEFT = 1
RIGHT = 2
DOWN = 3


class Player:
    """Members"""
    __body_positions = []  # A list of tuples containing x and y coordinates of each segment of the snake
    __color = ()           # The color of the snake
    __size = 0             # The size of each segment in the snake
    __direction = 0

    """Constructor"""
    def __init__(self, start_pos, color, size=10, direction=UP):
        self.__body_positions = [start_pos,
                                (start_pos[0], start_pos[1] + size),
                                (start_pos[0], start_pos[1] + size * 2),
                                (start_pos[0], start_pos[1] + size * 3)]
        self.__color = color
        self.__size = size
        self.__direction = direction

    """Adds a new segment to the end of the snake"""
    def add_segment(self):
        self.__body_positions.append(self.__body_positions[-1])

    """Returns True if the snake's head collides with any of the given positions"""
    def is_colliding(self, positions):
        if self.__body_positions[0] in positions:
            return True
        else:
            return False

    """Draws all of the snake segments onto the given surface"""
    def draw(self, surface):
        for pos in self.__body_positions:
            draw.rect(surface, self.__color, (pos[0], pos[1], self.__size, self.__size))

    """Returns the list of segements of the snake"""
    def get_body_positions(self): return self.__body_positions

    """Returns the color of the snake"""
    def get_color(self): return self.__color

    """Returns the direction that the snake is moving"""
    def get_direction(self): return self.__direction

    """Returns the size of the snake"""
    def get_size(self): return self.__size

    """Moves the snake in whatever direction it's facing"""
    def move(self):
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

    """Changes the direction the snake is moving to the given direction"""
    def set_direction(self, direction): self.__direction = direction
