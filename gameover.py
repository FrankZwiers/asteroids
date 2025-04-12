import pygame

from gameobject import GameObject
from constants import *

class GameOver(GameObject):
    def __init__(self, font):
        super().__init__()
        self.__game_over_text_line_1 = font.render("GAME OVER", True, (255,0,0))
        self.__game_over_text_line_2 = font.render("press enter to restart", True, (255,0,0))
        self.__counter = 0

    def draw(self, screen, dt):
        pygame.draw.rect(screen, OBJECT_COLOR, ((SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 - 50), (300, 100)), OBJECT_DRAW_WIDTH)

        if self.__counter < 1:
            screen.blit(self.__game_over_text_line_1, (SCREEN_WIDTH / 2  - self.__game_over_text_line_1.get_width() / 2, SCREEN_HEIGHT / 2 - self.__game_over_text_line_1.get_height() / 2))
            screen.blit(self.__game_over_text_line_2, (SCREEN_WIDTH / 2  - self.__game_over_text_line_2.get_width() / 2, SCREEN_HEIGHT / 2 + self.__game_over_text_line_2.get_height() / 2))

        self.__counter += dt
        if self.__counter > 2:
            self.__counter = 0