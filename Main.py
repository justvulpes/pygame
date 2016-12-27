"""Main."""

import pygame
import sys

import KeyListener
import game_graphics.Display
import game_graphics.UI.UI
import Menu
import World
import objects.mobs.Player
import game_state.Game_State
import game_graphics.UI

pygame.init()

window_title = "Driven Into the Last Corner"  # Title on top of the frame.
window_width = 1200  # Width of the canvas.
window_height = 700  # Height of the canvas.
fps_fix = 199

running = True  # while True game will run.

world = World.World()
gamestate = game_state.Game_State.Game_State()
player = objects.mobs.Player.Player(30 << 5, 70 << 5)

user_interface = None

def update():
    """Update all."""
    KeyListener.update()
    cameraPos()  # update camera position.
    world.update()
    user_interface.update()

    if KeyListener.exit_game is True:
        sys.exit()


def render(display_obj):
    """Render all visible stuff."""
    display_obj.canvas.fill(int(0x000000))
    world.render(display_obj)
    user_interface.render(display_obj)
    #Hud.render(display_obj)


cameraPosDoubleX = 0
cameraPosDoubleY = 0


def cameraPos():
    """Update camera position."""
    global cameraPosDoubleX
    global cameraPosDoubleY

    cameraPosDoubleX += (player.x - (cameraPosDoubleX + window_width/2)) / 20
    cameraPosDoubleY += (player.y - (cameraPosDoubleY + window_height/2)) / 20

    World.World.camera_x = int(cameraPosDoubleX)
    World.World.camera_y = int(cameraPosDoubleY)


def run():
    """Run the game."""
    game_window = game_graphics.Display.Display(window_width, window_height, fps_fix)
    mr = Menu.MenuRun(game_window.canvas)
    mr.run(game_window.canvas)
    world.mobs.append(player)
    global user_interface
    user_interface = game_graphics.UI.UI.UI()

    while running:

        game_window.clock.tick(game_window.fps)
        pygame.display.set_caption(window_title + " | " + "FPS: %i" % game_window.clock.get_fps())

        update()
        render(game_window)

        pygame.display.flip()


if __name__ == "__main__":
    run()
