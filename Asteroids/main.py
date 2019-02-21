
import pygame


pygame.init()

screen = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock()

# --- Main Loop ---
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player

    # Update the screen
    pygame.display.update()

    # Set clock speed
    clock.tick(60)
