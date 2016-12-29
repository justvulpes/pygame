
class Building:
    def __init__(self, x, y, max_hp=10):
        self.x = x
        self.y = y
        self.max_hp = max_hp
        self.hp = max_hp
        self.constructed = False

    def destroy(self):
        self.constructed = False

    def build(self):
        self.constructed = True

    def render(self, display):
        pass

    def still_active(self):
        pass

    def update(self):
        pass