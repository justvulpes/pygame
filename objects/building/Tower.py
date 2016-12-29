import objects.building.Building
import pygame
import World
import Main
import game_graphics.Sprite
import KeyListener

upgrade_cost = {0: {"coins": 95, "stone": 95, "wood": 95}, 1: {"coins": 90, "stone": 90, "wood": 90}, 2: {"coins": 60, "stone": 60, "wood": 60}, 3: {"coins": 50, "stone": 40, "wood": 80}}
background = pygame.Surface((64, 96), pygame.SRCALPHA)
background.fill((0, 0, 0, 170))


class Tower(objects.building.Building.Building):
    def __init__(self, x, y):
        super().__init__(x, y, max_hp=100)
        self.font = pygame.font.Font("game_graphics\\font.ttf", 22)

        self.font_color = (255, 255, 255)
        self.font_not_enough_color = (200, 20, 20)

        self.lvl = 0
        self.max_hp = 10

        self.coin_price_count = upgrade_cost[self.lvl]["coins"]
        self.stone_price_count = upgrade_cost[self.lvl]["stone"]
        self.wood_price_count = upgrade_cost[self.lvl]["wood"]

        self.coin_enough = False
        self.stone_enough = False
        self.wood_enough = False

        self.tower_text = self.font.render("Tower", 1, self.font_color)

        self.coin_price_text = self.font.render(str(self.coin_price_count), 1, self.font_color if self.coin_enough else self.font_not_enough_color)
        self.stone_price_text = self.font.render(str(self.stone_price_count), 1, self.font_color if self.stone_enough else self.font_not_enough_color)
        self.wood_price_text = self.font.render(str(self.wood_price_count), 1, self.font_color if self.wood_enough else self.font_not_enough_color)

    def destroy(self):
        self.constructed = False

    def build(self):
        self.constructed = True

    def render(self, display):
        display.canvas.blit(background, ((self.x << 5) - World.World.camera_x - 16, (self.y << 5) - World.World.camera_y - 112))

        display.canvas.blit(self.tower_text, ((self.x << 5) - World.World.camera_x + 1, (self.y << 5) - World.World.camera_y - 108))

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

        if ((self.y - 1) << 5) - 16 < World.World.camera_y + KeyListener.mouseY < (self.y << 5) - 16:
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
        pass

    def update(self):
        pass