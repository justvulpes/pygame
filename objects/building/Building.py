"""Building."""


class Building:
    """Building."""

    def __init__(self, x, y, max_hp=10):
        """Constructor."""
        self.x = x
        self.y = y
        self.max_hp = max_hp
        self.hp = max_hp
        self.constructed = False

    def destroy(self):
        """Destroy."""
        self.constructed = False

    def build(self):
        """Build."""
        self.constructed = True

    def render(self, display):
        """Render."""
        pass

    def still_active(self):
        """Still active."""
        pass

    def update(self):
        """Update."""
        pass
