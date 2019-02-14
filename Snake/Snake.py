
from pygame import draw
from GUI import GUI


class Snake:
    def __init__(self, x, y, color, direction=0):
        self.__pos = [(x * GUI.GRID_SIZE, y * GUI.GRID_SIZE)]
        self.__color = color
        self.__direction = direction

    def get_pos(self): return self.__pos[0]

    def set_pos(self, x, y):
        for i in range(len(self.__pos), 0, -1):
            if i == 0:
                self.__pos[0] = (x, y)
            else:
                self.__pos[i] = self.__pos[i - 1]

    def draw(self, surface):
        draw.rect(surface, self.__color, (self.__pos[0][0], self.__pos[0][1], GUI.GRID_SIZE, GUI.GRID_SIZE))
