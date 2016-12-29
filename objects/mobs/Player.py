"""Player."""
import Main
import objects.mobs.Mob
import game_graphics.Sprite
import KeyListener
import World
import sounds.Sound_control
import objects.projectiles.Stone
import objects.projectiles.Hand

sprite_up = game_graphics.Sprite.player_up
sprite_right = game_graphics.Sprite.player_right
sprite_down = game_graphics.Sprite.player_down
sprite_left = game_graphics.Sprite.player_left

sprite_up_step1 = game_graphics.Sprite.player_up_step1
sprite_right_step1 = game_graphics.Sprite.player_right_step1
sprite_down_step1 = game_graphics.Sprite.player_down_step1
sprite_left_step1 = game_graphics.Sprite.player_left_step1

sprite_up_step2 = game_graphics.Sprite.player_up_step2
sprite_right_step2 = game_graphics.Sprite.player_right_step2
sprite_down_step2 = game_graphics.Sprite.player_down_step2
sprite_left_step2 = game_graphics.Sprite.player_left_step2


class Player(objects.mobs.Mob.Mob):
    """Player."""

    def __init__(self, x, y, speed=1, size=18):
        """Constructor."""
        super().__init__(x, y, speed, size, race="Human")
        self.current_sprite = sprite_left
        self.direction = 3
        self.animation_counter = 0
        self.moving = False
        self.weapon = 1
        self.ammo = 10

        self.camera_shift_x = 0
        self.camera_shift_y = 0

    def update(self):
        """Update."""
        self.moving = False

        self.update_weapon()

        self.update_shooting()

        self.update_camera_tweak()
        self.update_moving()

    def update_camera_tweak(self):
        """Update camera tweak."""
        if self.current_tile is not None and self.current_tile.sprite == game_graphics.Sprite.tower_5:
            self.camera_shift_x = (World.World.camera_x + KeyListener.mouseX - self.x) / 2
            self.camera_shift_y = (World.World.camera_y + KeyListener.mouseY - self.y) / 2

        else:
            self.camera_shift_x = 0
            self.camera_shift_y = 0

    def update_weapon(self):
        """Update weapon."""
        if KeyListener.mouse_right_button_was_pressed() or KeyListener.mouse_scrolled_up or KeyListener.mouse_scrolled_down:
            sounds.Sound_control.SoundControl.play_click(Main.sc)
            if self.weapon == 1:
                self.weapon = 2
            elif self.weapon == 2:
                self.weapon = 1

    def update_shooting(self):
        """Update shooting."""
        if not KeyListener.interface_mode:
            if self.weapon == 1:
                if KeyListener.mouse_left_button_was_pressed():
                    sounds.Sound_control.SoundControl.player_shoot(Main.sc)
                    self.shoot(0, 0, 1)
            elif self.weapon == 2:
                if KeyListener.mouse_left_button_was_pressed():
                    sounds.Sound_control.SoundControl.player_punch(Main.sc)
                    self.shoot(0, 0, 2)

    def update_moving(self):
        """Update moving."""
        if KeyListener.button_is_pressed(ord("a")):
            self.move(-self.speed, 0)
            self.moving = True
            self.direction = 3

        elif KeyListener.button_is_pressed(ord("d")):
            self.move(self.speed, 0)
            self.moving = True
            self.direction = 1

        if KeyListener.button_is_pressed(ord("w")):
            self.move(0, -self.speed)
            self.moving = True
            self.direction = 0

        elif KeyListener.button_is_pressed(ord("s")):
            self.move(0, self.speed)
            self.moving = True
            self.direction = 2

        if not self.moving:
            self.animation_counter = 0

        else:
            self.animation_counter += 1
            if self.animation_counter >= 16:
                self.animation_counter = 0

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

    def shoot(self, x, y, particle_type):
        """Shoot."""
        high = False
        if self.current_tile is not None:
            high = self.current_tile.high

        if particle_type == 1:
            World.World.projectiles.append(objects.projectiles.Stone.Stone(self.x, self.y, World.World.camera_x + KeyListener.mouseX, World.World.camera_y + KeyListener.mouseY, self, high=high))
        elif particle_type == 2:
            World.World.projectiles.append(objects.projectiles.Hand.Hand(self.x, self.y, World.World.camera_x + KeyListener.mouseX, World.World.camera_y + KeyListener.mouseY, self))

    def destroy(self):
        """Destroy."""
        self.x = 30 << 5
        self.y = 70 << 5
