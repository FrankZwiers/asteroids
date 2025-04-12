import pygame
import random

from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__value = self.__calculate_value()

    def draw(self, screen):
        pygame.draw.circle(screen, OBJECT_COLOR, self.position, self.radius, OBJECT_DRAW_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        velocities = [self.velocity.rotate(angle), self.velocity.rotate(-angle)]
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        for velocity in velocities:
            Asteroid(self.position[0], self.position[1], new_radius).velocity = velocity * ASTEROID_SPLIT_SPEED_UP_FACTOR

    def __calculate_value(self):
        return 5 - self.radius / ASTEROID_MIN_RADIUS

    def get_value(self):
        return self.__value