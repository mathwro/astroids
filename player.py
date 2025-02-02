from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from circleshape import CircleShape
from shot import Shot
import pygame

class Player(CircleShape):
    def __init__(self, x ,y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown_timer = 0

    # in the player class
    def triangle(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
      a = self.position + forward * self.radius
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right
      return [a, b, c]
    
    def draw(self, screen):
      pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
      self.rotation += dt * PLAYER_TURN_SPEED

    def move(self, dt):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
      if self.cooldown_timer > 0:
        self.cooldown_timer -= dt
        if self.cooldown_timer < 0:
          self.cooldown_timer = 0
      keys = pygame.key.get_pressed()
      if keys[pygame.K_a]:
          self.rotate(-abs(dt))
      if keys[pygame.K_d]:
          self.rotate(dt)
      if keys[pygame.K_w]:
          self.move(dt)
      if keys[pygame.K_s]:
          self.move(-abs(dt))
      if keys[pygame.K_SPACE]:
          self.shoot()

    def shoot(self):
      if self.cooldown_timer > 0:
          return
      forward = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
      new_shot = Shot(self.position.x, self.position.y, forward.x, forward.y)
      self.cooldown_timer = PLAYER_SHOOT_COOLDOWN