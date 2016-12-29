"""Projectile."""

import objects.Object
import World
import math


class Projectile(objects.Object.Object):
    """Projectile."""

    def __init__(self, x, y, end_x, end_y, sprite, size=10, speed=1, lifetime=100, high=False):
        """Constructor."""
        super().__init__(x, y)
        self.angle = math.atan2(end_y - y, end_x - x)
        self.sprite = sprite
        self.size = size
        self.speed = speed
        self.lifetime = lifetime
        self.xSpeed = self.speed * math.cos(self.angle)
        self.ySpeed = self.speed * math.sin(self.angle)
        self.high = high

    def update(self):
        """Update."""
        self.lifetime -= 1
        if self.lifetime < 0:
            self.destroy()

        self.move(self.xSpeed, self.ySpeed)

    def render(self, display):
        """Render frame."""
        display.canvas.blit(self.sprite.pic, (self.x - World.World.camera_x - self.sprite.width / 2, self.y - World.World.camera_y - self.sprite.height / 2))

    def move(self, x, y):
        """Move."""

        if int(self.x + x - (self.size >> 1)) >> 5 < 0 or int(self.x + x + (self.size >> 1)) >> 5 >= World.World.map_width:
            self.destroy()
            return

        if int(self.y + y - (self.size >> 1)) >> 5 < 0 or int(self.y + y + (self.size >> 1)) >> 5 >= World.World.map_height:
            self.destroy()
            return

        if self.high:
            self.x += x
            self.y += y
            return

        first_corner = World.World.tiles_hash[int(self.y + y + (self.size >> 1)) >> 5][int(self.x + x + (self.size >> 1)) >> 5]
        second_corner = World.World.tiles_hash[int(self.y + y + (self.size >> 1)) >> 5][int(self.x + x - (self.size >> 1)) >> 5]
        third_corner = World.World.tiles_hash[int(self.y + y - (self.size >> 1)) >> 5][int(self.x + x + (self.size >> 1)) >> 5]
        fourth_corner = World.World.tiles_hash[int(self.y + y - (self.size >> 1)) >> 5][int(self.x + x - (self.size >> 1)) >> 5]

        if first_corner.solid and first_corner.high or second_corner.solid and second_corner.high or third_corner.solid and third_corner.high or fourth_corner.solid and fourth_corner.high:
            self.destroy()
            return
        else:
            self.x += x
            self.y += y

    def destroy(self):
        """Destroy object."""
        self.removed = True

    def update_tile(self):
        """Update tile."""
        if not self.removed:
            self.last_tile = self.current_tile

            self.current_tile = World.World.tiles_hash[int(self.y) >> 5][int(self.x) >> 5]

            if self.current_tile != self.last_tile:
                if self.last_tile is not None:
                    self.last_tile.projectiles.remove(self)
                self.current_tile.projectiles.append(self)
