from random import randint

def calculate_crit(player):
    has_crit = False
    dice = randint(0, 20)
    chance = player["LUCK"] + player["AGI"]
    if chance > dice:
        has_crit = True

    return has_crit


def combat_round(attacker, defender):
    print(attacker["NAME"], "is beating", defender["NAME"], "!")
    h = calculate_crit(attacker)
    if h:
        print("Critical hit!!!")
        damage = attacker["STR"] * 2 - defender["DEF"]
    else:
        damage = attacker["STR"] - defender["DEF"]
    if damage > 0:
        defender["HP"] -= damage
        print(defender["NAME"], "lost", damage, "HP")
        print(defender["NAME"], "has", defender["HP"], "hp left")
    else:
        attacker["HP"] -= attacker["STR"]
        print(attacker["NAME"], "lost", attacker["STR"], "HP")
        print(attacker["NAME"], "has", attacker["HP"], "hp left")


def combat_full(player, opponent):
    auto_combat = False
    while True:
        combat_round(player, opponent)
        if opponent["HP"] <= 0 or player["HP"] <= 0:
            break

        combat_round(opponent, player)
        if opponent["HP"] <= 0 or player["HP"] <= 0:
            break

        if not auto_combat:
            print("Do you want to:")
            print("1. Continue")
            print("2. Run , you can't be bother right now")
            print("3. Auto fight")
            option = input("Anddd??? ")
            if option == "1":
                print("You continue the fight like a badass!")
            elif option == "2":
                dice = randint(0, 100)
                if player["LUCK"] >= dice:
                    print("You successfully escape!")
                    break
                else:
                    print("You fail!!")
            elif option == "3":
                auto_combat = True
