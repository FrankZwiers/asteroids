import pygame
import random
import os

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from scoreboard import Scoreboard
from gameover import GameOver
from shot import Shot
from gameoverexception import GameOverException

def main():
    pygame.init()
    pygame.display.set_caption("Asteroids!!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    image = pygame.transform.scale(load_background(), (SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    dt = 0

    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables, shots)
    Scoreboard.containers = (drawables)

    scoreboard = Scoreboard(font)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    gameover = GameOver(font)
    AsteroidField()

    state = "running"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.blit(image, (0, 0))

        try:
            if state == "game_over":
                raise GameOverException

            for updatable in updatables:
                updatable.update(dt)

            for asteroid in asteroids:
                if asteroid.detect_collision(player):
                    state = "game_over"
                    raise GameOverException

                for shot in shots:
                    if shot.detect_collision(asteroid):
                        shot.kill()
                        asteroid.split()
                        scoreboard.modify_score(asteroid.get_value())

            for drawable in drawables:
                drawable.draw(screen)
        except GameOverException:
            gameover.draw(screen, dt)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]:
                for updatable in updatables:
                    updatable.kill()

                AsteroidField()
                player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                scoreboard.reset()
                state = "running"

        pygame.display.flip()
        dt = clock.tick(60) / 1000

def load_background():
    index = random.randint(0, len(BACKGROUNDS) -1)
    return pygame.image.load(os.path.join(ROOT_DIR, "assets", "backgrounds", f"{BACKGROUNDS[index]}.jpeg")).convert()

if __name__ == "__main__":
    main()