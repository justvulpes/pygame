"""Game state."""
import random
import World
import objects.mobs.Goblin


class GameState:
    """Game state."""

    def __init__(self):
        """Constructor."""
        self.coins = 500
        self.wood = 500
        self.stone = 500
        self.wave = 0
        self.difficulty = 0
        self.survival_time = 0
        self.wave = 0
        self.cool_down = 600

    def save_game(self):
        """Save game."""
        pass

    def update(self):
        """Update."""
        self.cool_down -= 1
        if self.cool_down <= 0:
            self.cool_down = 600
            self.wave += 1

            for i in range(int(5 * (1 + self.wave / 5))):
                World.World.mobs.append(objects.mobs.Goblin.Goblin(random.randint(10, 50) << 5, random.randint(27, 35) << 5))
