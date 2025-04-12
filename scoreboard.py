from gameobject import GameObject
from constants import *

class Scoreboard(GameObject):
    __score: int

    def __init__(self, font):
        super().__init__()
        self.font = font
        self.__score = 0

    def draw(self, screen):
        score_text = self.font.render(f'Score: {self.__score:.0f}', True, OBJECT_COLOR)
        screen.blit(score_text, (10, 10))

    def modify_score(self, modifier: int):
        self.__score += modifier