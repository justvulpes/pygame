"""Menu."""
import PIL
import pygame
import random
import sys

from PIL import Image
from PIL import ImageFilter
import sounds.Sound_control
import KeyListener
import Main

inMenu = True
default_difficulty = "Noob"


class MenuButton:
    """Menu button."""
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
        """Set position."""
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def selected(self, mouse_pos_x, mouse_pos_y):
        """Selected."""
        m_posx, m_posy = (mouse_pos_x, mouse_pos_y)
        return self.pos_x <= m_posx <= self.pos_x + self.width and self.pos_y <= m_posy <= self.pos_y + self.height

    def set_font_color(self, rgb):
        """Set font color."""
        self.label = self.font.render(self.text, 1, rgb)

    def set_the_font(self, font, size):
        """Set the font."""
        self.font = pygame.font.SysFont(font, size)


class Menu:
    """Menu."""
    def __init__(self, scrn, buttons, events1, bg_color=(192, 192, 192), font=random.choice(pygame.font.get_fonts()), font_size=60):
        """Constructor."""
        self.scrn = scrn  # screen
        self.events1 = events1
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

    def running(self, surf2=None):
        """Loop running menu."""
        set_once = False
        current_seleceted = 0
        global user_interface
        while inMenu:
            #  surf2.clock.tick(surf2.fps)
            Main.update()
            Main.render(surf2)
            surf2.canvas.blit(pygame.image.frombuffer(Image.frombytes('RGB', (1200, 700), pygame.image.tostring(surf2.canvas, 'RGB')).filter(ImageFilter.GaussianBlur(radius=4)).tobytes(), (1200, 700), "RGB"), (0, 0))
            #  pygame.display.flip()
            # static blurred background
            #  bg = pygame.image.load("game_graphics\\res\\objects\\blurred.png")
            #  self.scrn.blit(bg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in self.buttons:
                        if item.selected(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                            for i in self.events1:
                                if i[0] == item.text:
                                    i[1]()  # run the function that matches the text
            for i, item in enumerate(self.buttons):
                #  item.set_the_font(random.choice(pygame.font.get_fonts()), 70) crazyness
                if item.selected(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    item.set_font_color((0, 0, 0))
                    current_seleceted = i
                    if not set_once:
                        set_once = True
                        #  sounds.Sound_control.SoundControl.menu_selected(Main.sc)  # menu sound (bugged atm)
                else:
                    if current_seleceted == i:
                        set_once = False
                    item.set_font_color((255, 255, 255))
                self.scrn.blit(item.label, item.position)
            pygame.display.flip()


class Settings(Menu):
    """Settings."""

    def __init__(self, scrn, buttons, events1):
        """Constctor."""
        super().__init__(scrn, buttons, events1)
        self.difficulty = default_difficulty  # difficulty by default

    '''
      # once difficulty is implemented
    def set_diff_noob(self):
        """Set difficulty to noob."""
        print("Difficulty set to NOOB.")
        self.difficulty = "Noob"

    def set_diff_advanced(self):
        """Set difficulty to advanved."""
        print("Difficulty set to ADVANCED.")
        self.difficulty = "Advanced"

    def set_diff_imposs(self):
        """Set difficult to imposs."""
        print("Difficulty set to IMPOSSIBLE.")
        self.difficulty = "Impossible"
    '''

    @ staticmethod
    def pause_music():
        """Pause music."""
        sounds.Sound_control.SoundControl.pause_sound(Main.sc)

    @ staticmethod
    def unpause_music():
        """Pause music."""
        sounds.Sound_control.SoundControl.unpause_sound(Main.sc)

    def back_to_menu(self):
        """Back to menu."""
        print("Back")
        mr = MenuRun(self.scrn)
        mr.run(self.scrn, surf=the_surf)


class MenuRun:
    """Menu run."""
    def __init__(self, screen2):
        """Constructor."""
        self.screen = screen2
        self.events = [("Play", self.pressed_play), ("Settings", self.open_settings), ("Highscores", self.pressed_highscores),
                       ("Quit", self.pressed_quit)]
        menu_buttons = ("Mute", "Unmute", "Back")
        self.s = Settings(self.screen, menu_buttons, self.events)
        self.events = [("Play", self.pressed_play), ("Settings", self.open_settings), ("Highscores", self.pressed_highscores),
                       ("Quit", self.pressed_quit), ("Mute", self.s.pause_music), ("Unmute", self.s.unpause_music),
                       ("Back", self.s.back_to_menu)]
        self.s = Settings(self.screen, menu_buttons, self.events)

    def run(self, screen, surf=None):
        """Start the menu."""
        self.screen = screen
        global the_surf
        the_surf = surf
        menu_buttons = ("Play", "Settings", "Highscores", "Quit")
        pygame.display.set_caption('Game Menu')
        Menu(screen, menu_buttons, self.events).running(surf2=surf)

    @ staticmethod
    def pressed_play():
        """Start playing, after play is pressed."""
        global inMenu
        inMenu = False
        print("Play.")

    def open_settings(self):
        """Function to run when settings are opened."""
        print("Open settings.")
        pygame.display.set_caption('Settings')
        self.s.running(surf2=the_surf)

    @ staticmethod
    def pressed_highscores():
        """Function to run when highscores is opened."""
        print("Open highscores.")

    @ staticmethod
    def pressed_quit():
        """Quit the game."""
        print("Quit.")
        sounds.Sound_control.SoundControl.unpause_sound()
        sys.exit()
