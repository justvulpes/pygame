
class Building:
    def __init__(self, x, y, hp=10):
        self.x = x
        self.y = y
        self.hp = hp
        self.constructed = False

    def destroy(self):
        self.constructed = False

    def build(self):
        self.constructed = True

    def level_up(self):
        pass

    def render(self, display):
        pass

    def still_active(self):
        pass