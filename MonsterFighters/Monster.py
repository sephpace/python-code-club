
from abc import ABC, abstractmethod


class Monster(ABC):
    def __init__(self):
        self.name = ""
        self.description = ""
        self.health = 0
        self.magic = 0
        self.speed = 0

        self.attack_timer = 0
        self.ability_timer = 0

    @abstractmethod
    def attack(self, monsters):
        """Run when it is this monster's time to attack"""
        pass

    @abstractmethod
    def ability(self, monsters):
        """Run when it is this monster's time to use its ability"""
        pass
