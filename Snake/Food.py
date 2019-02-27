
from pygame import draw


class Food:
    """Members"""
    __pos = ()  # A tuple representing the position of the food
    __size = 0

    """Constructor"""
    def __init__(self, pos, size=10):
        self.__pos = pos
        self.__size = size

    """Draws the food to the given surface"""
    def draw(self, surface):
        draw.rect(surface, (153, 76, 0), (self.__pos[0], self.__pos[1], self.__size, self.__size))

    """Return the position of the food"""
    def get_pos(self): return self.__pos

    """Set the position of the food to the given value"""
    def set_pos(self, pos): self.__pos = pos
