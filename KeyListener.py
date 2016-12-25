import pygame
from pygame.locals import *


exit_game = False  # True if user click escape or close the game. Game should be saved and closed if this is True.

key_last = [False for x in range(200)]  # Track which keyboard buttons were in pressed state in previous update. Value index represent button key number "ord()".
key_current = [False for y in range(200)] # Track which keyboard buttons are in pressed state. Value index represent button key number "ord()".

mouseX = -1  # Mouse X coordinate.
mouseY = -1  # Mouse Y coordinate.

mouse_right_button_last = False  # True if mouse right button was in pressed state last update.
mouse_left_button_last = False  # True if mouse left button was in pressed state last update.

mouse_right_button_current = False  # True if mouse right button is currently in pressed state.
mouse_left_button_current = False  # True if mouse left button is currently in pressed state.


def update():
    """Update all information about which buttons are pressed etc."""
    global mouse_right_button_last
    global mouse_left_button_last
    global mouse_right_button_current
    global mouse_left_button_current
    global mouseX
    global mouseY
    global key_last
    global key_current
    global exit_game

    for i in range(200):  # Save latest update info.
        key_last[i] = key_current[i]

    mouse_right_button_last = mouse_right_button_current  # Save latest update info.
    mouse_left_button_last = mouse_left_button_current  # Save latest update info.

    for event in pygame.event.get():  # Get and set new update info.
        print(event)

        if event.type == QUIT:
            exit_game = True

        elif event.type == KEYDOWN:
            key_current[event.key] = True

        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                exit_game = True
            else:
                key_current[event.key] = False

        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_left_button_current = True
            elif event.button == 3:
                mouse_right_button_current = True

        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                mouse_left_button_current = False
            elif event.button == 3:
                mouse_right_button_current = False

        elif event.type == MOUSEMOTION:
            mouseX = event.pos[0]
            mouseY = event.pos[1]


def button_is_pressed(key_number):
    """Return True if button is currently pressed."""
    return key_current[key_number]


def button_was_pressed(key_number):
    """Return True if was pressed right now (if user just now click it)."""
    return key_current[key_number] and not key_last[key_number]


def button_was_released(key_number):
    """Return True if was released right now (if user just now released it)."""
    return key_last[key_number] and not key_current[key_number]

