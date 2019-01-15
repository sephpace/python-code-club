
from Monster import Monster
import random

class Fairy(Monster):
    def __init__(self):
        super(Fairy, self).__init__()
        self.name = "Fairy"
        self.description = "A tiny, little fairy.  As mischievous as she is pretty."
        self.health = 15
        self.speed = 0
        self.magic = 70

    def attack(self, monsters):
        pass

    def ability(self, monsters):
        monster = self.get_most_magical_monster(monsters)
        damage = 5
        print(f"{self.name} zapped {monster.name} for {damage} damage!")
        magic_drained = 5
        monster.health -= damage
        monster.magic -= magic_drained
        self.magic += magic_drained
        print(f"{self.name} drained {magic_drained} magic from {monster.name}")

    def get_most_magical_monster(self, monsters):
        """Returns the monster with the highest magic level"""
        max_magic = 0
        most_magical_monster = None
        for monster in monsters:
            if monster.magic > max_magic:
                max_magic = monster.magic
                most_magical_monster = monster
        if most_magical_monster is not None:
            return most_magical_monster
        else:
            return self.get_random_monster(monsters)

    def get_random_monster(self, monsters):
        """Returns a random monster from the given list of monsters (excluding self if found)"""
        while True:
            monster = random.choice(monsters)
            if monster != self:
                return monster


"""
Remaining Points: 0
"""
