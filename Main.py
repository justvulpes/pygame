import pygame
import random

import KeyListener
import game_graphics.Display

import World
import objects.mobs.Player

window_title = "title_"  # Title on top of the frame.
window_width = 1200  # Width of the canvas.
window_height = 700  # Height of the canvas.

running = True

world = World.World()
player = objects.mobs.Player.Player(10,10)

def update():
    KeyListener.update()

    player.update()
    world.update()



def render(display_obj):
    display_obj.canvas.fill(int(0x000000))
    world.render(display_obj)


cameraPosIntX = 0
cameraPosIntY = 0

cameraPosDoubleX = 0
cameraPosDoubleY = 0


def cameraPos():
    pass


def run():
    game_window = game_graphics.Display.Display(window_width, window_height)
    world.objects.append(player)

    while running:
        game_window.clock.tick(game_window.fps)
        pygame.display.set_caption(window_title + " | " + "FPS: %i" % game_window.clock.get_fps())

        update()
        render(game_window)




        pygame.display.flip()


if __name__ == "__main__":
    run()