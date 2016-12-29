"""Player info bar."""

import pygame
import Main
import game_graphics.Sprite


class PlayerInfoBar:
    """Player info bar."""

    def __init__(self):
        """Constructor."""
        self.font = pygame.font.Font("game_graphics\\font.ttf", 22)

        self.background = pygame.Surface((100, 64), pygame.SRCALPHA)
        self.background.fill((0, 0, 0, 170))

        self.text_color = (255, 255, 255)

        self.player_hp_count = Main.World.player.hp
        self.player_max_hp_count = Main.World.player.max_hp
        self.player_xp_count = Main.World.player.xp
        self.player_level_count = Main.World.player.lvl

        self.player_hp_text = self.font.render(str(self.player_hp_count), 1, self.text_color)
        self.player_xp_text = self.font.render(str(self.player_xp_count), 1, self.text_color)
        self.player_level_text = self.font.render(str(self.player_level_count), 1, self.text_color)

    def render(self, display):
        """Render."""
        if Main.World.player.hp / Main.World.player.max_hp > 0.6:
            display.canvas.blit(game_graphics.Sprite.player_icon.pic, (Main.window_width - 184, 20))
        elif Main.World.player.hp / Main.World.player.max_hp > 0.3:
            display.canvas.blit(game_graphics.Sprite.player_icon_injured_1.pic, (Main.window_width - 184, 20))
        elif Main.World.player.hp / Main.World.player.max_hp > 0:
            display.canvas.blit(game_graphics.Sprite.player_icon_injured_2.pic, (Main.window_width - 184, 20))
        else:
            display.canvas.blit(game_graphics.Sprite.player_icon_death.pic, (Main.window_width - 184, 20))

        display.canvas.blit(self.background, (Main.window_width - 120, 20))

        display.canvas.blit(game_graphics.Sprite.hp_icon.pic, (Main.window_width - 116, 23))
        display.canvas.blit(game_graphics.Sprite.xp_icon.pic, (Main.window_width - 116, 44))
        display.canvas.blit(game_graphics.Sprite.level_icon.pic, (Main.window_width - 116, 65))

        if self.player_hp_count != Main.World.player.hp or self.player_max_hp_count != Main.World.player.max_hp:
            self.player_hp_count = Main.World.player.hp
            self.player_max_hp_count = Main.World.player.max_hp
            self.player_hp_text = self.font.render(str(round(self.player_hp_count, 1)), 1, self.text_color)

        if self.player_xp_count != Main.World.player.xp:
            self.player_xp_count = Main.World.player.xp
            self.player_xp_text = self.font.render(str(round(self.player_xp_count, 1)), 1, self.text_color)

        if self.player_level_count != Main.World.player.lvl:
            self.player_level_count = Main.World.player.lvl
            self.player_level_text = self.font.render(str(self.player_level_count), 1, self.text_color)

        display.canvas.fill((170, 0, 0), ((Main.window_width - 95), 25, 70 * (Main.World.player.hp / Main.World.player.max_hp), 12))
        display.canvas.blit(self.player_hp_text, (Main.window_width - 62 - self.player_hp_text.get_width() / 2, 25))

        display.canvas.fill((100, 0, 160), ((Main.window_width - 95), 46, 70 * Main.World.player.xp / ((Main.World.player.lvl * Main.World.player.lvl + 10) * Main.World.player.lvl), 12))
        display.canvas.blit(self.player_xp_text, (Main.window_width - 62 - self.player_xp_text.get_width() / 2, 46))

        display.canvas.blit(self.player_level_text, (Main.window_width - 97, 67))

    def update(self):
        """Update."""
        pass