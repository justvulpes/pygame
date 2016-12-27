import pygame


class Reasource_Bar:
    def __init__(self):
        self.background = pygame.Surface((300, 30), pygame.SRCALPHA)
        self.background.fill((10, 10, 10, 170))

    def render(self, display):
        display.canvas.blit(self.background, (20, 20))

    def update(self):
        pass
