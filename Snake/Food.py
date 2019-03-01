
from pygame import draw


class Food:
    """A bit of food that a player can collect"""

    # Member variables
    __pos = ()  # A tuple representing the position of the food
    __size = 0

    def __init__(self, pos, size=10):
        """Constructor"""
        self.__pos = pos
        self.__size = size

    def draw(self, surface):
        """Draws the food to the given surface"""
        draw.rect(surface, (153, 76, 0), (self.__pos[0], self.__pos[1], self.__size, self.__size))

    def get_pos(self):
        """Return the position of the food"""
        return self.__pos

    def set_pos(self, pos):
        """Set the position of the food to the given value"""
        self.__pos = pos
