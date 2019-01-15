
import time
import random
from ExampleMonster import ExampleMonster
from BigFatSlug import BigFatSlug
from Fairy import Fairy


# --- Functions ---
def get_attackable_monsters(monsters, monster):
    """Removes the given monster from the list of monsters and returns the result"""
    attackable_monsters = list(monsters)
    attackable_monsters.pop(attackable_monsters.index(monster))
    return attackable_monsters


def ko_check(monster_list):
    """Checks if a monster in the given list of monsters has zero health or less, and removes them from the list
       if so"""
    for monster in monster_list:
        if monster.health <= 0:
            print(f"{monster.name} got KOed!")
            monsters.pop(monsters.index(monster))


# --- Setup ---
monsters = []

"""Add monsters here"""
monsters.append(ExampleMonster())
monsters.append(BigFatSlug())
monsters.append(Fairy())

# Shuffle the monsters for fairness
random.shuffle(monsters)

# Introduce monsters
num = 0
for monster in monsters:
    num += 1
    intro = f"""
    Challenger #{num}:
        Name:        {monster.name}
        Description: {monster.description}
        Health:      {monster.health}
        Magic:       {monster.magic}
        Speed:       {monster.speed}"""
    print(intro)

input("\nPress enter to begin the match!")
print()

# --- Main loop ---
while len(monsters) > 1:  # Keep going until there is only one monster standing
    for monster in monsters:
        monster.attack_timer += 1
        monster.ability_timer += 1

        # Attack a monster when the attack timer reaches the speed of the monster
        if monster.attack_timer >= 100 - monster.speed:
            # Do the monster's attack
            monster.attack(get_attackable_monsters(monsters, monster))
            ko_check(monsters)
            time.sleep(1)

            # Set the attack_timer to 0
            monster.attack_timer = 0

        # Use an ability when the ability_timer reaches the magic of the monster
        if monster.ability_timer >= 100 - monster.magic:
            # Use the monster's ability
            monster.ability(get_attackable_monsters(monsters, monster))
            ko_check(monsters)
            time.sleep(1)

            # Set ability_timer to 0
            monster.ability_timer = 0

print(f"\nThe winner is {monsters[0].name}!!")
