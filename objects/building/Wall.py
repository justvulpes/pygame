import objects.building.Building
import World
import game_graphics.Sprite

upgrade_cost = {1:{"coins":5, "stone":0, "wood":10}, 2:{"coins":25, "stone":20, "wood":20}, 3:{"coins":50, "stone":40, "wood":0}}


class Wall(objects.building.Building.Building):
    def __init__(self,x,y):
        super().__init__(x,y, hp=10)
        self.lvl = 0
        self.max_hp = 10
        self.old_tile_mask = World.World.tiles_hash[y][x].mask
        self.old_tile_sprite = World.World.tiles_hash[y][x].sprite
        self.old_tile_solid = World.World.tiles_hash[y][x].solid
        self.old_tile_high = World.World.tiles_hash[y][x].high

    def destroy(self):
        if self.constructed:
            self.constructed = False
            self.lvl = 0

            World.World.tiles_hash[self.y][self.x].sprite = World.World.tiles_hash[self.y][self.x].sprite
            World.World.tiles_hash[self.y][self.x].mask = World.World.tiles_hash[self.y][self.x].mask
            World.World.tiles_hash[self.y][self.x].solid = World.World.tiles_hash[self.y][self.x].solid
            World.World.tiles_hash[self.y][self.x].high = World.World.tiles_hash[self.y][self.x].high

    def build(self):
        if not self.constructed:
            if len(World.World.tiles_hash[self.y][self.x].mobs) == 0:
                self.constructed = True
                self.hp = 15
                self.lvl = 1

                World.World.tiles_hash[self.y][self.x].sprite = game_graphics.Sprite.wooden_wall
                World.World.tiles_hash[self.y][self.x].mask = None
                World.World.tiles_hash[self.y][self.x].solid = True
                World.World.tiles_hash[self.y][self.x].high = True

    def level_up(self):
        if self.constructed:
            self.lvl += 1
            self.max_hp += 5
            self.hp += 5

