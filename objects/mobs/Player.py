import objects.mobs.Mob
import game_graphics.Sprite
import KeyListener
import World

sprite_down = game_graphics.Sprite.player_down


class Player(objects.mobs.Mob.Mob):
    def __init__(self, x, y, speed=1):
        super().__init__(x, y, speed)

    def update(self):

        if KeyListener.button_is_pressed(ord("d")):
            self.move(1,0)
        if KeyListener.button_is_pressed(ord("a")):
            self.move(-1, 0)
        if KeyListener.button_is_pressed(ord("w")):
            self.move(0, -1)
        if KeyListener.button_is_pressed(ord("s")):
            self.move(0, 1)

    def render(self, display):
        display.canvas.blit(sprite_down.pic, (self.x - World.World.camera_x - sprite_down.width/2, self.y - World.World.camera_y - sprite_down.height/2))
