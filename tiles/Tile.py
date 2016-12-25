class Tile:
    def __init__(self, sprite, mask=None):
        self.sprite = sprite
        self.mask = mask
        self.mobs = []
        self.projectiles = []
