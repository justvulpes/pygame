"""Particle."""

import objects.Object


class Particle(objects.Object.Object):
    """Particle."""

    def __init__(self, x, y):
        """Constructor."""
        super().__init__(x, y)

    def render(self, display):
        """Render."""
        pass

    def update(self):
        """Update."""
        pass
