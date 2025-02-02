import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers
    Asteroid.containers = [updatables, drawables, asteroids]
    AsteroidField.containers = [updatables]
    Player.containers = [updatables, drawables]
    Shot.containers = [updatables, drawables, shots]

    # Initialize
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # font object
    font = pygame.font.Font(None, 76)
    game_over = font.render("Game Over", True, "white")
    text_rect = game_over.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    # fade screen
    fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade.fill("black")

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

        for asteroid in asteroids:
            if player.CollisionCheck(asteroid):
                print("Game over!")
                screen.blit(game_over, text_rect)
                pygame.display.flip()
                for alpha in range(0, 255, 5):
                    fade.set_alpha(alpha)
                    screen.blit(fade, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(50)
                pygame.time.delay(1500)
                pygame.quit()
                return

        # Clear the screen
        screen.fill("black")

        # Draw the player
        for drawable in drawables:
            drawable.draw(screen)

        # Flip the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
