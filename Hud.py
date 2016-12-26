"""HUD."""
import Menu
import pygame
import Main
from builder_menu import Player_status
p = Player_status.PlayerStats()


def render(screen):

    mhealth = Menu.MenuButton("Money: " + str(p.get_money()), font='curlz', font_size=30)
    mhealth.set_position(20, 20)
    screen.canvas.blit(mhealth.label, mhealth.position)

    mgunman = Menu.MenuButton("Gunman: " + str(p.get_amount_gunman()), font='curlz', font_size=30)
    mgunman.set_position(1000, 50)
    screen.canvas.blit(mgunman.label, mgunman.position)

    mrepairman = Menu.MenuButton("Repair man: " + str(p.get_amount_repair_man()), font='curlz', font_size=30)
    mrepairman.set_position(1000, 80)
    screen.canvas.blit(mrepairman.label, mrepairman.position)

    pygame.draw.rect(screen.canvas, (255, 255, 255), (900, 10, 280, 30), 2)  # healthbar border
    pygame.draw.rect(screen.canvas, (75, 75, 75), (901, 11, int(max(min(p.get_fortress_health() / float(p.get_fortress_max_health()) * 278, 278), 0)), 28))  # healthbar inner rectangle

    p.damage_fortress(0.1)
    p.buy_gunman()
    #s = pygame.Surface((200, 400), pygame.SRCALPHA)  # per-pixel alpha
    #s.fill((192, 192, 192, 170))  # last value is alpha value, aka transparency of the box
    #display_obj.canvas.blit(s, (display_obj.width - display_obj.width / 4.5, display_obj.height - display_obj.height / 1.3))
