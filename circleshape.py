import pygame

from gameobject import GameObject

# Base class for game objects
class CircleShape(GameObject):
    def __init__(self, x, y, radius):
        super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def update(self, dt):
        # sub-classes must override
        pass

    def detect_collision(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius