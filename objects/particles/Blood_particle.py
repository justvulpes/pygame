import objects.particles.Particle
import World
import random


class BloodParticle(objects.particles.Particle.Particle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (140 + random.randint(0, 100), 30, 30)
        self.width = 2
        self.height = 2
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)
        self.life_time = random.randint(10, 70)

    def render(self, display):
        display.canvas.fill(self.color, (self.x - World.World.camera_x, self.y - World.World.camera_y, self.width, self.height))

    def update(self):
        if not self.removed:
            self.speed_x /= 1.1
            self.speed_y /= 1.1

            self.life_time -= 1

            if not (0 <= int(self.x + self.speed_x) >> 5 < World.World.map_width):
                self.destroy()
                return

            if World.World.tiles_hash[int(self.y) >> 5][int(self.x + self.speed_x) >> 5].solid:
                if not (0 <= int(self.x - self.speed_x) >> 5 < World.World.map_width):
                    self.destroy()
                    return
                self.speed_x = - self.speed_x

            self.x += self.speed_x

            if not (0 <= int(self.y + self.speed_y) >> 5 < World.World.map_height):
                self.destroy()
                return

            if World.World.tiles_hash[int(self.y + self.speed_y) >> 5][int(self.x) >> 5].solid:
                if not (0 <= int(self.y - self.speed_y) >> 5 < World.World.map_height):
                    self.destroy()
                    return
                self.speed_y = - self.speed_y

            self.y += self.speed_y

            if self.life_time <= 0:
                self.destroy()
