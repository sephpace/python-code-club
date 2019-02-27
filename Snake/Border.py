
from pygame import draw


class Border:
    """Members"""
    __screen_size = 0        # The size of the screen
    __cell_size = 0          # The size of each cell in the grid
    __color = ()             # The color of the border
    __square_positions = []  # Positions of each square in the border

    """Constructor"""
    def __init__(self, screen_size, cell_size, color=(0, 0, 255)):
        self.__screen_size = screen_size
        self.__cell_size = cell_size
        self.__color = color
        for i in range(0, screen_size, cell_size):
            self.__square_positions.append((i, 0))
            self.__square_positions.append((0, i))
            self.__square_positions.append((screen_size - cell_size, i))
            self.__square_positions.append((i, screen_size - cell_size))

    """Draws the border onto the given surface"""
    def draw(self, surface):
        for pos in self.__square_positions:
            draw.rect(surface, self.__color, (pos[0], pos[1], self.__cell_size, self.__cell_size))

    # Returns the positions of each square in the border
    def get_positions(self): return self.__square_positions
