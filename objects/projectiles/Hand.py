"""Stone."""

import objects.projectiles.Projectile
import game_graphics.Sprite
import random


class Hand(objects.projectiles.Projectile.Projectile):
    """Class stone."""

    def __init__(self, x, y, end_x, end_y):
        """Constructor."""
        super().__init__(x, y, end_x, end_y, None, size=6, speed=15, lifetime=2)

    def render(self, display):
        pass
