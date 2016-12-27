"""Player stats."""


class PlayerStats:
    """Playerstats."""

    def __init__(self):
        """Constructor."""
        self.money = 5000000000
        self.fortress_max_health = 100
        self.fortress_health = 100
        self.gunman_amount = 0
        self.repair_man_amount = 0
        self.tower_cost = 500
        self.gunman_cost = 300
        self.repair_man_cost = 750
        self.repair_fortress_cost = 100

    def get_amount_gunman(self):
        """Get the amount of current gunman."""
        return self.gunman_amount

    def get_amount_repair_man(self):
        """Get the amount of current repair man."""
        return self.repair_man_amount

    def get_money(self):
        """Get the amount of current money."""
        return self.money

    def get_fortress_max_health(self):
        """Get the max health of fortress."""
        return self.fortress_max_health

    def get_fortress_health(self):
        """Get the current health of fortress."""
        return self.fortress_health

    def damage_fortress(self, damage_amount):
        """Fortress gets damaged."""
        self.fortress_health -= damage_amount

    def buy_gunman(self):
        """Buy a gunman."""
        if self.money - self.gunman_cost >= 0:
            self.money -= self.gunman_cost
            self.gunman_cost += 50
            self.gunman_amount += 1

    def buy_repair_man(self):
        """Buy a repair man."""
        if self.money - self.repair_man_cost >= 0:
            self.money -= self.repair_man_cost
            self.repair_man_cost += 250
            self.repair_man_amount += 1

    def buy_repair_fortress(self):
        """Buy - repair fortress."""
        if self.money - self.repair_fortress_cost >= 0:
            self.money -= self.repair_fortress_cost
        # start repairing every x game tick

    def buy_tower(self):
        """Buy a tower."""
        if self.money - self.tower_cost >= 0:
            self.money -= self.tower_cost
            self.tower_cost *= 3
        # add a tower
