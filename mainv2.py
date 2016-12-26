import pygame
import KeyListener
import Menu
import game_graphics.Display
import World
import objects.mobs.Player
import Hud

window_title = "Driven Into the Last Corner"  # Title on top of the frame.
window_width = 1200  # Width of the canvas.
window_height = 700  # Height of the canvas.
fps_fix = 1160

running = True  # while True game will run.

world = World.World()
player = objects.mobs.Player.Player(30 << 5,70 << 5)


def update():
    """Update all."""
    KeyListener.update()
    cameraPos()  # update camera position.
    world.update()


def render(display_obj):
    """Render all visible stuff."""
    display_obj.canvas.fill(int(0x000000))
    world.render(display_obj)
    Hud.render(display_obj)
    if KeyListener.button_is_pressed(ord('v')):
        print("V was pressed.")
        #  pygame.draw.rect(display_obj.canvas, (255, 255, 0), (display_obj.width / 2 - display_obj.width / 8, display_obj.height / 2 - display_obj.height / 8, display_obj.width / 4, display_obj.height / 4))
        s = pygame.Surface((200, 400), pygame.SRCALPHA) # per-pixel alpha
        s.fill((192, 192, 192, 170))  # last value is alpha value, aka transparency of the box
        display_obj.canvas.blit(s, (display_obj.width - display_obj.width / 4.5, display_obj.height - display_obj.height / 1.3))
        #  pygame.display.flip()


cameraPosDoubleX = 0
cameraPosDoubleY = 0


def cameraPos():
    """Update camera position."""
    global cameraPosDoubleX
    global cameraPosDoubleY
    global cameraPosIntX
    global cameraPosIntY

    cameraPosDoubleX += (player.x - (cameraPosDoubleX + window_width/2)) / 20
    cameraPosDoubleY += (player.y - (cameraPosDoubleY + window_height/2)) / 20

    World.World.camera_x = int(cameraPosDoubleX)
    World.World.camera_y = int(cameraPosDoubleY)


def run():
    game_window = game_graphics.Display.Display(window_width, window_height, fps_fix)
    Menu.run(game_window.canvas)

    world.mobs.append(player)

    while running:
        game_window.clock.tick(game_window.fps)
        pygame.display.set_caption(window_title + " | " + "FPS: %i" % game_window.clock.get_fps())

        update()
        render(game_window)

        pygame.display.flip()


if __name__ == "__main__":
    run()


"""Menu."""

import pygame
import random
import Main

# print(pygame.font.get_fonts())  # prints a string of all the available fonts
inMenu = True


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

    def selected(self, mouse_pos_x, mouse_pos_y):
        m_posx, m_posy = (mouse_pos_x, mouse_pos_y)
        return self.pos_x <= m_posx <= self.pos_x + self.width and self.pos_y <= m_posy <= self.pos_y + self.height

    def set_font_color(self, rgb):
        self.label = self.font.render(self.text, 1, rgb)

    def set_the_font(self, font, size):
        self.font = pygame.font.SysFont(font, size)


class Menu:
    def __init__(self, scrn, buttons, events1, bg_color=(192, 192, 192), font=random.choice(pygame.font.get_fonts()), font_size=60):
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

    def running(self):
        while inMenu:
            self.scrn.fill(self.bg_color)
            for event in pygame.event.get():  # so it wouldn't crash, delete events
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in self.buttons:
                        if item.selected(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                            for i in events:
                                if i[0] == item.text:
                                    i[1]()  # run the function that matches the text
            for item in self.buttons:
                #  item.set_the_font(random.choice(pygame.font.get_fonts()), 70) crazyness
                if item.selected(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    item.set_font_color((0, 0, 0))
                else:
                    item.set_font_color((255, 255, 255))

                self.scrn.blit(item.label, item.position)
            pygame.display.flip()


def run(screen):
    screen = screen
    menu_buttons = ("Play", "Settings", "Highscores", "Quit")
    pygame.display.set_caption('Game Menu')

    Menu(screen, menu_buttons, events).running()


def pressed_play():
    global inMenu
    inMenu = False
    print("Play.")


def open_settings():
    print("Open settings.")


def pressed_highscores():
    print("Open highscores.")


def pressed_quit():
    print("Quit.")


events = [("Play", pressed_play), ("Settings", open_settings), ("Highscores", pressed_highscores), ("Quit", pressed_quit)]