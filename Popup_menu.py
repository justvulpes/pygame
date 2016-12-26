"""Popup menu."""

import pygame
import KeyListener


def render(display_obj):
    """Render."""
    if KeyListener.button_is_pressed(ord('v')):
        #  pygame.draw.rect(display_obj.canvas, (255, 255, 0), (display_obj.width / 2 - display_obj.width / 8,
        # display_obj.height / 2 - display_obj.height / 8, display_obj.width / 4, display_obj.height / 4))

        s = pygame.Surface((200, 400), pygame.SRCALPHA)  # per-pixel alpha
        s.fill((192, 192, 192, 170))  # last value is alpha value, aka transparency of the box
        display_obj.canvas.blit(s, (display_obj.width - display_obj.width / 4.5, display_obj.height - display_obj.height / 1.3))

        #  pygame.display.flip()
