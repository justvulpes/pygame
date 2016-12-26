"""Object."""


class Object:
    """Object."""

    def __init__(self, x, y):
        """Constructor."""
        self.x = x
        self.y = y
        self.removed = False

        self.last_tile = None
        self.current_tile = None

    def update(self):
        """Update."""
        pass

    def render(self, display):
        """Render frame."""
        pass

    def move(self, x, y):
        """Move."""
        pass

    def destroy(self):
        """Destroy."""
        self.removed = True

    def update_tile(self):
        """Update tile."""
        print("Something is wrong.")
        pass
