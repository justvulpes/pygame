"""GOBLIN."""
import objects.mobs.Mob
import game_graphics.Sprite
import World
import random
import sounds.Sound_control


sprite_up = game_graphics.Sprite.goblin_up
sprite_right = game_graphics.Sprite.goblin_right
sprite_down = game_graphics.Sprite.goblin_down
sprite_left = game_graphics.Sprite.goblin_left

sprite_up_step1 = game_graphics.Sprite.goblin_up_step1
sprite_right_step1 = game_graphics.Sprite.goblin_right_step1
sprite_down_step1 = game_graphics.Sprite.goblin_down_step1
sprite_left_step1 = game_graphics.Sprite.goblin_left_step1

sprite_up_step2 = game_graphics.Sprite.goblin_up_step2
sprite_right_step2 = game_graphics.Sprite.goblin_right_step2
sprite_down_step2 = game_graphics.Sprite.goblin_down_step2
sprite_left_step2 = game_graphics.Sprite.goblin_left_step2


class Goblin(objects.mobs.Mob.Mob):
    """Goblin."""

    def __init__(self, x, y, speed=1, size=10):
        """Constructor."""
        super().__init__(x, y, speed, size, race="Goblin", xp_reward=210.5)
        self.current_sprite = sprite_left
        self.direction = 3
        self.animation_counter = 0
        self.moving = False
        self.enemy = None
        self.enemy_building = None
        self.enemy_building_x = 0
        self.enemy_building_y = 0
        self.shooting_cool_down = 30

    def update(self):
        """Update."""
        self.moving = False

        if self.enemy is None and self.enemy_building is None:
            self.check_if_enemy()
            self.check_if_building()
            if self.enemy is None and self.enemy_building is None:
                self.move(0, self.speed)
                self.moving = True
                self.direction = 2
            else:
                self.update()
                return

        elif self.enemy is not None:
            moving_x = 0
            moving_y = 0
            if abs(self.x - self.enemy.x) > 15:
                if self.x - self.enemy.x > 0:
                    moving_x = -self.speed
                else:
                    moving_x = self.speed
            if abs(self.y - self.enemy.y) > 15:
                if self.y - self.enemy.y > 0:
                    moving_y = -self.speed
                else:
                    moving_y = self.speed

            if moving_x != 0 or moving_y != 0:
                self.move(moving_x, moving_y)
                self.moving = True
                if moving_x > 0:
                    self.direction = 1
                elif moving_x < 0:
                    self.direction = 3
                if moving_y > 0:
                    self.direction = 2
                elif moving_y < 0:
                    self.direction = 0

            if self.enemy.hp <= 0:
                self.enemy = None
                self.update()
                return

            self.update_shooting()
            return

        elif self.enemy_building is not None:
            moving_x = 0
            moving_y = 0

            if abs(self.x - self.enemy_building_x) > 16:
                if self.x - self.enemy_building_x > 0:
                    moving_x = -self.speed
                else:
                    moving_x = self.speed

            if abs(self.x - self.enemy_building_y) > 16:
                if self.x - self.enemy_building_y > 0:
                    moving_y = -self.speed
                else:
                    moving_y = self.speed

            if moving_x != 0 or moving_y != 0:
                self.move(moving_x, moving_y)
                self.moving = True
                if moving_x > 0:
                    self.direction = 1
                elif moving_x < 0:
                    self.direction = 3
                if moving_y > 0:
                    self.direction = 2
                elif moving_y < 0:
                    self.direction = 0

            if self.enemy_building.hp <= 0:
                self.enemy_building = None
                self.update()
                return

            self.update_shooting()
            return

    def update_shooting(self):
        self.shooting_cool_down -= 1

        if self.shooting_cool_down <= 0:
            if self.enemy is not None:
                self.shoot(self.enemy.x, self.enemy.y, 2)
                self.shooting_cool_down = 30
            elif self.enemy_building is not None:
                print("shoot")
                self.shoot(self.enemy_building_x, self.enemy_building_y, 2)
                self.shooting_cool_down = 30

    def check_if_enemy(self):
        enemy_list =[]
        for y in range(5):
            for x in range(5):
                if len(World.World.tiles_hash[(self.y >> 5) + y - 2][(self.x >> 5) + x - 2].mobs) != 0:
                    for mob in World.World.tiles_hash[(self.y >> 5) + y - 2][(self.x >> 5) + x - 2].mobs:
                        if mob.race == "Human" and mob.hp > 0:
                            enemy_list.append(mob)

        if len(enemy_list) != 0:
            self.enemy = enemy_list[random.randint(0, len(enemy_list) - 1)]

    def check_if_building(self):
        enemy_list = []
        for y in range(3):
            for x in range(3):
                if World.World.tiles_hash[(self.y >> 5) + y - 1][(self.x >> 5) + x - 1].is_building is not None and World.World.tiles_hash[(self.y >> 5) + y - 1][(self.x >> 5) + x - 1].is_building.hp > 0:
                    enemy_list.append((y, x))

        if len(enemy_list) != 0:
            pos = enemy_list[random.randint(0, len(enemy_list) - 1)]
            self.enemy_building = World.World.tiles_hash[(self.y >> 5) + pos[0] - 1][(self.x >> 5) + pos[1] - 1].building
            self.enemy_building_x = (((self.x >> 5) + pos[1] - 1) << 5) + 16
            self.enemy_building_y = (((self.y >> 5) + pos[0] - 1) << 5) + 16

    def render(self, display):
        """Render frame."""
        self.set_sprite()
        display.canvas.blit(self.current_sprite.pic, (self.x - World.World.camera_x - self.current_sprite.width/2, self.y - World.World.camera_y - self.current_sprite.height/2 - 4))

    def set_sprite(self):
        """Set sprite."""
        if self.moving:
            if self.direction == 0:
                if self.animation_counter >= 8:
                    self.current_sprite = sprite_up_step1
                else:
                    self.current_sprite = sprite_up_step2

            elif self.direction == 1:
                if self.animation_counter >= 8:
                    self.current_sprite = sprite_right_step1
                else:
                    self.current_sprite = sprite_right_step2

            elif self.direction == 2:
                if self.animation_counter >= 8:
                    self.current_sprite = sprite_down_step1
                else:
                    self.current_sprite = sprite_down_step2

            elif self.direction == 3:
                if self.animation_counter >= 8:
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
