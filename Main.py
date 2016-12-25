import pygame
from pygame.locals import *
import KeyListener
import random
import game_graphics.Display
from array import array
import World

window_title = "title_"  # Title on top of the frame.
window_width = 900  # Width of the canvas.
window_height = 700  # Height of the canvas.

running = True

world = World.World()

def update():
    KeyListener.update()
    world.update()


def render(display_obj):
    display_obj.canvas.fill(int(0x006600))
    world.render(display_obj)

class Bong:
    def __init__(self):
        self.x = random.randint(0, window_width)
        self.y = random.randint(0, window_height)
        self.speedx = 1
        self.speedy = 1

    def move(self):
        if self.x > window_width:
            self.speedx = -1
        elif self.x < 0:
            self.speedx = 1

        if self.y > window_height:
            self.speedy = -1
        elif self.y < 0:
            self.speedy = 1

        self.x += self.speedx
        self.y += self.speedy


def run():
    game_window = game_graphics.Display.Display(window_width, window_height)

    man_pic = pygame.image.load('man.png')

    objects = []

    for i in range(10):
        objects.append(Bong())

    while running:
        game_window.clock.tick(game_window.fps)
        pygame.display.set_caption(window_title + " | " + "FPS: %i" % game_window.clock.get_fps())

        update()
        render(game_window)


        for obj in objects:
            obj.move()
            game_window.canvas.blit(man_pic, (obj.x,obj.y))

        pygame.display.flip()


if __name__ == "__main__":
    run()