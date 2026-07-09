import random

# ==========================
# ASCII ART
# ==========================

logo = r'''
 __          __                 _             
 \ \        / /                (_)            
  \ \  /\  / /_ _ _ __ _ __ ___ _  ___  _ __  
   \ \/  \/ / _` | '__| '__/ _ \ |/ _ \| '__| 
    \  /\  / (_| | |  | | |  __/ | (_) | |    
     \/  \/ \__,_|_|  |_|  \___|_|\___/|_|    

        CLI TURN-BASED FIGHTING GAME
'''

print(logo)

# ==========================
# PLAYER
# ==========================

player = {
    "name": "Warrior",
    "hp": 100,
    "attack": 20,
    "potions": 3
}

# ==========================
# ENEMIES (Nested Dictionary)
# ==========================

enemies = {
    "Goblin 1": {
        "hp": 40,
        "attack": 8
    },
    "Goblin 2": {
        "hp": 50,
        "attack": 10
    },
    "Orc 1": {
        "hp": 70,
        "attack": 15
    },
    "Orc 2": {
        "hp": 90,
        "attack": 18
    },
    "Dragon": {
        "hp": 150,
        "attack": 25
    }
}

# ==========================
# FUNCTIONS
# ==========================

def show_status(enemy_name, enemy):

    print("\n==============================")
    print(f"Player HP : {player['hp']}")
    print(f"Potions   : {player['potions']}")
    print("------------------------------")
    print(f"Enemy     : {enemy_name}")
    print(f"Enemy HP  : {enemy['hp']}")
    print("==============================")



def attack_enemy(enemy):

    damage = random.randint(15, player["attack"])

    enemy["hp"] -= damage

    if enemy["hp"] < 0:
        enemy["hp"] = 0

    print(f"\nYou attacked for {damage} damage!")



def heal():

    if player["potions"] > 0:

        heal_amount = random.randint(30, 50)

        player["hp"] += heal_amount

        if player["hp"] > 100:
            player["hp"] = 100

        player["potions"] -= 1

        print(f"\nYou healed {heal_amount} HP.")

    else:

        print("\nNo potions left!")



def enemy_attack(enemy_name, enemy):

    damage = random.randint(5, enemy["attack"])

    player["hp"] -= damage

    if player["hp"] < 0:
        player["hp"] = 0

    print(f"{enemy_name} attacked you for {damage} damage!")



def battle(enemy_name, enemy):

    print("\n=================================")
    print(f"A wild {enemy_name} appeared!")
    print("=================================")

    while enemy["hp"] > 0 and player["hp"] > 0:

        show_status(enemy_name, enemy)

        print("\n1. Attack")
        print("2. Heal")

        choice = input("\nChoose an option: ")

        if choice == "1":

            attack_enemy(enemy)

            if enemy["hp"] <= 0:

                print(f"\nYou defeated {enemy_name}!")

                break

            enemy_attack(enemy_name, enemy)

        elif choice == "2":

            heal()

            enemy_attack(enemy_name, enemy)

        else:

            print("\nInvalid choice!")



# ==========================
# GAME START
# ==========================

print("Welcome Warrior!")
print("Defeat all enemies to win!\n")

for enemy_name in enemies:

    battle(enemy_name, enemies[enemy_name])

    if player["hp"] <= 0:

        print("\n==========================")
        print("YOU DIED!")
        print("GAME OVER")
        print("==========================")

        break

else:

    print("\n################################")
    print("YOU DEFEATED ALL ENEMIES!")
    print("THE DRAGON HAS BEEN SLAIN!")
    print("YOU ARE THE HERO OF THE KINGDOM!")
    print("################################")