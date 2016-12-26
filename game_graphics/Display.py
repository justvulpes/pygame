"""Display."""

import pygame


class Display:
    """Make a new window with canvas."""

    def __init__(self, window_width, window_height, fps=60):
        """Constructor."""
        pygame.init()
        self.canvas = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()  # To set a limit for fps / time
        self.fps = fps
        self.width = window_width
        self.height = window_height
