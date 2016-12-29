"""Player."""
import pygame

import Main
import Menu
import objects.mobs.Mob
import game_graphics.Sprite
import KeyListener
import World
import sounds.Sound_control


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

    def __init__(self, x, y, worker_number, spawn, speed=1, size=18):
        """Constructor."""
        super().__init__(x, y, speed, size)
        self.current_sprite = sprite_left
        self.direction = 3
        self.animCount = 0
        self.moving = False
        self.x = x
        self.y = y
        self.destination = spawn
        self.counter = 0
        self.first_pass = True
        self.wait = False
        self.wait_timer = 0
        self.worker_number = worker_number
        self.stone_path = [[496, 2192], [464, 2226], [432, 2224], [495, 2227], [496, 2192]]
        self.wood_path = [[1584, 2162], [1584, 2096], [1616, 2096], [1616, 2129], [1648, 2129], [1652, 2193], [1679, 2193], [1652, 2193],
                       [1648, 2226], [1580, 2227], [1580, 2162], [1580, 2161], [1520, 2223], [1520, 2160], [1580, 2158], [1580, 2290]]

    def update_destination(self):
        if self.worker_number == 0:
            self.destination = self.wood_path[self.counter]
            if self.counter == 0 and not self.first_pass:
                Main.gamestate.wood += 50
                sounds.Sound_control.SoundControl.add_wood(Main.sc)
            if self.counter == len(self.wood_path) - 1:
                self.first_pass = False
                self.counter = -1
            self.counter += 1
        elif self.worker_number == 1:
            self.destination = self.stone_path[self.counter]
            if self.counter == 0 and not self.first_pass:
                Main.gamestate.stone += 20
                sounds.Sound_control.SoundControl.add_stone(Main.sc)
            if self.counter == 2:
                self.wait = True
                self.wait_timer += 1
                if self.wait_timer == 1000:
                    self.wait = False
                    self.wait_timer = 0
            if self.counter == len(self.stone_path) - 1:
                self.first_pass = False
                self.counter = -1
            if not self.wait:
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

        if not self.moving:
            self.animCount = 0

        else:
            self.animCount += 1
            if self.animCount >= 16:
                self.animCount = 0

    def render(self, display):
        """Render frame."""
        self.set_sprite()
        display.canvas.blit(self.current_sprite.pic, (self.x - World.World.camera_x - self.current_sprite.width/2, self.y - World.World.camera_y - self.current_sprite.height/2 - 4))
        if self.counter == 0 and not self.first_pass and self.worker_number == 0 or self.counter == 0 and self.worker_number == 1 and not self.first_pass:
            display.canvas.blit(pygame.font.Font("game_graphics\\font.ttf", 22).render("50", 0, (0, 200, 0)), (self.x - World.World.camera_x - self.current_sprite.width / 2, self.y - World.World.camera_y - self.current_sprite.height - 5))


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
