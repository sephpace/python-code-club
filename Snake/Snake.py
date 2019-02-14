
from pygame import draw


class Snake:
    def __init__(self, x, y, size, color, direction=0):
        self.__pos = [(x, y)]
        self.__size = size
        self.__color = color
        self.__direction = direction

    def get_pos(self): return self.__pos[0]

    def set_pos(self, x, y):
        for i in range(len(self.__pos), 0, -1):
            if i == 0:
                self.__pos[0] = (x, y)
            else:
                self.__pos[i] = self.__pos[i - 1]

    def set_direction(self, direction): self.__direction = direction

    def move(self):
        pos = self.__pos
        if self.__direction == 'UP':
            self.set_pos(pos[0][0], pos[0][1] - 1)
        elif self.__direction == 'LEFT':
            self.set_pos(pos[0][0] - 1, pos[0][1])
        elif self.__direction == 'DOWN':
            self.set_pos(pos[0][0], pos[0][1] + 1)
        elif self.__direction == 'RIGHT':
            self.set_pos(pos[0][0] + 1, pos[0][1])

    def draw(self, surface):
        draw.rect(surface, self.__color, (self.__pos[0][0] * self.__size, self.__pos[0][1] * self.__size, self.__size, self.__size))
