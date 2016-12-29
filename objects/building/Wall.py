import objects.building.Building
import game_graphics.Sprite
import pygame
import KeyListener
import World
import game_graphics.Sprite
import Main
import sounds.Sound_control

upgrade_cost = {0: {"coins": 2, "stone": 0, "wood": 5}, 1: {"coins": 5, "stone": 0, "wood": 10}, 2: {"coins": 25, "stone": 30, "wood": 5}, 3: {"coins": 50, "stone": 40, "wood": 0}}
background = pygame.Surface((64, 96), pygame.SRCALPHA)
background.fill((0, 0, 0, 170))


class Wall(objects.building.Building.Building):
    def __init__(self, x, y):
        super().__init__(x, y, max_hp=10)

        self.font = pygame.font.SysFont("IrisUPC", 22)
        self.font_color = (255, 255, 255)
        self.font_not_enough_color = (200, 20, 20)

        self.lvl = 0
        self.max_hp = 10
        self.old_tile_mask = World.World.tiles_hash[y][x].mask
        self.old_tile_sprite = World.World.tiles_hash[y][x].sprite
        self.old_tile_solid = World.World.tiles_hash[y][x].solid
        self.old_tile_high = World.World.tiles_hash[y][x].high

        self.coin_price_count = upgrade_cost[self.lvl]["coins"]
        self.stone_price_count = upgrade_cost[self.lvl]["stone"]
        self.wood_price_count = upgrade_cost[self.lvl]["wood"]

        self.coin_enough = True
        self.stone_enough = True
        self.wood_enough = True

        self.wall_text = self.font.render("Wall", 1, self.font_color)

        self.coin_price_text = self.font.render(str(self.coin_price_count), 1, self.font_color if self.coin_enough else self.font_not_enough_color)
        self.stone_price_text = self.font.render(str(self.stone_price_count), 1, self.font_color if self.stone_enough else self.font_not_enough_color)
        self.wood_price_text = self.font.render(str(self.wood_price_count), 1, self.font_color if self.wood_enough else self.font_not_enough_color)

    def destroy(self):
        if self.constructed:
            self.constructed = False
            self.lvl = 0

            World.World.tiles_hash[self.y][self.x].sprite = self.old_tile_sprite
            World.World.tiles_hash[self.y][self.x].mask = self.old_tile_mask
            World.World.tiles_hash[self.y][self.x].solid = self.old_tile_solid
            World.World.tiles_hash[self.y][self.x].high = self.old_tile_high

    def build(self):
        if Main.gamestate.coins >= upgrade_cost[self.lvl]["coins"] and Main.gamestate.stone >= upgrade_cost[self.lvl]["stone"] and Main.gamestate.wood >= upgrade_cost[self.lvl]["wood"]:
            if not self.constructed:
                if self.no_mobs():
                    self.constructed = True

                    Main.gamestate.coins -= upgrade_cost[self.lvl]["coins"]
                    Main.gamestate.stone -= upgrade_cost[self.lvl]["stone"]
                    Main.gamestate.wood -= upgrade_cost[self.lvl]["wood"]

                    self.max_hp = 10
                    self.hp = 10
                    self.lvl = 1

                    World.World.tiles_hash[self.y][self.x].sprite = game_graphics.Sprite.wooden_wall_level_1
                    World.World.tiles_hash[self.y][self.x].mask = None
                    World.World.tiles_hash[self.y][self.x].solid = True
                    World.World.tiles_hash[self.y][self.x].high = True

                    sounds.Sound_control.SoundControl.upgrade(Main.sc)

            else:
                if self.lvl in upgrade_cost.keys() and self.no_mobs():

                    if self.lvl == 1:
                        Main.gamestate.coins -= upgrade_cost[self.lvl]["coins"]
                        Main.gamestate.stone -= upgrade_cost[self.lvl]["stone"]
                        Main.gamestate.wood -= upgrade_cost[self.lvl]["wood"]

                        self.max_hp = 15
                        self.hp += 5
                        self.lvl = 2

                        World.World.tiles_hash[self.y][self.x].sprite = game_graphics.Sprite.wooden_wall_level_2

                        sounds.Sound_control.SoundControl.upgrade(Main.sc)

                    elif self.lvl == 2:
                        Main.gamestate.coins -= upgrade_cost[self.lvl]["coins"]
                        Main.gamestate.stone -= upgrade_cost[self.lvl]["stone"]
                        Main.gamestate.wood -= upgrade_cost[self.lvl]["wood"]

                        self.max_hp = 30
                        self.hp += 15
                        self.lvl = 3

                        World.World.tiles_hash[self.y][self.x].sprite = game_graphics.Sprite.wooden_wall_level_3
        else:
            print("See peaks mangus viskama teksti \"Not enough resources\"")

    def no_mobs(self):
        if len(World.World.tiles_hash[self.y][self.x].mobs) == 0:
            return True
        else:
            return False

    def level_up(self):
        if self.constructed:
            self.lvl += 1
            self.max_hp += 5
            self.hp += 5


    def render(self, display):
        display.canvas.blit(background, ((self.x << 5) - World.World.camera_x - 16, (self.y << 5) - World.World.camera_y - 112))

        display.canvas.blit(self.wall_text, ((self.x << 5) - World.World.camera_x + 1, (self.y << 5) - World.World.camera_y - 108))

        ###
        if self.coin_price_count != upgrade_cost[self.lvl]["coins"] or (self.wood_enough != (Main.gamestate.wood >= upgrade_cost[self.lvl]["wood"])):
            self.coin_price_count = upgrade_cost[self.lvl]["coins"]
            self.coin_enough = Main.gamestate.coins >= upgrade_cost[self.lvl]["coins"]
            self.coin_price_text = self.font.render(str(self.coin_price_count), 1, self.font_color if self.coin_enough else self.font_not_enough_color)

        if self.stone_price_count != upgrade_cost[self.lvl]["stone"] or (self.stone_enough != (Main.gamestate.stone >= upgrade_cost[self.lvl]["stone"])):
            self.stone_price_count = upgrade_cost[self.lvl]["stone"]
            self.stone_enough = Main.gamestate.stone >= upgrade_cost[self.lvl]["stone"]
            self.stone_price_text = self.font.render(str(self.stone_price_count), 1, self.font_color if self.stone_enough else self.font_not_enough_color)

        if self.wood_price_count != upgrade_cost[self.lvl]["wood"] or (self.wood_enough != (Main.gamestate.wood >= upgrade_cost[self.lvl]["wood"])):
            self.wood_price_count = upgrade_cost[self.lvl]["wood"]
            self.wood_enough = Main.gamestate.wood >= upgrade_cost[self.lvl]["wood"]
            self.wood_price_text = self.font.render(str(self.wood_price_count), 1, self.font_color if self.wood_enough else self.font_not_enough_color)


        display.canvas.blit(game_graphics.Sprite.coin_icon.pic, ((self.x << 5) - World.World.camera_x - 14, (self.y << 5) - World.World.camera_y - 90))

        display.canvas.blit(game_graphics.Sprite.stone_icon.pic, ((self.x << 5) - World.World.camera_x + 8, (self.y << 5) - World.World.camera_y - 90))

        display.canvas.blit(game_graphics.Sprite.tree_icon.pic, ((self.x << 5) - World.World.camera_x + 30, (self.y << 5) - World.World.camera_y - 90))

        ###
        display.canvas.blit(self.coin_price_text, ((self.x << 5) - World.World.camera_x - self.coin_price_text.get_width() / 2 - 6, (self.y << 5) - World.World.camera_y - 70))

        display.canvas.blit(self.stone_price_text, ((self.x << 5) - World.World.camera_x - self.stone_price_text.get_width() / 2 + 16, (self.y << 5) - World.World.camera_y - 70))

        display.canvas.blit(self.wood_price_text, ((self.x << 5) - World.World.camera_x - self.wood_price_text.get_width() / 2 + 38, (self.y << 5) - World.World.camera_y - 70))

        if ((self.y - 1) << 5) - 16 < World.World.camera_y + KeyListener.mouseY < ((self.y) << 5) - 16:
            if (self.x << 5) - 16 < World.World.camera_x + KeyListener.mouseX < ((self.x + 1) << 5) + 16:
                if KeyListener.mouse_left_button_current:
                    if self.constructed:
                        display.canvas.blit(game_graphics.Sprite.upgrade_button_pressed.pic, ((self.x << 5) - World.World.camera_x - 15, (self.y << 5) - World.World.camera_y - 47))
                    else:
                        display.canvas.blit(game_graphics.Sprite.build_button_pressed.pic, ((self.x << 5) - World.World.camera_x - 15, (self.y << 5) - World.World.camera_y - 47))
                    return

        if self.constructed:
            display.canvas.blit(game_graphics.Sprite.upgrade_button.pic, ((self.x << 5) - World.World.camera_x - 15, (self.y << 5) - World.World.camera_y - 47))
        else:
            display.canvas.blit(game_graphics.Sprite.build_button.pic, ((self.x << 5) - World.World.camera_x - 15, (self.y << 5) - World.World.camera_y - 47))


    def still_active(self):
        first_rect = True
        second_rect = True

        if World.World.camera_x + KeyListener.mouseX < self.x << 5 or World.World.camera_x + KeyListener.mouseX > ((self.x + 1) << 5):
            first_rect = False

        if World.World.camera_y + KeyListener.mouseY < self.y << 5 or World.World.camera_y + KeyListener.mouseY > ((self.y + 1) << 5):
            first_rect = False

        if World.World.camera_x + KeyListener.mouseX < (self.x << 5) - 16 or World.World.camera_x + KeyListener.mouseX > ((self.x + 1) << 5) + 16:
            second_rect = False

        if World.World.camera_y + KeyListener.mouseY < ((self.y - 3) << 5) - 16 or World.World.camera_y + KeyListener.mouseY > (self.y << 5):
            second_rect = False

        return first_rect or second_rect

    def update(self):
        if ((self.y - 1) << 5) - 16 < World.World.camera_y + KeyListener.mouseY < ((self.y) << 5) - 16:
            if (self.x << 5) - 16 < World.World.camera_x + KeyListener.mouseX < ((self.x + 1) << 5) + 16:
                if KeyListener.mouse_left_button_was_released():
                    self.build()
