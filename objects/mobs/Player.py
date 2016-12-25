import objects.mobs.Mob


class Player(objects.mobs.Mob.Mob):
    def __init__(self, x, y):
        super().__init__(x, y)

    def update(self):
        pass

    def render(self):
        pass
