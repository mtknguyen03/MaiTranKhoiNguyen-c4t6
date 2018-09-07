name = input("What's your name? ")
player = {
    "NAME": name,
    "CLASS": "Greek demigod",
    "WEAPON": "Sword",
    "HP": 100,
    "STR": 10,
    "DEF": 6,
    "AGI": 1,
    "LVL": 1,
    "LUCK": 10,
}
cmd = input("Your command (stats, start): ")
if cmd == "stats":
    print("NAME:", player["NAME"])
    print("CLASS", player["CLASS"])
    print("HP", player["HP"])
    print("STR", player["STR"])
    print("DEF", player["DEF"])
    print("AGI", player["AGI"])
    print("LVL", player["LVL"])
    print("LUCK", player["LUCK"])
elif cmd == "Start" or cmd == "start":
    print("You are a demigod, an offspring of a god and a mortal")
    print("The HB camp(where you live) have heard a prophecy")
    print("You have been chosen to go on a quest to save the god from an evil force")
    print("Now you can:")
    print("1. stay in the camp(You really gonna chose this?)")
    print("2. go and become a hero! ")
    choice = input("Your choice: ")
    if choice == "1":
        print("So be it...")
        print("I thought you were special...")
        print("We will choose another one...")
        print("GAME OVER")
    elif choice == "2":
        print("I know i could trust you!")
        print("You go out and start your quest...")
        print("A journey begin!")
        print("After an hour of walking, you see a hellhound!")
        print("Would you:")
        print("1. run away!")
        print("2. stand still, it haven't seen you(yet)")
        print("3. FIGHT!FIGHT!FIGHT!(sorry, i just got excited :) )")
    choice = input("Your choice: ")
    if choice == "1":
        print("you try to run, but you not fast enough")
        print("The hound run toward you and rip you apart")
        print("A bit nasty, I know, but I have to keep the story interesting even if you lose")
        print("GAME OVER")
    elif choice == "2":
        print("Right after that thought, the dog see you!")
        print("Before you can do anything, it go and kill you in one bite!")
        print("Sorry, I just want to see a fight")
        print("After all, you need to learn how to fight!")
        print("GAME OVER")
    elif choice == "3":
        hound = {
            "NAME": "young hellhound",
            "CLASS": "Hellhound(Obviously!)",
            "HP": 50,
            "STR": 10,
            "DEF": 1,
            "AGI": 1,
            "LVL": 1,
        }
        print("OPPONENT:", hound["NAME"])
        print("CLASS:", hound["CLASS"])
        print("HP:", hound["HP"])
        print("STRENGTH:", hound["STR"])
        print("DEFENSE:", hound["DEF"])
        print("AGILITY:", hound["AGI"])
        print("LEVEL:", hound["LVL"])

        print("You and the hound see each other")
        print("You take out your sword and make the first move!")
        print("WAIT, I forgot to told you that you have a sword?!?!")
        print("How do I forget that?!?!")
        print("Let just ... accept it,ok?")
        print("After all, you wouldn't want to fight with your bare hands!")
        print("anyway")
        print("you are the first one to attack!")


        def combat(attacker, defender):
            print(attacker["NAME"], "is trying to end", defender["NAME"], "life" "!")
            damage = attacker["STR"] - defender["DEF"]
            if damage > 0:
                defender["HP"] -= damage
                print(defender["NAME"], "lost", damage, "HP")
            else:
                attacker["HP"] -= abs(damage)
                print(attacker["NAME"], "lost", abs(damage), "HP")


        while True:
            combat(player, hound)
            print("Hellhound hp:", hound["HP"])

            if hound["HP"] <= 0 or player["HP"] <= 0:
                break

            combat(hound, player)
            print("Your hp:", player["HP"])

            if hound["HP"] <= 0 or player["HP"] <= 0:
                break

        if player["HP"] <= 0:
            print("Try again next time!")
            print("Game Over")
        if hound["HP"] <= 0:
            print("The hellhound is defeated!")
            print("But...")
            print("The fight has given you some serious health problems")
            print("luckily, before you go on the quest, you have brought a bottle of nectar with you")
            print("(Nectar is the drink of the god, can heal demigod, will burn mortals to ash)")
            print("Do you want to:")
            print("1. leave it in the bag")
            print("2. drink it")
            choice = input("Your choice")
            if choice == "1":
                print("Maybe another time...")
            elif choice == "2":
                print("You drink just enough to heal the wound")
                print("Your health has fully recovered!")
                player["HP"] = 100
                print("Your HP:", player["HP"])
                









