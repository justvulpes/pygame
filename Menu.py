"""Menu."""

import pygame
import random
import KeyListener
import Main

print(pygame.font.get_fonts()) # prints a string of all the available fonts


class MenuButton:
    def __init__(self, text, font=random.choice(pygame.font.get_fonts()), font_size=60,
                 font_color=(255, 255, 255), pos_x=0, pos_y=0):
        self.text = text
        self.font = pygame.font.SysFont(font, font_size)
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.font.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def is_mouse_selection(self, pos_x, pos_y):
        posx, posy = (pos_x, pos_y)
        if self.pos_x <= posx <= self.pos_x + self.width and self.pos_y <= posy <= self.pos_y + self.height:
            return True
        return False

    def set_font_color(self, rgb):
        self.font_color = rgb
        self.label = self.font.render(self.text, 1, self.font_color)

    def set_the_font(self, font):
        self.font = pygame.font.SysFont(font, 60)


class Menu:
    def __init__(self, scrn, buttons, bg_color=(192, 192, 192), font=random.choice(pygame.font.get_fonts()), font_size=60):
        self.scrn = scrn  # screen
        self.scr_width = self.scrn.get_rect().width  # width of the screen
        self.scr_height = self.scrn.get_rect().height  # height of the screen
        self.bg_color = bg_color  # background color
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(font, font_size)
        self.buttons = []
        self.clock.tick(60)

        for i, button in enumerate(buttons):  # give buttons
            mbutton = MenuButton(button)
            text_width, text_height = mbutton.width, mbutton.height
            posx = (self.scr_width / 2) - (text_width / 2)
            posy = (self.scr_height / 2) - (len(buttons) * text_height / 2) + (i * text_height)
            mbutton.set_position(posx, posy)
            self.buttons.append(mbutton)

    def running(self):
        while True:
            KeyListener.update()
            self.scrn.fill(self.bg_color)
            pygame.event.get()  # so it wouldn't crash, delete events
            for item in self.buttons:
                item.set_the_font(random.choice(pygame.font.get_fonts()))
                if item.is_mouse_selection(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    item.set_font_color((0, 0, 0))
                else:
                    item.set_font_color((255, 255, 255))

                self.scrn.blit(item.label, item.position)
            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((Main.window_width, Main.window_height), 0, 32)
    menu_buttons = ("Play", "Settings", "Highscores", "Quit")
    pygame.display.set_caption('Game Menu')
    Menu(screen, menu_buttons).running()
