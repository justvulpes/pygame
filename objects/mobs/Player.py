import objects.mobs.Mob
import game_graphics.Sprite
import KeyListener
import World

sprite_down = game_graphics.Sprite.player_down


class Player(objects.mobs.Mob.Mob):
    def __init__(self, x, y):
        super().__init__(x, y)

    def update(self):

        if KeyListener.button_is_pressed(ord("d")):
            self.x += 4
        if KeyListener.button_is_pressed(ord("a")):
            self.x -= 4
        if KeyListener.button_is_pressed(ord("w")):
            self.y -= 4
        if KeyListener.button_is_pressed(ord("s")):
            self.y += 4

    def render(self, display):
        display.canvas.blit(sprite_down.pic, (self.x - World.World.camera_x, self.y - World.World.camera_y))
