
from Monster import Monster
import random


class ExampleMonster(Monster):
    def __init__(self):
        super(ExampleMonster, self).__init__()
        self.name = "ExampleMonster"
        self.description = "No one knows what the ExampleMonster looks like, but they've heard it beneath their beds."
        self.health = 30
        self.speed = 40
        self.magic = 10

    def attack(self, monsters):
        monster = self.get_random_monster(monsters)
        damage = 10
        print(f"ExampleMonster punched {monster.name} in the face for {damage} damage!")
        monster.health -= damage

    def ability(self, monsters):
        monster = self.get_random_monster(monsters)
        health_sucked = 5
        print(f"ExampleMonster sucked {health_sucked} health points out of {monster.name}!")
        monster.health -= health_sucked
        self.health += health_sucked

    def get_random_monster(self, monsters):
        """Returns a random monster from the given list of monsters (excluding self if found)"""
        while True:
            monster = random.choice(monsters)
            if monster != self:
                return monster


"""
Remaining Points: 0
"""
