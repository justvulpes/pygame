import objects.Object


class Mob(objects.Object.Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def update(self):
        pass

    def render(self, display):
        pass