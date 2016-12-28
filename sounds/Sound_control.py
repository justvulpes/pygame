"""Sound."""
import random

import pygame


class SoundControl:
    """Sound_control."""
    def __init__(self):
        self.menumusic = None
        self.gamemusic = None
        self.click = None
        self.shoot = None
        self.menu_selected_sound = None
        self.muted = False

    def play_menu_music(self):
        """Play the menu music."""
        if not self.muted:
            self.menumusic = pygame.mixer.Sound('sounds\\menumusic.wav')
            self.menumusic.set_volume(0.1)
            self.menumusic.play(-1)  # infinite loop

    def fadeout_menu_music_to_game_music(self, fadeout_time):
        """Fadeout_menu_music."""
        if not self.muted:
            self.menumusic.fadeout(fadeout_time)
            # random music if random.randint(0, 1) == 0:
            if 0 == 0:
                self.gamemusic = pygame.mixer.Sound('sounds\\gamemusic.wav')
                self.gamemusic.set_volume(0.05)
            else:
                self.gamemusic = pygame.mixer.Sound('sounds\\gamemusic2.wav')
                self.gamemusic.set_volume(0.4)
            self.gamemusic.play(-1)  # infinite loop

    def play_click(self):
        """Play click sound."""
        if not self.muted:
            self.click = pygame.mixer.Sound("sounds\\switchweaponsound.wav")
            self.click.set_volume(0.1)
            self.click.play()

    def player_shoot(self):
        """Play shooting sound."""
        if not self.muted:
            self.shoot = pygame.mixer.Sound("sounds\\shoot.wav")
            self.shoot.set_volume(0.4)
            self.shoot.play()

    def menu_selected(self):
        """Play menu selected sound."""
        if not self.muted:
            self.menu_selected_sound = pygame.mixer.Sound("sounds\\menu_selected.wav")
            self.menu_selected_sound.set_volume(0.4)
            self.menu_selected_sound.play()

    def pause_sound(self):
        """Pause all sound."""
        pygame.mixer.pause()
        self.muted = True
        print("Muted")

    def unpause_sound(self):
        """Unpause all sound."""
        pygame.mixer.unpause()
        self.muted = False
        print("Unmuted")
