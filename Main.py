import pygame

import KeyListener
import game_graphics.Display
import Menu

import World
import objects.mobs.Player

window_title = "title_"  # Title on top of the frame.
window_width = 1200  # Width of the canvas.
window_height = 700  # Height of the canvas.
fps_fix = 60

running = True  # while True game will run.

world = World.World()
player = objects.mobs.Player.Player(10,10)


def update():
    """Update all."""
    KeyListener.update()

    cameraPos()  # update camera position.
    player.update()
    world.update()


def render(display_obj):
    """Render all visible stuff."""
    display_obj.canvas.fill(int(0x000000))
    world.render(display_obj)


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

    world.objects.append(player)

    while running:
        game_window.clock.tick(game_window.fps)
        pygame.display.set_caption(window_title + " | " + "FPS: %i" % game_window.clock.get_fps())

        update()
        render(game_window)

        pygame.display.flip()


if __name__ == "__main__":
    run()