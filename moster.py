"""Documentation."""
from random import choice
from dice import dice


class Monster:
    """Baseline monster class."""
    element = ['Fire', 'Water', 'Air', 'Earth']
    types = ['Dragon', 'Giant', 'Spirit']

    def __init__(self, level):
        self.name = choice(self.element)
        self.level = level
        self.health = {
            'total': dice(self.level, 8),
            'current': 0
        }

    def __str__(self):
        return self.name


if __name__ == '__main__':
    m = Monster(level=1)
    print(m)
