import objects.Object
import World

class Mob(objects.Object.Object):
    def __init__(self, x, y, speed=1, size=20):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size

    def update(self):
        pass

    def render(self, display):
        pass

    def move(self, x, y):
        if x != 0 and y != 0:
            self.move(x, 0)
            self.move(0, y)

        if x != 0:
            if int(self.x + x - (self.size >> 1)) >> 5 >= 0 and int(self.x + x + (self.size >> 1)) >> 5 < World.World.map_width:
                if not World.World.tiles_hash[int(self.y + (self.size >> 1)) >> 5][int(self.x + x + (self.size >> 1)) >> 5].solid \
                        and not World.World.tiles_hash[int(self.y + (self.size >> 1)) >> 5][int(self.x + x - (self.size >> 1)) >> 5].solid \
                        and not World.World.tiles_hash[int(self.y - (self.size >> 1)) >> 5][int(self.x + x + (self.size >> 1)) >> 5].solid \
                        and not World.World.tiles_hash[int(self.y - (self.size >> 1)) >> 5][int(self.x + x - (self.size >> 1)) >> 5].solid:
                    self.x += x

        if y != 0:
            if int(self.y + y - (self.size >> 1)) >> 5 >= 0 and int(self.y + y + (self.size >> 1)) >> 5 < World.World.map_width:
                if not World.World.tiles_hash[int(self.y + y + (self.size >> 1)) >> 5][int(self.x + (self.size >> 1)) >> 5].solid \
                        and not World.World.tiles_hash[int(self.y + y - (self.size >> 1)) >> 5][int(self.x + (self.size >> 1)) >> 5].solid \
                        and not World.World.tiles_hash[int(self.y + y + (self.size >> 1)) >> 5][int(self.x - (self.size >> 1)) >> 5].solid \
                        and not World.World.tiles_hash[int(self.y + y - (self.size >> 1)) >> 5][int(self.x - (self.size >> 1)) >> 5].solid:
                    self.y += y