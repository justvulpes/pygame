class Tile:
    def __init__(self, sprite, solid=False, mask=None):

        self.sprite = sprite
        self.mask = mask

        self.solid = solid

        self.mobs = []
        self.projectiles = []




