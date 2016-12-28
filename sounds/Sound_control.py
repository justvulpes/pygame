"""Sound."""
import pygame


class SoundControl:
    """Sound_control."""

    def __init__(self):
        """Constructor, set sounds."""
        self.menumusic = pygame.mixer.Sound('sounds\\menumusic.wav')
        self.gamemusic = pygame.mixer.Sound('sounds\\gamemusic.wav')
        self.click = pygame.mixer.Sound("sounds\\switchweaponsound.wav")
        self.shoot = pygame.mixer.Sound("sounds\\shoot.wav")
        self.punch = pygame.mixer.Sound("sounds\\punch1.wav")
        self.menu_selected_sound = pygame.mixer.Sound("sounds\\menu_selected.wav")
        self.upgrade_sound = pygame.mixer.Sound("sounds\\buywithcoins.wav")
        self.muted = False

        self.menumusic.set_volume(0.1)
        self.punch.set_volume(0.1)
        self.gamemusic.set_volume(0.05)
        self.click.set_volume(0.1)
        self.shoot.set_volume(0.4)
        self.menu_selected_sound.set_volume(0.4)
        self.upgrade_sound.set_volume(0.5)

    def play_menu_music(self):
        """Play the menu music."""
        if not self.muted:
            self.menumusic.play(-1)  # infinite loop

    def fadeout_menu_music_to_game_music(self, fadeout_time):
        """Fadeout_menu_music."""
        if not self.muted:
            self.menumusic.fadeout(fadeout_time)
            self.gamemusic.play(-1)  # infinite loop

    def play_click(self):
        """Play click sound."""
        if not self.muted:
            self.click.play()

    def player_shoot(self):
        """Play shooting sound."""
        if not self.muted:
            self.shoot.play()

    def player_punch(self):
        """Play punch sound."""
        if not self.muted:
            self.punch.play()

    def menu_selected(self):
        """Play menu selected sound."""
        if not self.muted:
            self.menu_selected_sound.play()

    def upgrade(self):
        """Upgrade."""
        if not self.muted:
            self.upgrade_sound.play()

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
