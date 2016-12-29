import objects.building.Building
import pygame
import World
import Main
import game_graphics.Sprite
import KeyListener
import sounds.Sound_control

upgrade_cost = {0: {"coins": 95, "stone": 95, "wood": 95}, 1: {"coins": 90, "stone": 90, "wood": 90}, 2: {"coins": 60, "stone": 60, "wood": 60}, 3: {"coins": 50, "stone": 40, "wood": 80}}
background = pygame.Surface((64, 96), pygame.SRCALPHA)
background.fill((0, 0, 0, 170))


class Tower(objects.building.Building.Building):
    """Tower."""

    def __init__(self, x, y):
        """Constructor."""
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
        """Destroy."""
        self.constructed = False

    def build(self):
        """Build."""
        if Main.gamestate.coins >= upgrade_cost[self.lvl]["coins"] and Main.gamestate.stone >= upgrade_cost[self.lvl]["stone"] and Main.gamestate.wood >= upgrade_cost[self.lvl]["wood"]:
            if self.no_mobs():
                if not self.constructed:
                    self.constructed = True
                    self.lvl = 1
                    self.hp = 100
                    self.max_hp = 100

                    Main.gamestate.coins -= upgrade_cost[self.lvl]["coins"]
                    Main.gamestate.stone -= upgrade_cost[self.lvl]["stone"]
                    Main.gamestate.wood -= upgrade_cost[self.lvl]["wood"]

                    World.World.tiles_hash[self.y - 4][self.x - 3].sprite = game_graphics.Sprite.tower_1
                    World.World.tiles_hash[self.y - 4][self.x - 2].sprite = game_graphics.Sprite.tower_2
                    World.World.tiles_hash[self.y - 4][self.x - 1].sprite = game_graphics.Sprite.tower_3
                    World.World.tiles_hash[self.y - 3][self.x - 3].sprite = game_graphics.Sprite.tower_4
                    World.World.tiles_hash[self.y - 3][self.x - 2].sprite = game_graphics.Sprite.tower_5
                    World.World.tiles_hash[self.y - 3][self.x - 1].sprite = game_graphics.Sprite.tower_6
                    World.World.tiles_hash[self.y - 2][self.x - 3].sprite = game_graphics.Sprite.tower_7
                    World.World.tiles_hash[self.y - 2][self.x - 2].sprite = game_graphics.Sprite.tower_8
                    World.World.tiles_hash[self.y - 2][self.x - 1].sprite = game_graphics.Sprite.tower_9
                    World.World.tiles_hash[self.y - 1][self.x - 3].sprite = game_graphics.Sprite.tower_10
                    World.World.tiles_hash[self.y - 1][self.x - 2].sprite = game_graphics.Sprite.tower_11
                    World.World.tiles_hash[self.y - 1][self.x - 1].sprite = game_graphics.Sprite.tower_12

                    World.World.tiles_hash[self.y - 4][self.x - 3].solid = True
                    World.World.tiles_hash[self.y - 4][self.x - 2].solid = True
                    World.World.tiles_hash[self.y - 4][self.x - 1].solid = True
                    World.World.tiles_hash[self.y - 3][self.x - 3].solid = True
                    World.World.tiles_hash[self.y - 3][self.x - 2].solid = False
                    World.World.tiles_hash[self.y - 3][self.x - 1].solid = True
                    World.World.tiles_hash[self.y - 2][self.x - 3].solid = True
                    World.World.tiles_hash[self.y - 2][self.x - 2].solid = False
                    World.World.tiles_hash[self.y - 2][self.x - 1].solid = True
                    World.World.tiles_hash[self.y - 1][self.x - 3].solid = True
                    World.World.tiles_hash[self.y - 1][self.x - 2].solid = False
                    World.World.tiles_hash[self.y - 1][self.x - 1].solid = True

                    World.World.tiles_hash[self.y - 4][self.x - 3].is_building = self
                    World.World.tiles_hash[self.y - 4][self.x - 2].is_building = self
                    World.World.tiles_hash[self.y - 4][self.x - 1].is_building = self
                    World.World.tiles_hash[self.y - 3][self.x - 3].is_building = self
                    World.World.tiles_hash[self.y - 3][self.x - 2].is_building = self
                    World.World.tiles_hash[self.y - 3][self.x - 1].is_building = self
                    World.World.tiles_hash[self.y - 2][self.x - 3].is_building = self
                    World.World.tiles_hash[self.y - 2][self.x - 2].is_building = self
                    World.World.tiles_hash[self.y - 2][self.x - 1].is_building = self
                    World.World.tiles_hash[self.y - 1][self.x - 3].is_building = self
                    World.World.tiles_hash[self.y - 1][self.x - 2].is_building = self
                    World.World.tiles_hash[self.y - 1][self.x - 1].is_building = self

                    World.World.tiles_hash[self.y - 4][self.x - 3].high = True
                    World.World.tiles_hash[self.y - 4][self.x - 2].high = True
                    World.World.tiles_hash[self.y - 4][self.x - 1].high = True
                    World.World.tiles_hash[self.y - 3][self.x - 3].high = True
                    World.World.tiles_hash[self.y - 3][self.x - 2].high = True
                    World.World.tiles_hash[self.y - 3][self.x - 1].high = True
                    World.World.tiles_hash[self.y - 2][self.x - 3].high = True
                    World.World.tiles_hash[self.y - 2][self.x - 2].high = True
                    World.World.tiles_hash[self.y - 2][self.x - 1].high = True
                    World.World.tiles_hash[self.y - 1][self.x - 3].high = True
                    World.World.tiles_hash[self.y - 1][self.x - 2].high = True
                    World.World.tiles_hash[self.y - 1][self.x - 1].high = True

                    World.World.tiles_hash[self.y - 1][self.x - 2].slow = True

                    sounds.Sound_control.SoundControl.upgrade(Main.sc)

    def no_mobs(self):
        """No mobs."""
        for y in range(4):
            for x in range(3):
                if len(World.World.tiles_hash[self.y - y - 1][self.x - x - 1].mobs) != 0:
                    print("Something in the way!")
                    return False
        return True

    def render(self, display):
        """Render."""
        display.canvas.blit(background, ((self.x << 5) - World.World.camera_x - 16, (self.y << 5) - World.World.camera_y - 112))

        display.canvas.blit(self.tower_text, ((self.x << 5) - World.World.camera_x - 3, (self.y << 5) - World.World.camera_y - 108))

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
        """Still active."""
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
        """Update."""
        if ((self.y - 1) << 5) - 16 < World.World.camera_y + KeyListener.mouseY < (self.y << 5) - 16:
            if (self.x << 5) - 16 < World.World.camera_x + KeyListener.mouseX < ((self.x + 1) << 5) + 16:
                if KeyListener.mouse_left_button_was_released():
                    self.build()
