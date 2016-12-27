"""HUD."""

import Menu
import pygame
from game_state import Player_status

p = None
mhealth = None

mgunman = None

mrepairman = None



set_up = False
def render(screen):
    """Render HUD elements to the screen."""
    global p
    global set_up
    global mhealth
    global mgunman
    global mrepairman

    if not set_up:
        p = Player_status.PlayerStats()
        mhealth = Menu.MenuButton("Money: " + str(p.get_money()), font='curlz', font_size=30)
        mhealth.set_position(20, 20)

        mgunman = Menu.MenuButton("Gunman: " + str(p.get_amount_gunman()), font='curlz', font_size=30)
        mgunman.set_position(1000, 50)

        mrepairman = Menu.MenuButton("Repair man: " + str(p.get_amount_repair_man()), font='curlz', font_size=30)
        mrepairman.set_position(1000, 80)
        set_up = True

    screen.canvas.blit(mhealth.label, mhealth.position)


    screen.canvas.blit(mgunman.label, mgunman.position)


    screen.canvas.blit(mrepairman.label, mrepairman.position)

    pygame.draw.rect(screen.canvas, (255, 255, 255), (900, 10, 280, 30), 2)  # healthbar border
    pygame.draw.rect(screen.canvas, (75, 75, 75), (901, 11, int(max(min(p.get_fortress_health() / float(p.get_fortress_max_health()) * 278, 278), 0)), 28))  # healthbar inner rectangle