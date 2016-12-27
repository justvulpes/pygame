"""Tile."""


class Tile:
    """Tile."""

    def __init__(self, sprite, solid=False, high=False, mask=None, slow=False):
        """Constructor."""

        self.sprite = sprite
        self.mask = mask

        self.solid = solid
        self.high = high
        self.slow = slow

        self.mobs = []
        self.projectiles = []
        self.building = None
