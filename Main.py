import pygame
from pygame.locals import *
import KeyListener
import random
from array import array

window_title = "title_"  # Title on top of the frame.
window_width = 900  # Width of the canvas.
window_height = 700  # Height of the canvas.


class Display():
    """Make a new window with canvas."""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((window_width, window_height), DOUBLEBUF | RESIZABLE)
        self.clock = pygame.time.Clock()  # To set a limit for fps / time
        self.fps = 10000


def update():
    KeyListener.update()


def render():
    pass

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



if __name__ == "__main__":
    a = Display()

    a.running = True

    man_pic = pygame.image.load('man.png')
    print(man_pic)
    print(man_pic)


    objects = []

    for i in range(10):
        objects.append(Bong())


    while a.running:


        a.clock.tick(a.fps)
        pygame.display.set_caption(window_title + " | " + "FPS: %i" % a.clock.get_fps())

        a.screen.set_at((random.randint(0, window_width - 1), random.randint(0, window_height - 1)), random.randint(400000, 900000))


        a.screen.fill(int(0x006600))

        for obj in objects:
            obj.move()
            a.screen.blit(man_pic, (obj.x,obj.y))



        pygame.display.flip()



