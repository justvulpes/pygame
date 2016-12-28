import Main
import pygame
import game_graphics.UI.UI
import game_graphics.Sprite


class WeaponInfo:
    def __init__(self):
        self.font = pygame.font.SysFont(game_graphics.UI.UI.UI.user_interface_font, game_graphics.UI.UI.UI.user_interface_font_size)

        self.background = pygame.Surface((200, 64), pygame.SRCALPHA)
        self.background.fill((0, 0, 0, 170))

        self.text_color = (255, 255, 255)

        self.current_weapon = Main.player.weapon
        self.current_ammo = Main.player.ammo

        self.hand_weapon_text = self.font.render("Weapon: Trump's Big Hand", 1, self.text_color)
        self.stone_weapon_text = self.font.render("Weapon: Regular Stone", 1, self.text_color)

        self.type_melee_text = self.font.render("Type: Melee", 1, self.text_color)
        self.type_range_text = self.font.render("Type: Range", 1, self.text_color)

        self.ammo_text = self.font.render("Ammo:", 1, self.text_color)

        self.stone_ammo_count = Main.player.ammo
        self.stone_ammo_text = self.font.render(str(self.stone_ammo_count), 0, self.text_color)
        self.hand_ammo_text = self.font.render("-", 1, self.text_color)

    def update(self):
        pass

    def render(self, display):
        print(Main.player)
        if Main.player.weapon == 1:
            display.canvas.blit(game_graphics.Sprite.stone_weapon_icon.pic, (Main.window_width/2 - 132, Main.window_height - 84))

        elif Main.player.weapon == 2:
            display.canvas.blit(game_graphics.Sprite.hand_weapon_icon.pic, (Main.window_width / 2 - 132, Main.window_height - 84))

        display.canvas.blit(self.background, (Main.window_width / 2 - 68, Main.window_height - 84))

        if Main.player.weapon == 1:
            display.canvas.blit(self.stone_weapon_text, (Main.window_width / 2 - 64, Main.window_height - 78))
            display.canvas.blit(self.type_range_text, (Main.window_width / 2 - 64, Main.window_height - 58))
            if Main.player.ammo != self.stone_ammo_count:
                self.stone_ammo_count = Main.player.ammo
                self.stone_ammo_text = self.font.render(str(self.stone_ammo_count), 0, self.text_color)
            display.canvas.blit(self.ammo_text, (Main.window_width / 2 - 64, Main.window_height - 38))
            display.canvas.blit(self.stone_ammo_text, (Main.window_width / 2 - 15, Main.window_height - 38))

        elif Main.player.weapon == 2:
            display.canvas.blit(self.hand_weapon_text, (Main.window_width / 2 - 64, Main.window_height - 78))
            display.canvas.blit(self.type_melee_text, (Main.window_width / 2 - 64, Main.window_height - 58))
            display.canvas.blit(self.type_range_text, (Main.window_width / 2 - 64, Main.window_height - 38))
            display.canvas.blit(self.hand_ammo_text, (Main.window_width / 2 - 15, Main.window_height - 38))
