"""Resource bar."""

import pygame
import game_graphics.Sprite
import Main


class ResourceBar:
    """Resource bar."""

    def __init__(self):
        """Constructor."""
        self.font = pygame.font.Font("game_graphics\\font.ttf", 22)
        self.background = pygame.Surface((70, 20), pygame.SRCALPHA)
        self.background.fill((0, 0, 0, 170))

        self.text_color = (255, 255, 255)

        self.coins_count = Main.gamestate.coins
        self.stone_count = Main.gamestate.stone
        self.wood_count = Main.gamestate.wood

        self.coins_text = self.font.render(str(self.coins_count), 1, self.text_color)
        self.stone_text = self.font.render(str(self.stone_count), 1, self.text_color)
        self.wood_text = self.font.render(str(self.wood_count), 1, self.text_color)

    def render(self, display):
        """Render."""
        display.canvas.blit(self.background, (20, 20))
        display.canvas.blit(self.background, (20, 50))
        display.canvas.blit(self.background, (20, 80))

        display.canvas.blit(game_graphics.Sprite.coin_icon.pic, (22, 22))
        display.canvas.blit(game_graphics.Sprite.stone_icon.pic, (22, 52))
        display.canvas.blit(game_graphics.Sprite.tree_icon.pic, (22, 82))

        if self.coins_count != Main.gamestate.coins:
            self.coins_count = Main.gamestate.coins
            self.coins_text = self.font.render(str(self.coins_count), 1, self.text_color)

        if self.stone_count != Main.gamestate.stone:
            self.stone_count = Main.gamestate.stone
            self.stone_text = self.font.render(str(self.stone_count), 1, self.text_color)

        if self.wood_count != Main.gamestate.wood:
            self.wood_count = Main.gamestate.wood
            self.wood_text = self.font.render(str(self.wood_count), 1, self.text_color)

        display.canvas.blit(self.coins_text, (42, 24))
        display.canvas.blit(self.stone_text, (42, 54))
        display.canvas.blit(self.wood_text, (42, 84))

    def update(self):
        """Update."""
        pass
