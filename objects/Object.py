import World

class Object:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.removed = False

        self.last_tile = None
        self.current_tile = None

    def update(self):
        pass

    def render(self, display):
        pass

    def move(self, x, y):
        pass

    def destroy(self):
        self.removed = True

    def update_tile(self):
        print("Something is wrong.")
        pass