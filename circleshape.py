
import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # If containers attribute is set, add to those groups
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def check_collision(self, other):
        if not isinstance(other, CircleShape):
            return False
        # Simple circle collision
        return self.position.distance_to(other.position) < self.radius + other.radius
