"""Stone."""

import objects.projectiles.Projectile
import game_graphics.Sprite
import random


class Hand(objects.projectiles.Projectile.Projectile):
    """Class stone."""

    def __init__(self, x, y, end_x, end_y, owner):
        """Constructor."""
        super().__init__(x, y, end_x, end_y, None, owner, size=6, speed=15, lifetime=2, damage=1.5)

    def render(self, display):
        pass
