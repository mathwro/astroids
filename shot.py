from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):
    def __init__(self, x ,y, velocity_x, velocity_y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(velocity_x, velocity_y)

    def draw(self, screen):
      pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt