import objects.Object
import World

class Mob(objects.Object.Object):
    def __init__(self, x, y, speed=1):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.speed = speed

    def update(self):
        pass

    def render(self, display):
        pass

    def move(self, x, y):
        if x != 0 and y != 0:
            self.move(x, 0)
            self.move(0, y)

        if x != 0:
            if (self.x + x) >> 5 >= 0 and (self.x + x) >> 5 < World.World.map_width:
                if not World.World.tiles_hash[self.y >> 5][(self.x + x) >> 5].solid:
                    self.x += x

        if y != 0:
            if (self.y + y) >> 5 >= 0 and (self.y + y) >> 5 < World.World.map_width:
                if not World.World.tiles_hash[(self.y + y) >> 5][self.x >> 5].solid:
                    self.y += y