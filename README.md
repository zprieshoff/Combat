# (lab) turn based combat

This program simulates a classic turn-based combat game with characters having random stats, attack chances, and outcomes.

## A description of the character class

Character class is defined inside of 'zechariahprieshoff_tbc.py' and represents the characters inside the game.

## Planned limitations of every property

* **name: (str)** > name of the character, there isn't any specific limitations as it can be any string.
* **health: (int)** > health points of the character, needs to be a positive integer and is set at 10 by default.
* **hitChance: (int)** > the chances or percent that the characters(attackers) attack hits the other character(defender). Needs to be an integer between 0 and 100. Set at 50 by default.
* **maxDamage: (int)** > The max about of damage the character can deal to the other character. Needs to be a postitive integer, set at 5 by default and it's minimum is forced at 1.
* **armor: (int**) > armor points that can absorb an attack. Needs to be a non negative, 0 and up. Set at 2 by default.

## An algorithm for each method or function 

* **__init__(self, name="Jin Sakai", health=10, hitChance=50, maxDamage=5, armor=2):** > Creates a new character with default stats and attributes. Can be changed. Makes sure that hitChance is between 0 and 100 by using the testInt method. Makes sure that maxDamage is a positive integer and at least 1. Makes sure that armor is a non negative integer and at least 0.
* **testInt(self, value, min=0, max=100, default=0)** > Makes sure that all the stats integer values meet their given ranges. Returns their values if they meet their ranges. If the values don't meet their ranges, health is set at -10, a message is outputted notifying the user and they are set to their specified default value.
* **stats(self):** > Prints the characters stats. This includes name, health, hit chance, max damage, and armor.
* **fight(character1, character2):** > This manages the combat between the characters. Alternates the output between each character until one of their healths equals 0 or if theres a tie.
* **attack(attacker, defender):** > Outputs an attack from the charcter "attacker" against the character "defender". Determines if the attack hits the defender based on the attackers hit chance. Calculates how much damage is dealt to the defender by considering the value of the defeenders 		armor.
* **main() inside zechariahprieshoff_combat.py:** > Outputs a prompt to the user to start the game. Creates the hero and monster characters. Outputs the hero and monsters stats. Outputs a prompt to the user to begin the fight.

# For the correct output, users should run the program via the combat.py file. (zechariahprieshoff_combat.py)
