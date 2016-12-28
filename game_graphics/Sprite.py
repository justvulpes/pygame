"""Sprite."""

import pygame


class Sprite:
    """Sprite."""

    def __init__(self, width, height, pic_path):
        """Constructor."""
        self.width = width
        self.height = height
        self.pic = pygame.image.load(pic_path)

# Tiles
grass = Sprite(32, 32, "game_graphics\\res\\tiles\\grass.png")
stone = Sprite(32, 32, "game_graphics\\res\\tiles\\stone.png")
dirt = Sprite(32, 32, "game_graphics\\res\\tiles\\dirt.png")
sand = Sprite(32, 32, "game_graphics\\res\\tiles\\sand.png")
water = Sprite(32, 32, "game_graphics\\res\\tiles\\water.png")
snow = Sprite(32, 32, "game_graphics\\res\\tiles\\snow.png")
###

# Projectiles
stone_projectile = Sprite(6, 6, "game_graphics\\res\\projectiles\\stone.png")
###


# Player
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
###


# Worker_man
worker_man_down = Sprite(16, 27, "game_graphics\\res\\mobs\\worker_man\\worker_man_down.png")
worker_man_up = Sprite(16, 27, "game_graphics\\res\\mobs\\worker_man\\worker_man_up.png")
worker_man_right = Sprite(11, 27, "game_graphics\\res\\mobs\\worker_man\\worker_man_right.png")
worker_man_left = Sprite(11, 27, "game_graphics\\res\\mobs\\worker_man\\worker_man_left.png")

worker_man_down_step1 = Sprite(16, 27, "game_graphics\\res\\mobs\\worker_man\\worker_man_down_step1.png")
worker_man_up_step1 = Sprite(16, 27, "game_graphics\\res\\mobs\\worker_man\\worker_man_up_step1.png")
worker_man_right_step1 = Sprite(11, 27, "game_graphics\\res\\mobs\\worker_man\\worker_man_right_step1.png")
worker_man_left_step1 = Sprite(11, 27, "game_graphics\\res\\mobs\\worker_man\\worker_man_left_step1.png")

worker_man_down_step2 = Sprite(16, 27, "game_graphics\\res\\mobs\\worker_man\\worker_man_down_step2.png")
worker_man_up_step2 = Sprite(16, 27, "game_graphics\\res\\mobs\\worker_man\\worker_man_up_step2.png")
worker_man_right_step2 = Sprite(11, 27, "game_graphics\\res\\mobs\\worker_man\\worker_man_right_step2.png")
worker_man_left_step2 = Sprite(11, 27, "game_graphics\\res\\mobs\\worker_man\\worker_man_left_step2.png")
###

# Goblin

###


# Icons
coin_icon = Sprite(16, 16, "game_graphics\\res\\icons\\coin_icon.png")
stone_icon = Sprite(16, 16, "game_graphics\\res\\icons\\stone_icon.png")
tree_icon = Sprite(16, 16, "game_graphics\\res\\icons\\tree_icon.png")

hp_icon = Sprite(16, 16, "game_graphics\\res\\icons\\hp_icon.png")
xp_icon = Sprite(16, 16, "game_graphics\\res\\icons\\xp_icon.png")
level_icon = Sprite(16, 16, "game_graphics\\res\\icons\\level_icon.png")

player_icon = Sprite(64, 64, "game_graphics\\res\\icons\\player_icon.png")
player_icon_injured_1 = Sprite(64, 64, "game_graphics\\res\\icons\\player_icon_injured_1.png")
player_icon_injured_2 = Sprite(64, 64, "game_graphics\\res\\icons\\player_icon_injured_2.png")
player_icon_death = Sprite(64, 64, "game_graphics\\res\\icons\\player_icon_death.png")


hand_weapon_icon = Sprite(64, 64, "game_graphics\\res\\icons\\hand_weapon_icon.png")
stone_weapon_icon = Sprite(64, 64, "game_graphics\\res\\icons\\stone_weapon_icon.png")


# Buttons
build_button = Sprite(62, 30, "game_graphics\\res\\buttons\\build_button.png")
upgrade_button = Sprite(62, 30, "game_graphics\\res\\buttons\\upgrade_button.png")
###

# Objects
stone_source = Sprite(32, 32, "game_graphics\\res\\objects\\stone_source.png")
wooden_wall = Sprite(32, 32, "game_graphics\\res\\objects\\wooden_wall.png")
christmas_tree_upper = Sprite(32, 32, "game_graphics\\res\\objects\\christmas_tree_upper.png")
christmas_tree_lower = Sprite(32, 32, "game_graphics\\res\\objects\\christmas_tree_lower.png")

# Tower
tower_1 = Sprite(32, 32, "game_graphics\\res\\objects\\tower\\tower_1.png")
tower_2 = Sprite(32, 32, "game_graphics\\res\\objects\\tower\\tower_2.png")
tower_3 = Sprite(32, 32, "game_graphics\\res\\objects\\tower\\tower_3.png")
tower_4 = Sprite(32, 32, "game_graphics\\res\\objects\\tower\\tower_4.png")
tower_5 = Sprite(32, 32, "game_graphics\\res\\objects\\tower\\tower_5.png")
tower_6 = Sprite(32, 32, "game_graphics\\res\\objects\\tower\\tower_6.png")
tower_7 = Sprite(32, 32, "game_graphics\\res\\objects\\tower\\tower_7.png")
tower_8 = Sprite(32, 32, "game_graphics\\res\\objects\\tower\\tower_8.png")
tower_9 = Sprite(32, 32, "game_graphics\\res\\objects\\tower\\tower_9.png")
tower_10 = Sprite(32, 32, "game_graphics\\res\\objects\\tower\\tower_10.png")
tower_11 = Sprite(32, 32, "game_graphics\\res\\objects\\tower\\tower_11.png")
tower_12 = Sprite(32, 32, "game_graphics\\res\\objects\\tower\\tower_12.png")
###

# Map
map = Sprite(40, 20, "game_graphics\\res\\map\\map.png")
