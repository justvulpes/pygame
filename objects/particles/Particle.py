import objects.Object


class Particle(objects.Object.Object):
    def __init__(self, x, y):
        super().__init__(x, y)

    def render(self, display):
        pass

    def update(self):
        pass