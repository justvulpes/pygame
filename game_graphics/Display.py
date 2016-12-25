import pygame


class Display():
    """Make a new window with canvas."""
    def __init__(self, window_width, window_height):
        pygame.init()
        self.canvas = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()  # To set a limit for fps / time
        self.fps = 10000
        self.width = window_width
        self.height = window_height