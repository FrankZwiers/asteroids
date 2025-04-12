import pygame
import random
import os

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    image = pygame.transform.scale(load_background(), (SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroid = pygame.sprite.Group()
    shot = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroid)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shot)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.blit(image, (0, 0))

        # Update groups
        for object in updatable:
            object.update(dt)

        for a in asteroid:
            if a.detect_collision(player):
                print("Game over!")
                exit(1)

            for s in shot:
                if s.detect_collision(a):
                    s.kill()
                    a.split()

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

def load_background():
    index = random.randint(0, len(BACKGROUNDS) -1)
    return pygame.image.load(os.path.join(ROOT_DIR, "assets", "backgrounds", f"{BACKGROUNDS[index]}.jpeg")).convert()

if __name__ == "__main__":
    main()