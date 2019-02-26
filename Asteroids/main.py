
import math
import pygame


# --- Classes ---
class Player:
    def __init__(self, pos, speed=0, rot=(3 * math.pi / 2), color=(255, 255, 255)):
        self.__points = ()       # The points that make up the player's shape
        self.__pos = pos         # The player's position
        self.__speed = speed     # The speed of player
        self.__rot = rot         # The direction the player is facing
        self.__color = color     # The color of the player
        self.__go_left = False   # Whether the player is turning left or not
        self.__go_right = False  # Whether the player is turning right or not
        self.__direction = rot   # The direction the player is traveling

        # Update the player's position
        self.__update_pos()

    def get_pos(self): return self.__pos

    def get_rot(self): return self.__rot

    def get_speed(self): return self.__speed

    def set_pos(self, pos):
        self.__pos = pos
        self.__update_pos()

    def set_speed(self, speed):
        self.__speed = speed

    def set_rot(self, radians):
        self.__rot = radians
        self.__update_pos()

    def set_left(self, left): self.__go_left = left

    def set_right(self, right): self.__go_right = right

    def move_forward(self):
        player.set_speed(player.get_speed() + 1)
        # TODO: To move forward when UP is pressed, add a unit-vector in the direction of self.__rot to the velocity vector

    def move_backward(self):
        player.set_speed(player.get_speed() - 1)

    def draw(self, surface):
        pygame.draw.polygon(surface, self.__color, self.__points)

    def handle(self):
        # Turn left or right when turning
        if self.__go_left:
            self.set_rot(self.get_rot() - math.pi / 20)
        if self.__go_right:
            self.set_rot(self.get_rot() + math.pi / 20)

        # Move in the correct direction
        self.set_pos((self.__pos[0] + (self.__speed * math.cos(self.__direction)), self.__pos[1] + (self.__speed * math.sin(self.__direction))))

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
            # If a key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move_forward()
                if event.key == pygame.K_DOWN:
                    player.move_backward()
                if event.key == pygame.K_LEFT:
                    player.set_left(True)
                if event.key == pygame.K_RIGHT:
                    player.set_right(True)

            # If a key is released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.set_left(False)
                if event.key == pygame.K_RIGHT:
                    player.set_right(False)

            # Quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Handle the player's movements
        player.handle()

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
