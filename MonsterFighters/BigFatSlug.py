
from Monster import Monster
import random

class BigFatSlug(Monster):
    def __init__(self):
        super(BigFatSlug, self).__init__()
        self.name = "Big Fat Slug"
        self.description = "It is what it sounds like.  A big, fat slug!"
        self.health = 50
        self.speed = 5
        self.magic = 10

    def attack(self, monsters):
        monster = self.get_slowest_monster(monsters)
        damage = 25
        print(f"SLUUUURRP!  {self.name} licked {monster.name} for {damage} damage!")
        monster.health -= damage
        print(f"{monster.name} feels violated...")

    def ability(self, monsters):
        print(f"{self.name} ate a bunch of food and got EVEN FATTER!")
        health_added = 15
        speed_taken = 5  # 5 extra points for taking away speed
        self.health += health_added
        self.speed -= speed_taken
        print(f"{self.name}'s health increased by {health_added} but its speed decreased by {speed_taken}")

    def get_slowest_monster(self, monsters):
        """Returns the monster with the lowest speed level"""
        min_speed = 100
        slowest_monster = None
        for monster in monsters:
            if monster.speed < min_speed:
                min_speed = monster.speed
                slowest_monster = monster
        if slowest_monster is not None:
            return slowest_monster
        else:
            return self.get_random_monster(monsters)

    def get_random_monster(self, monsters):
        """Returns a random monster from the given list of monsters (excluding self if found)"""
        while True:
            monster = random.choice(monsters)
            if monster != self:
                return monster

"""
Remaining points: 0
"""
