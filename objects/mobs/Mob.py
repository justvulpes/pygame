"""Mob."""
import Menu
import objects.Object
import World
import objects.projectiles.Stone
import objects.projectiles.Hand
import KeyListener


class Mob(objects.Object.Object):
    """Mob."""

    def __init__(self, x, y, speed=1, size=20):
        """Constructor."""
        super().__init__(x, y)
        self.speed = speed
        self.size = size
        self.hp = 99
        self.max_hp = 99
        self.xp = 11
        self.lvl = 1

    def update(self):
        """Update."""
        pass

    def render(self, display):
        """Render frame."""
        pass

    def move(self, x, y):
        """Move."""
        if not Menu.inMenu and self.current_tile is not None:
            if self.current_tile.slow:
                x, y = x * 2, y * 2

        if x != 0:
            if int(self.x + x - (self.size >> 1)) >> 5 >= 0 and int(self.x + x + (self.size >> 1)) >> 5 < World.World.map_width:
                if not World.World.tiles_hash[int(self.y + (self.size >> 1)) >> 5][int(self.x + x + (self.size >> 1)) >> 5].solid \
                        and not World.World.tiles_hash[int(self.y + (self.size >> 1)) >> 5][int(self.x + x - (self.size >> 1)) >> 5].solid \
                        and not World.World.tiles_hash[int(self.y - (self.size >> 1)) >> 5][int(self.x + x + (self.size >> 1)) >> 5].solid \
                        and not World.World.tiles_hash[int(self.y - (self.size >> 1)) >> 5][int(self.x + x - (self.size >> 1)) >> 5].solid:
                    self.x += x

        if y != 0:
            if int(self.y + y - (self.size >> 1)) >> 5 >= 0 and int(self.y + y + (self.size >> 1)) >> 5 < World.World.map_height:
                if not World.World.tiles_hash[int(self.y + y + (self.size >> 1)) >> 5][int(self.x + (self.size >> 1)) >> 5].solid \
                        and not World.World.tiles_hash[int(self.y + y - (self.size >> 1)) >> 5][int(self.x + (self.size >> 1)) >> 5].solid \
                        and not World.World.tiles_hash[int(self.y + y + (self.size >> 1)) >> 5][int(self.x - (self.size >> 1)) >> 5].solid \
                        and not World.World.tiles_hash[int(self.y + y - (self.size >> 1)) >> 5][int(self.x - (self.size >> 1)) >> 5].solid:
                    self.y += y

    def shoot(self, particle_type):
        if particle_type == 1:
            World.World.projectiles.append(objects.projectiles.Stone.Stone(self.x, self.y, World.World.camera_x + KeyListener.mouseX, World.World.camera_y + KeyListener.mouseY))
        elif particle_type == 2:
            World.World.projectiles.append(objects.projectiles.Hand.Hand(self.x, self.y, World.World.camera_x + KeyListener.mouseX, World.World.camera_y + KeyListener.mouseY))

    def update_tile(self):

        if not self.removed:
            self.last_tile = self.current_tile

            self.current_tile = World.World.tiles_hash[int(self.y) >> 5][int(self.x) >> 5]

            if self.current_tile != self.last_tile:
                if self.last_tile is not None:
                    self.last_tile.mobs.remove(self)
                self.current_tile.mobs.append(self)

    def check_level_up(self):
        if self.xp >= (self.lvl * self.lvl + 10) * self.lvl:
            self.xp -= (self.lvl * self.lvl + 10) * self.lvl
            self.lvl += 1
            self.max_hp += 5
            self.hp += 5
