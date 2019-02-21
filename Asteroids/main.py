
import math
import pygame


# --- Classes ---
class Player:
    def __init__(self, pos, speed=0, rot=(3 * math.pi / 2), color=(255, 255, 255)):
        self.__points = ()
        self.__pos = pos
        self.__speed = speed
        self.__rot = rot
        self.__color = color
        self.__update_pos()

    def get_pos(self): return self.__pos

    def get_rot(self): return self.__rot

    def set_pos(self, pos):
        self.__pos = pos
        self.__update_pos()

    def set_speed(self, speed):
        self.__speed = speed

    def set_rot(self, radians):
        self.__rot = radians
        self.__update_pos()

    def draw(self, surface):
        pygame.draw.polygon(surface, self.__color, self.__points)

    def __update_pos(self):
        self.__points = ((self.__pos[0] + int(5 * math.cos(self.__rot)), self.__pos[1] + int(5 * math.sin(self.__rot))),  # Front
                         (self.__pos[0] - int(10 * math.cos(self.__rot + math.pi / 6)), self.__pos[1] - int(10 * math.sin(self.__rot + math.pi / 6))),  # Right
                         (self.__pos[0] - int(5 * math.cos(self.__rot)), self.__pos[1] - int(5 * math.sin(self.__rot))),  # Back
                         (self.__pos[0] - int(10 * math.cos(self.__rot - math.pi / 6)), self.__pos[1] - int(10 * math.sin(self.__rot - math.pi / 6))),  # Left
                         (self.__pos[0] + int(5 * math.cos(self.__rot)), self.__pos[1] + int(5 * math.sin(self.__rot))))  # Front

# --- Functions ---
def start():
    run()


def run():
    """Main Loop"""
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the player
        player.draw(screen)

        # Update the screen
        pygame.display.update()

        # Set clock speed
        clock.tick(60)


if __name__ == '__main__':
    pygame.init()

    SCREEN_SIZE = 500

    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

    clock = pygame.time.Clock()

    player = Player((SCREEN_SIZE // 2, SCREEN_SIZE // 2))

    start()
