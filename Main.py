"""Main."""
import random

import pygame
import sys

import KeyListener
import game_graphics.Display
import game_graphics.UI.UI
import Menu
import World
import objects.mobs.Player
import objects.mobs.Worker_man
import objects.mobs.Goblin
import game_state.GameState
import game_graphics.UI
import sounds.Sound_control
import Menu_world

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)  # preset the mixer init arguments

window_title = "Driven Into the Last Corner"  # Title on top of the frame.
window_width = 1200  # Width of the canvas.
window_height = 700  # Height of the canvas.
fps_fix = 160

running = True  # while True game will run.


sc = sounds.Sound_control.SoundControl()
player = objects.mobs.Player.Player(30 << 5, 70 << 5)
menu_ghost = objects.mobs.Player.Player(30 << 5, 70 << 5)
world = World.World()
menu_world = Menu_world.MenuWorld()
gamestate = game_state.GameState.GameState()

worker_man = objects.mobs.Worker_man.Worker(37 << 5, 70 << 5, 0, [1456, 2162])   # first wood
worker_man2 = objects.mobs.Worker_man.Worker(37 << 5, 70 << 5, 0, [1456, 2162])   # second wood
worker_man3 = objects.mobs.Worker_man.Worker(27 << 5, 70 << 5, 1, [496, 2194])   # first stone

user_interface = None


def update():
    """Update all."""
    if Menu.inMenu:
        menu_world.update()
    else:
        KeyListener.update()
        world.update()
        gamestate.update()
        user_interface.update()
    cameraPos()  # update camera position.

    if KeyListener.exit_game is True:
        sys.exit()


def render(display_obj):
    """Render all visible stuff."""
    if Menu.inMenu:
        menu_world.render(display_obj)
    else:
        display_obj.canvas.fill(int(0x609CB0))
        world.render(display_obj)
        user_interface.render(display_obj)
        #  print(KeyListener.mouseX + World.World.camera_x, World.World.camera_y + KeyListener.mouseY)


cameraPosDoubleX = (menu_ghost.x - (window_width / 2))
cameraPosDoubleY = (menu_ghost.y - (window_height / 2))


def cameraPos():
    """Update camera position."""
    global cameraPosDoubleX
    global cameraPosDoubleY

    if Menu.inMenu:
        cameraPosDoubleY -= 1  # speed of menu camera up movement
        Menu_world.MenuWorld.camera_x = int(cameraPosDoubleX)
        Menu_world.MenuWorld.camera_y = int(cameraPosDoubleY)
    else:
        cameraPosDoubleX += ((player.x + player.camera_shift_x) - (cameraPosDoubleX + window_width / 2)) / 20
        cameraPosDoubleY += ((player.y + player.camera_shift_y) - (cameraPosDoubleY + window_height / 2)) / 20
        World.World.camera_x = int(cameraPosDoubleX)
        World.World.camera_y = int(cameraPosDoubleY)


def run():
    """Run the game."""
    sounds.Sound_control.SoundControl.play_menu_music(sc)

    game_window = game_graphics.Display.Display(window_width, window_height, fps_fix)  # surface
    mr = Menu.MenuRun(game_window.canvas)
    mr.run(game_window.canvas, surf=game_window)

    world.mobs.append(worker_man)
    world.mobs.append(worker_man3)
    world.mobs.append(player)
    world.mobs.append(objects.mobs.Goblin.Goblin(30 << 5, 40 << 5))
    """
    world.mobs.append(objects.mobs.Goblin.Goblin(31 << 5, 40 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(32 << 5, 40 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(33 << 5, 40 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(34 << 5, 40 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(35 << 5, 40 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(36 << 5, 40 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(29 << 5, 40 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(28 << 5, 40 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(27 << 5, 40 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(26 << 5, 40 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(30 << 5, 40 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(31 << 5, 41 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(32 << 5, 42 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(33 << 5, 43 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(34 << 5, 44 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(35 << 5, 45 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(36 << 5, 39 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(29 << 5, 38 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(28 << 5, 37 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(27 << 5, 36 << 5))
    world.mobs.append(objects.mobs.Goblin.Goblin(26 << 5, 35 << 5))
    """



    menu_world.mobs.append(menu_ghost)
    menu_world.player = menu_ghost
    World.player = player
    global user_interface
    user_interface = game_graphics.UI.UI.UI()
    sounds.Sound_control.SoundControl.fadeout_menu_music_to_game_music(sc, 3000)  # fadeout time is in ms

    while running:
        game_window.clock.tick(game_window.fps)
        pygame.display.set_caption(window_title + " | " + "FPS: %i" % game_window.clock.get_fps())
        update()
        render(game_window)
        pygame.display.flip()

if __name__ == "__main__":
    run()
