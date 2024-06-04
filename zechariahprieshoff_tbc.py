#Zechariah Prieshoff
#May 31st, 2024
#(lab) Turn based combat (imported module)
#Program simulates your classic turn based combat game with random stats and attack chances.

import random

class Character(object):
    def __init__(self, name = "Jin Sakai", health = 10, hitChance = 50, maxDamage = 5, armor = 2):
        self.name = name
        self.health = health
        self.hitChance = self.testInt(hitChance, 0, 100, 50)
        self.maxDamage = max(1, maxDamage)
        self.armor = max(0, armor)

    def testInt(self, value, min=0, max=100, default=0):
        out = default
        if isinstance(value, int):
            if min <= value <= max:
                out = value
            elif value > max:
                print(f"{value} is too large, setting to default {default}")
            else:
                print(f"{value} is too small, setting to default {default}")
        else:
            print(f"{value} is not an int, setting to default {default}")
        return out

    def stats(self):
        print(f"\n{self.name}")
        print("====================")
        print(f"Health:     {self.health}")
        print(f"Hit chance: {self.hitChance}")
        print(f"Max damage: {self.maxDamage}")
        print(f"Armor:      {self.armor}\n")

def fight(character1, character2):
    while character1.health > 0 and character2.health > 0:
        for attacker, defender in [(character1, character2), (character2, character1)]:
            if attack(attacker, defender):
                break
            input("Press enter to continue...\n")

        if character1.health <= 0 or character2.health <= 0:
            break

    if character1.health > 0:
        print(f"{character1.name} wins!")

    elif character2.health > 0:
        print(f"{character2.name} wins!")

    else:
        print("Draw!")

def attack(attacker, defender):
    print(f"{attacker.name} attacks the {defender.name}...")
    if random.randint(1, 100) <= attacker.hitChance:
        damage = random.randint(1, attacker.maxDamage)
        effectiveDamage = max(0, damage - defender.armor)
        defender.health -= effectiveDamage
        print(f"  For {damage} damage!")
        print(f"  {defender.name}'s armor was able to absorb {defender.armor} damage!")

    else:
        print(f"  But misses!")
    print(f"{attacker.name}: {attacker.health} Health")
    print(f"{defender.name}: {defender.health} Health")
    print()
    return defender.health <= 0

if __name__ == "__main__":
    hero = Character("Hero", 10, 50, 5, 2)
    monster = Character("Monster", 20, 30, 5, 0)

    hero.stats()
    monster.stats()

    input("Press enter to begin!")
    fight(hero, monster)
