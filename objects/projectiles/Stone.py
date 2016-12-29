"""Stone."""

import objects.projectiles.Projectile
import game_graphics.Sprite
import random
import World
import objects.particles.Stone_particle

class Stone(objects.projectiles.Projectile.Projectile):
    """Class stone."""

    def __init__(self, x, y, end_x, end_y, owner, high=False):
        """Constructor."""
        super().__init__(x, y, end_x, end_y, game_graphics.Sprite.stone_projectile, owner, size=8, speed=12 + random.randint(10, 40)/7, lifetime=70, high=high, damage=0.5)

    def destroy(self):
        self.removed = True
        for i in range(random.randint(10, 20)):
            World.World.particles.append(objects.particles.Stone_particle.StoneParticle(self.x, self.y))
