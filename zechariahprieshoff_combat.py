#Zechariah Prieshoff
#May 31st, 2024
#(lab) Turn based combat
#Program simulates your classic turn based combat game with random stats and attack chances.


import zechariahprieshoff_tbc

def main():
    ready = input("Are you ready to fight? (yes/no): ").lower()
    if ready != "yes":
        print("Come back when you are ready.")
        return

    hero = zechariahprieshoff_tbc.Character("Hero", 10, 50, 5, 2)

    monster = zechariahprieshoff_tbc.Character("Monster", 20, 30, 5, 0)

    hero.stats()
    monster.stats()

    input("Press enter to begin!")
    print()
    zechariahprieshoff_tbc.fight(hero, monster)

main()