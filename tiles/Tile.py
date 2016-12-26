"""Tile."""


class Tile:
    """Tile."""

    def __init__(self, sprite, solid=False, high=False, mask=None):
        """Constructor."""

        self.sprite = sprite
        self.mask = mask

        self.solid = solid
        self.high = high
        self.mobs = []
        self.projectiles = []
