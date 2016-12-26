import objects.Object
import World
import math
class Projectile(objects.Object.Object):
    def __init__(self, x, y, end_x, end_y, sprite, size=10, speed=1, lifetime=100):
        super().__init__(x,y)
        self.angle = math.atan2(end_y - y, end_x - x)
        self.sprite = sprite
        self.size = size
        self.speed = speed
        self.lifetime = lifetime
        self.xSpeed = self.speed * math.cos(self.angle)
        self.ySpeed = self.speed * math.sin(self.angle)

    def update(self):
        self.lifetime -= 1
        if self.lifetime < 0:
            World.World.objects.remove(self)
        self.move(self.xSpeed, self.ySpeed)

    def render(self, display):
        display.canvas.blit(self.sprite.pic, (self.x - World.World.camera_x - self.sprite.width / 2, self.y - World.World.camera_y - self.sprite.height / 2))

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
