import pygame

from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def draw(self, screen):
        pygame.draw.circle(screen, OBJECT_COLOR, self.position, SHOT_RADIUS, OBJECT_DRAW_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt