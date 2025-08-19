
import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # Only split if not at minimum size
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # Split into two with random angle offset
            angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            radius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, radius)
            a1.velocity = v1 * 1.2
            a2 = Asteroid(self.position.x, self.position.y, radius)
            a2.velocity = v2 * 1.2



