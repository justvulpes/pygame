import objects.projectiles.Projectile
import game_graphics.Sprite
import random

class Stone(objects.projectiles.Projectile.Projectile):
    def __init__(self, x, y, end_x, end_y):
        super().__init__(x, y, end_x, end_y, game_graphics.Sprite.stone_projectile, size=8, speed=12 + random.randint(10,40)/7, lifetime=70)

