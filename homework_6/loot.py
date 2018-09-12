leviathan_axe = {
    "NAME": "Leviathan axe",
    "STR": 7,
    "AGI": +1,
}
bronze_shield = {
    "NAME": "Bronze shield",
    "DEF": +5,
    "AGI": -1,
}
golden_staff = {
    "Name": "Golden stick",
    "AGI": 15,
    "STR": 5,
}


def show_item(game_item):
    print("*" * 15)

    for key, value in game_item.items():
        print("*", key, ":", value)

    print("*" * 15)


inventory = [leviathan_axe, bronze_shield, golden_staff]
