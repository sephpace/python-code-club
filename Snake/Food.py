
from pygame import draw


class Food:
    """
    A bit of food that a player can eat.

    Takes up a single grid position and teleports to a new, randomly selected spot once it is eaten by a player.

    Once eaten, the size of the player's snake will grow by one cell.

    Will increment the player's score by one if the game mode is singleplayer.
    """

    # Member variables
    __pos = None   # A tuple representing the position of the food
    __size = None  # The size of the food (default is 10)

    def __init__(self, pos, size=10):
        """
        Constructor.

        :param pos:   A tuple representing the position of the food
        :param size:  The size of the food (default is 10)
        """
        self.__pos = pos
        self.__size = size

    def draw(self, surface):
        """
        Draws the food to the given surface.

        :param surface:  The surface to draw the food onto
        """
        draw.rect(surface, (153, 76, 0), (self.__pos[0], self.__pos[1], self.__size, self.__size))

    def get_pos(self):
        """
        Return the position of the food.

        :return:  A tuple containing the xy coordinates on the screen
        """
        return self.__pos

    def set_pos(self, pos):
        """
        Set the position of the food to the given value.

        :param pos:  A tuple containing the xy coordinates for the new position for the food on the screen
        """
        self.__pos = pos
