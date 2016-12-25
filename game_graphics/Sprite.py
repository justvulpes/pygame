import pygame


class Sprite:
    def __init__(self, width, height, pic_path):
        self.width = width
        self.height = height
        self.pic = pygame.image.load(pic_path)


grass_sprite = Sprite(32, 32, "game_graphics\\res\\tiles\\grass.png")
stone_sprite = Sprite(32, 32, "game_graphics\\res\\tiles\\stone.png")

player_down = Sprite(32, 32, "game_graphics\\res\\mobs\\player\\man.png")

print(grass_sprite)