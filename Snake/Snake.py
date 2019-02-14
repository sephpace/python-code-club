
from pygame import draw
from GUI import GUI


class Snake:
    def __init__(self, x, y, color):
        self.__x = x
        self.__y = y
        self.__color = color

    def get_x(self): return self.__x

    def get_y(self): return self.__y

    def set_x(self, x): self.__x = x

    def set_y(self, y): self.__y = y

    def draw(self, surface):
        draw.rect(surface, self.__color, (self.__x, self.__y, GUI.GRID_SIZE, GUI.GRID_SIZE))
