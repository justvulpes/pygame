"""Game state."""


class Game_State:
    """Game state."""

    def __init__(self):
        """Constructor."""
        self.coins = 500
        self.wood = 500
        self.stone = 500
        self.wave = 0
        self.difficulty = 0
        self.survival_time = 0

    def save_game(self):
        """Save game."""
        pass
