
import pygame
import random

pygame.init()

# Constants
SCREEN_SIZE = 500
SNAKE_SIZE = SCREEN_SIZE // 50
UP = 0
LEFT = 1
RIGHT = 2
DOWN = 3

# Other variables and objects
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()
start_pos = (SCREEN_SIZE // 2, SCREEN_SIZE // 2)
body_positions = []
apple_positions = []

# The border around the screen
border = []
for i in range(0, SCREEN_SIZE, SNAKE_SIZE):
    border.append((i, 0))
    border.append((0, i))
    border.append((SCREEN_SIZE - SNAKE_SIZE, i))
    border.append((i, SCREEN_SIZE - SNAKE_SIZE))

# Menu words
pygame.font.init()
font = pygame.font.SysFont('Verdana', 80)
title = font.render("Snake", False, (0, 255, 0))
font = pygame.font.SysFont('Verdana', 50)
game_over_text = font.render("Game Over", False, (255, 255, 255))
font = pygame.font.SysFont('Verdana', 30)
subtitle = font.render("Press enter to start", False, (255, 255, 255))


def menu():
    """Displays the game title and menu"""
    draw_title = True

    while True:
        # Draw the title
        if draw_title:
            pygame.Surface.blit(screen, title, (120, 150))
            pygame.Surface.blit(screen, subtitle, (100, 240))
            draw_title = False

        pygame.display.update()

        # Event handler
        for event in pygame.event.get():
            # Key events
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_RETURN:
                    start()
                    draw_title = True
            # Quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


def game_over():
    """Displays the game over screen then goes badk to the title"""
    screen.fill((0, 0, 0))
    pygame.Surface.blit(screen, game_over_text, (100, 170))
    pygame.display.update()

    milliseconds = 0  # The amt of milliseconds delayed

    # Handle quit event and delay for a little bitß
    while True:
        # Event handler
        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        milliseconds += pygame.time.delay(1)

        if milliseconds >= 2000:
            break


    screen.fill((0, 0, 0))


def start():
    """Sets up and starts the game"""
    global body_positions
    body_positions = [start_pos, (start_pos[0], start_pos[1] + SNAKE_SIZE), (start_pos[0], start_pos[1] + SNAKE_SIZE * 2),
     (start_pos[0], start_pos[1] + SNAKE_SIZE * 3)]
    run()


def run():
    """Runs the main game logic"""
    direction = UP
    apple_positions = [get_rand_pos(), get_rand_pos(), get_rand_pos(), get_rand_pos()]
    score = 0
    global font
    font = pygame.font.SysFont("Verdana", 20)
    score_bar_text = font.render("Score: ", False, (255, 255, 255))
    score_text = font.render(str(score), False, (255, 255, 255))

    # --- Main Loop ---
    while True:
        # Event handler
        for event in pygame.event.get():
            # Key events
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_UP:
                    if direction != DOWN:
                        direction = UP
                if key == pygame.K_LEFT:
                    if direction != RIGHT:
                        direction = LEFT
                if key == pygame.K_DOWN:
                    if direction != UP:
                        direction = DOWN
                if key == pygame.K_RIGHT:
                    if direction != LEFT:
                        direction = RIGHT
            # Quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Move the snake
        for i in range(len(body_positions) - 1, -1, -1):
            # Update the positions
            if i == 0:
                if direction == UP:
                    body_positions[i] = (body_positions[i][0], body_positions[i][1] - SNAKE_SIZE)
                elif direction == LEFT:
                    body_positions[i] = (body_positions[i][0] - SNAKE_SIZE, body_positions[i][1])
                elif direction == DOWN:
                    body_positions[i] = (body_positions[i][0], body_positions[i][1] + SNAKE_SIZE)
                elif direction == RIGHT:
                    body_positions[i] = (body_positions[i][0] + SNAKE_SIZE, body_positions[i][1])
            else:
                body_positions[i] = body_positions[i - 1]

        # Check for collisions with self and border
        if body_positions[0] in body_positions[1:] or body_positions[0] in border:
            game_over()
            break

        # Check for collisions with the apple
        if body_positions[0] in apple_positions:
            # Move the apple
            apple_positions[apple_positions.index(body_positions[0])] = get_rand_pos()

            # Add a new body segment to the snake
            body_positions.append(body_positions[-1])

            # Update the score
            score += 1
            score_text = font.render(str(score), False, (255, 255, 255))

        # Draw the apples
        for pos in apple_positions:
            pygame.draw.rect(screen, (255, 0, 0), (pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))

        # Draw the border
        for pos in border:
            pygame.draw.rect(screen, (0, 0, 255), (pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))

        # Draw the snake
        for pos in body_positions:
            pygame.draw.rect(screen, (0, 255, 0), (pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))

        # Draw the score bar
        pygame.Surface.blit(screen, score_bar_text, (15, 10))
        pygame.Surface.blit(screen, score_text, (85, 10))

        # Update the screen
        pygame.display.update()

        # Set the speed of each frame
        clock.tick(10)


def get_rand_pos():
    return random.randint(2, SCREEN_SIZE // SNAKE_SIZE - 2) * SNAKE_SIZE, random.randint(2, SCREEN_SIZE // SNAKE_SIZE - 2) * SNAKE_SIZE


menu()
