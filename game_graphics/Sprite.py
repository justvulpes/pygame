import pygame


class Sprite:
    def __init__(self, width, height, pic_path):
        self.width = width
        self.height = height
        self.pic = pygame.image.load(pic_path)


grass_sprite = Sprite(32, 32, "game_graphics\\res\\tiles\\grass.png")
stone_sprite = Sprite(32, 32, "game_graphics\\res\\tiles\\stone.png")



player_down = Sprite(16, 27, "game_graphics\\res\\mobs\\player\\man_down.png")
player_up = Sprite(16, 27, "game_graphics\\res\\mobs\\player\\man_up.png")
player_right = Sprite(11, 27, "game_graphics\\res\\mobs\\player\\man_right.png")
player_left = Sprite(11, 27, "game_graphics\\res\\mobs\\player\\man_left.png")

player_down_step1 = Sprite(16, 27, "game_graphics\\res\\mobs\\player\\man_down_step1.png")
player_up_step1 = Sprite(16, 27, "game_graphics\\res\\mobs\\player\\man_up_step1.png")
player_right_step1 = Sprite(11, 27, "game_graphics\\res\\mobs\\player\\man_right_step1.png")
player_left_step1 = Sprite(11, 27, "game_graphics\\res\\mobs\\player\\man_left_step1.png")

player_down_step2 = Sprite(16, 27, "game_graphics\\res\\mobs\\player\\man_down_step2.png")
player_up_step2 = Sprite(16, 27, "game_graphics\\res\\mobs\\player\\man_up_step2.png")
player_right_step2 = Sprite(11, 27, "game_graphics\\res\\mobs\\player\\man_right_step2.png")
player_left_step2 = Sprite(11, 27, "game_graphics\\res\\mobs\\player\\man_left_step2.png")
