"""Projectile."""

import objects.Object
import World
import math


class Projectile(objects.Object.Object):
    """Projectile."""

    def __init__(self, x, y, end_x, end_y, sprite, owner, size=10, speed=1, lifetime=100, high=False, damage=1):
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
        self.owner = owner
        self.damage = damage

    def update(self):
        """Update."""
        self.lifetime -= 1
        if self.lifetime < 0:
            self.destroy()
            return

        self.move(self.xSpeed, self.ySpeed)
        self.check_if_enemy()

    def render(self, display):
        """Render frame."""
        display.canvas.blit(self.sprite.pic, (self.x - World.World.camera_x - self.sprite.width / 2, self.y - World.World.camera_y - self.sprite.height / 2))

    def check_if_enemy(self):
        for y in range(3):
            for x in range(3):
                if 0 <= (int(self.y) >> 5) + y - 1 < World.World.map_height and 0 <= (int(self.x) >> 5) + x - 1 < World.World.map_width:
                    for mob in World.World.tiles_hash[(int(self.y) >> 5) + y - 1][(int(self.x) >> 5) + x - 1].mobs:
                        if mob.race != self.owner.race:
                            if abs(self.x - mob.x) < self.size + mob.size and abs(self.y - mob.y) < self.size + mob.size:
                                mob.do_damage(self)
                                self.removed = True
                                return

    def move(self, x, y):
        """Move."""

        # if abs(x) > 1 or abs(y) > 1:
        #     if x > 0:
        #         x_mark = 1
        #     else:
        #         x_mark = -1
        #
        #     if y > 0:
        #         y_mark = 1
        #     else:
        #         y_mark = -1
        #
        #     while (x != 0 or y != 0) and not self.removed:
        #         if abs(x) > 1 and abs(y) > 1:
        #             x -= x_mark
        #             y -= y_mark
        #             self.move(x_mark, y_mark)
        #         elif abs(x) > 1:
        #             x -= x_mark
        #             self.move(x_mark, y)
        #             y = 0
        #
        #         elif abs(y) > 1:
        #             y -= y_mark
        #             self.move(x, y_mark)
        #             x = 0
        #         else:
        #             self.move(x, y)
        #             x = 0
        #             y = 0
        #     return

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
