
import math
import pygame


# --- Classes ---
class Player:
    def __init__(self, pos, rot=math.pi / 2, color=(255, 255, 255)):
        self.set_pos(pos)
        self.__rot = rot
        self.__color = color
        self.__points = ()

    def set_pos(self, pos):
        self.__points = ((pos[0], pos[1] - 5), (pos[0] + 5, pos[1] + 10), (pos[0], pos[1] + 5), (pos[0] - 5, pos[1] + 10), (pos[0], pos[1] - 5))

    def set_rot(self, rad):
        pass

    def draw(self, surface):
        pygame.draw.polygon(surface, self.__color, self.__points)


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
