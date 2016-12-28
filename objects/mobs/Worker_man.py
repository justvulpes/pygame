"""Player."""
import Menu
import objects.mobs.Mob
import game_graphics.Sprite
import KeyListener
import World


sprite_up = game_graphics.Sprite.worker_man_up
sprite_right = game_graphics.Sprite.worker_man_right
sprite_down = game_graphics.Sprite.worker_man_down
sprite_left = game_graphics.Sprite.worker_man_left

sprite_up_step1 = game_graphics.Sprite.worker_man_up_step1
sprite_right_step1 = game_graphics.Sprite.worker_man_right_step1
sprite_down_step1 = game_graphics.Sprite.worker_man_down_step1
sprite_left_step1 = game_graphics.Sprite.worker_man_left_step1

sprite_up_step2 = game_graphics.Sprite.worker_man_up_step2
sprite_right_step2 = game_graphics.Sprite.worker_man_right_step2
sprite_down_step2 = game_graphics.Sprite.worker_man_down_step2
sprite_left_step2 = game_graphics.Sprite.worker_man_left_step2


class Worker(objects.mobs.Mob.Mob):
    """Worker."""

    def __init__(self, x, y, speed=1, size=18):
        """Constructor."""
        super().__init__(x, y, speed, size)
        self.current_sprite = sprite_left
        self.direction = 3
        self.animCount = 0
        self.moving = False
        self.x = x
        self.y = y
        self.destination = [1184, 2240]
        self.counter = 0

    def update_destination(self):
        if self.counter == 0:
            self.destination = [1184, 2240]
        elif self.counter == 1:
            self.destination = [1184, 2176]
        elif self.counter == 2:
            self.destination = [1152, 2176]
        elif self.counter == 3:
            self.destination = [1152, 2240]
            self.counter = -1
        self.counter += 1

    def update(self):
        self.moving = False
        #print(self.x, self.y, self.destination)

        if [self.x, self.y] == self.destination:
            self.update_destination()

        if self.x < self.destination[0]:
            self.move(self.speed, 0)
            self.moving = True
            self.direction = 1

        elif self.x > self.destination[0]:
            self.move(-self.speed, 0)
            self.moving = True
            self.direction = 3

        elif self.y > self.destination[1]:
            self.move(0, -self.speed)
            self.moving = True
            self.direction = 0

        elif self.y < self.destination[1]:
            self.move(0, self.speed)
            self.moving = True
            self.direction = 2


    def render(self, display):
        """Render frame."""
        self.set_sprite()
        display.canvas.blit(self.current_sprite.pic, (self.x - World.World.camera_x - self.current_sprite.width/2, self.y - World.World.camera_y - self.current_sprite.height/2 - 4))

    def set_sprite(self):
        """Set sprite."""
        if self.moving:
            if self.direction == 0:
                if self.animCount >= 8:
                    self.current_sprite = sprite_up_step1
                else:
                    self.current_sprite = sprite_up_step2

            elif self.direction == 1:
                if self.animCount >= 8:
                    self.current_sprite = sprite_right_step1
                else:
                    self.current_sprite = sprite_right_step2

            elif self.direction == 2:
                if self.animCount >= 8:
                    self.current_sprite = sprite_down_step1
                else:
                    self.current_sprite = sprite_down_step2

            elif self.direction == 3:
                if self.animCount >= 8:
                    self.current_sprite = sprite_left_step1
                else:
                    self.current_sprite = sprite_left_step2

        else:
            if self.direction == 0:
                self.current_sprite = sprite_up

            elif self.direction == 1:
                self.current_sprite = sprite_right

            elif self.direction == 2:
                self.current_sprite = sprite_down

            elif self.direction == 3:
                self.current_sprite = sprite_left
