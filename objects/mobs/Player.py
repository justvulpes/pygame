import objects.mobs.Mob
import game_graphics.Sprite
import KeyListener
import World

sprite_down = game_graphics.Sprite.player_down
sprite_up = game_graphics.Sprite.player_up
sprite_left = game_graphics.Sprite.player_left
sprite_right = game_graphics.Sprite.player_right



class Player(objects.mobs.Mob.Mob):
    def __init__(self, x, y, speed=1, size=18):
        super().__init__(x, y, speed, size)
        self.current_sprite = sprite_left
    def update(self):

        if KeyListener.button_is_pressed(ord("d")):
            self.move(self.speed,0)
            self.current_sprite = sprite_right
        if KeyListener.button_is_pressed(ord("a")):
            self.move(-self.speed, 0)
            self.current_sprite = sprite_left
        if KeyListener.button_is_pressed(ord("w")):
            self.move(0, -self.speed)
            self.current_sprite = sprite_up
        if KeyListener.button_is_pressed(ord("s")):
            self.move(0, self.speed)
            self.current_sprite = sprite_down

    def render(self, display):
        display.canvas.blit(self.current_sprite.pic, (self.x - World.World.camera_x - self.current_sprite.width/2, self.y - World.World.camera_y - self.current_sprite.height/2 - 4))
