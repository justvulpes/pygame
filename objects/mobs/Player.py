"""Player."""
import Main
import objects.mobs.Mob
import game_graphics.Sprite
import KeyListener
import World
import sounds.Sound_control


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
        super().__init__(x, y, speed, size)
        self.current_sprite = sprite_left
        self.direction = 3
        self.animCount = 0
        self.moving = False
        self.weapon = 1
        self.ammo = 10

    def update(self):
        """Update."""
        self.moving = False

        self.update_weapon()

        self.update_shooting()


        self.update_moving()

    def update_weapon(self):

        if KeyListener.mouse_right_button_was_pressed() or KeyListener.mouse_scrolled_up or KeyListener.mouse_scrolled_down:
            sounds.Sound_control.SoundControl.play_click(Main.sc)
            if self.weapon == 1:
                self.weapon = 2
            elif self.weapon == 2:
                self.weapon = 1

    def update_shooting(self):
        if self.weapon == 1:
            if KeyListener.mouse_left_button_was_pressed():
                sounds.Sound_control.SoundControl.player_shoot(Main.sc)
                self.shoot(1)
        elif self.weapon == 2:
            if KeyListener.mouse_left_button_was_pressed():
                self.shoot(2)

    def update_moving(self):
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
            self.animCount = 0

        else:
            self.animCount += 1
            if self.animCount >= 16:
                self.animCount = 0

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
