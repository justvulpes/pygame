import objects.projectiles.Projectile
import game_graphics.Sprite

class Stone(objects.projectiles.Projectile.Projectile):
    def __init__(self, x, y, end_x, end_y):
        super().__init__(x, y, end_x, end_y, game_graphics.Sprite.stone_projectile, size=10, speed=10, lifetime=15)

