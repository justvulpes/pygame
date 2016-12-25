"""Menu."""

import pygame
import random
import KeyListener
import Main

pygame.init()


#  print(pygame.font.get_fonts()) # prints a string of all the available fonts


class Menu:
    def __init__(self, scrn, buttons, bg_color=(192, 192, 192), font=random.choice(pygame.font.get_fonts()), font_size=60, text_color=(0, 0, 0)):
        self.scrn = scrn  # screen
        self.scr_width = self.scrn.get_rect().width  # width of the screen
        self.scr_height = self.scrn.get_rect().height  # height of the screen
        self.bg_color = bg_color  # background color
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(font, font_size)
        self.buttons = []
        self.clock.tick(60)

        for i, button in enumerate(buttons):  # give buttons
            text = self.font.render(button, 1, text_color)
            text_width, text_height = text.get_rect().width, text.get_rect().height
            posx = (self.scr_width / 2) - (text_width / 2)
            posy = (self.scr_height / 2) - (len(buttons) * text_height / 2) + (i * text_height)
            self.buttons.append([button, text, (posx, posy)])

    def running(self):
        while True:
            #  KeyListener.update()
            #  print(KeyListener.mouseX, KeyListener.mouseY)
            self.scrn.fill(self.bg_color)
            pygame.event.get()  # so it wouldn't crash, delete events
            for name, text, (posx, posy) in self.buttons:
                self.scrn.blit(text, (posx, posy))  # draw a source surface onto this screen
            pygame.display.flip()


if __name__ == "__main__":
    screen = pygame.display.set_mode((Main.window_width, Main.window_height), 0, 32)
    menu_buttons = ("Play", "Settings", "Highscores", "Quit")
    pygame.display.set_caption('Game Menu')
    Menu(screen, menu_buttons).running()
