import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

    def draw(self, screen):
        # sub-classes must override
        pass