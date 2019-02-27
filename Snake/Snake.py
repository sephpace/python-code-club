
import pygame
import random

from Player import Player


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
player = Player((SCREEN_SIZE // 2, SCREEN_SIZE // 2), (0, 255, 0))
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

    # Handle quit event and delay for a little bit
    timer = 0
    while True:
        # Event handler
        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if timer >= 800000:
            break
        timer += 1

    # Clear the screen
    screen.fill((0, 0, 0))


def start():
    """Sets up and starts the game"""
    run()


def run():
    """Runs the main game logic"""
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
                    if player.get_direction() != DOWN:
                        player.set_direction(UP)
                if key == pygame.K_LEFT:
                    if player.get_direction() != RIGHT:
                        player.set_direction(LEFT)
                if key == pygame.K_DOWN:
                    if player.get_direction() != UP:
                        player.set_direction(DOWN)
                if key == pygame.K_RIGHT:
                    if player.get_direction() != LEFT:
                        player.set_direction(RIGHT)
            # Quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Move the snake
        player.move()

        # Check for collisions with self and border
        if player.is_colliding(border + player.get_body_positions()[1:]):
            game_over()
            break

        # Check for collisions with the apple
        if player.is_colliding(apple_positions):
            # Move the apple
            apple_positions[apple_positions.index(player.get_body_positions()[0])] = get_rand_pos()

            # Add a new body segment to the snake
            player.add_segment()

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
        player.draw(screen)

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
