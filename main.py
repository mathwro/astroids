import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    timer = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = [updatables, drawables]
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        # Cap the frame rate
        dt = timer.tick(60) / 1000

        # Update the player
        for updatable in updatables:
            updatable.update(dt)

        # Clear the screen
        screen.fill("black")

        # Draw the player
        for drawable in drawables:
            drawable.draw(screen)

        # Flip the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
