
from pygame import draw


class Border:
    """The border surrounding the players"""

    # Member variables
    __screen_size = 0        # The size of the screen
    __cell_size = 0          # The size of each cell in the grid
    __color = ()             # The color of the border
    __square_positions = []  # Positions of each square in the border

    def __init__(self, screen_size, cell_size, color=(127, 127, 127)):
        """Constructor"""
        self.__screen_size = screen_size
        self.__cell_size = cell_size
        self.__color = color
        for i in range(0, screen_size, cell_size):
            self.__square_positions.append((i, 0))
            self.__square_positions.append((0, i))
            self.__square_positions.append((screen_size - cell_size, i))
            self.__square_positions.append((i, screen_size - cell_size))

    def draw(self, surface):
        """Draws the border onto the given surface"""
        for pos in self.__square_positions:
            draw.rect(surface, self.__color, (pos[0], pos[1], self.__cell_size, self.__cell_size))


    def get_positions(self):
        """Returns the positions of each square in the border"""
        return self.__square_positions
