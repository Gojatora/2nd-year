import Pokemon_Functions as pf
import random as rd
import array as arr
import tabulate as tb
import time as t

st = t.time()

Pokemon_ID = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                             11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                             21, 22, 23, 24, 25, 26, 27, 28, 29, 30])

Pokemon_list = ["Raichu", "Charizard", "Venusaur", "Blastoise", "Wigglypuff", "Gengar", "Sylveon", "Snorlax", "Mewtwo", "Lucario",
                    "Greninja", "Togepi", "Lunala", "Latias", "Gyarados", "Dragonite", "Snivy", "Kyogre", "Zoroark", "Groudon",
                    "Aggron", "Regirock", "Deoxys", "Froslass", "Altaria", "Milotic", "Crobat", "Flareon", "Gallade", "Steelix"]

Health = arr.array('i', [60, 78, 80, 79, 140, 60, 95, 160, 106, 70, 
                         72, 85, 137, 80, 95, 91, 75, 100, 60, 100, 
                         70, 80, 50, 70, 75, 95, 85, 65, 68, 75])

Power = arr.array('i', [90, 84, 82, 83, 70, 65, 65, 110, 110, 110, 
                        95, 50, 113, 80, 125, 134, 75, 100, 105, 150, 
                        110, 100, 150, 80, 70, 60, 90, 130, 125, 85])

selected_pokemon = arr.array('i', [])

player_1_Pokemon_Storage = arr.array('i', [])
player_1_Pokemon_Health = arr.array('i', [])
player_1_Pokemon_Power = arr.array('i', [])

player_2_Pokemon_Storage = arr.array('i', [])
player_2_Pokemon_Health = arr.array('i', [])
player_2_Pokemon_Power = arr.array('i', [])

Health_Potions = arr.array('i', [1, 2])

Poison_Potions = arr.array('i', [1, 2])

player_1_used_health_potions = arr.array('i', [])
player_1_used_poison_potions = arr.array('i', [])
player_2_used_health_potions = arr.array('i', [])
player_2_used_poison_potions = arr.array('i', [])

Player_1_Pokemon_Preview = []
Player_2_Pokemon_Preview = []

Battle_Summary = []

player_1 = input("Enter Player 1's name: ")
player_2 = input("Enter Player 2's name: ")
while True:
    if player_2 == player_1:
        print("Enter another name")
        player_2 = input("Enter Player 2's name: ")

    else:
        break

print(f"\nGreetings, {player_1} and {player_2}. Welcome to Pokemon Battle Royale: Power, Strategy, and Fatigue")

print("\nHow does this game work?")
print("\nBoth players will take turns when picking their desired Pokemon.")
print("Both players can choose whether they will pick their desired Pokemon themselves or let the Computer determine their Pokemon picks")
print("Each Pokemon has its unique Health and Power.")
print("Once the Pokemon selection is finished, they will proceed to battle each other.")
print("\nThe battle simulation goes like this:")
print("The program will randomly pair up each Pokemon to battle each other.")
print("Before both Pokemon attack each other, Both Players are allowed to use limited amount of health potions which heals their pokemon and poison potion to damage each other's Pokemon.")
print("Then both Pokemons will attack each other which damages them and decrease their health.")
print("The program will decide the winner of each battle based on their remaining health.")
print("\nAfter each battle, both pokemons will have a decreased in health due to fatigue.")
print("The program will continue to select the Pokemon to battle until their health is 0.")
print("Once either side has no remaining Pokemon to battle, the program will announce the overall winner based on the amount of battles won of both players.")

print("\nEnough yapping! It's time to get this show started!")


print("\nPicking turns: Heads or tails?")
print("Whoever chose correctly will pick first, alternatively.")

while True:
    try: 
        player_1_coinside = int(input(f"\n{player_1}, Heads (0) or Tails (1)?: "))
        if player_1_coinside== 0:
            player_2_coinside = 1
            print(f"If {player_1} is heads, then {player_2} is tails")
            break
        elif player_1_coinside == 1:
            player_2_coinside = 0
            print(f"If {player_1} is tails, then {player_2} is heads")
            break
        else:
            print("Invalid input, 0 for heads and 1 for tails only. Try again")
    except ValueError:
        print("Invalid input, 0 for heads and 1 for tails only. Try again")

coin = [0, 1]

side = rd.choice(coin)

if side == 0:
    print("The coin landed on heads!")
else:
    print("The coin landed on tails!")
    
turn_indicator = {
    f"{player_1}": player_1_coinside,
    f"{player_2}": player_2_coinside
}

if turn_indicator[f"{player_1}"] == side:
    print(f"\n{player_1} is first to select their list of Pokemon")


else:
    print(f"\n{player_2} is first to select their list of Pokemon")

while True:
    player_1_mode_of_selection = input(f"{player_1}, do you want the computer to select your list of Pokemon for you? (yes or no): ").lower()
    if player_1_mode_of_selection == "yes" or player_1_mode_of_selection == "no":
        break
    else:
        print("Yes or No only") 

while True:
    player_2_mode_of_selection = input(f"{player_2}, do you want the computer to select your list of Pokemon for you? (yes or no): ").lower()
    if player_2_mode_of_selection == "yes" or player_2_mode_of_selection == "no":
        break 
    else:
        print("Yes or No only")

i = 0
print("\nSelect a Pokemon from this list through 1-30:")
while i < 30:
    for i in range(0 + i, 5 + i):
        print(f"{i+1}. {Pokemon_list[i]}", end="    ")
        i += 1
    print("\n")
    

def Selection(limit):
    print(f"\nEach player will have {limit} Pokemon at their disposal")
    count = 1
    while count <= limit:
        if turn_indicator[f"{player_1}"] == side:
            selection = pf.Selecting_Pokemon(player_1, count, player_1_mode_of_selection, Pokemon_ID, Pokemon_list, Health, Power, selected_pokemon)
            extracted_pokemon = selection.Selecting()
            player_1_Pokemon_Storage.append(extracted_pokemon[0])
            player_1_Pokemon_Health.append(extracted_pokemon[1])
            player_1_Pokemon_Power.append(extracted_pokemon[2])
            selected_pokemon.append(extracted_pokemon[0])

            selection = pf.Selecting_Pokemon(player_2, count, player_2_mode_of_selection, Pokemon_ID, Pokemon_list, Health, Power, selected_pokemon)
            extracted_pokemon = selection.Selecting()
            player_2_Pokemon_Storage.append(extracted_pokemon[0])
            player_2_Pokemon_Health.append(extracted_pokemon[1])
            player_2_Pokemon_Power.append(extracted_pokemon[2])
            selected_pokemon.append(extracted_pokemon[0])

            count += 1
        else:
            selection = pf.Selecting_Pokemon(player_2, count, player_2_mode_of_selection, Pokemon_ID, Pokemon_list, Health, Power, selected_pokemon)
            extracted_pokemon = selection.Selecting()
            player_2_Pokemon_Storage.append(extracted_pokemon[0])
            player_2_Pokemon_Health.append(extracted_pokemon[1])
            player_2_Pokemon_Power.append(extracted_pokemon[2])
            selected_pokemon.append(extracted_pokemon[0])
            
            selection = pf.Selecting_Pokemon(player_1, count, player_1_mode_of_selection, Pokemon_ID, Pokemon_list, Health, Power, selected_pokemon)
            extracted_pokemon = selection.Selecting()
            player_1_Pokemon_Storage.append(extracted_pokemon[0])
            player_1_Pokemon_Health.append(extracted_pokemon[1])
            player_1_Pokemon_Power.append(extracted_pokemon[2])
            selected_pokemon.append(extracted_pokemon[0])

            count += 1
    '''
    while True:
        extra = input(f"{player_1}, do you want to select an extra Pokemon (Yes of No): ").lower()
        if extra == "yes":
            selection = pf.Selecting_Pokemon(player_1, count, player_1_mode_of_selection, Pokemon_ID, Pokemon_list, Health, Power, selected_pokemon)
            extracted_pokemon = selection.Selecting()
            player_1_Pokemon_Storage.append(extracted_pokemon[0])
            player_1_Pokemon_Health.append(extracted_pokemon[1])
            player_1_Pokemon_Power.append(extracted_pokemon[2])
            selected_pokemon.append(extracted_pokemon[0])
            break
        elif extra == "no":
            break
        else:
            print("Yes or No only.")

    while True:
        extra = input(f"{player_2}, do you want to select an extra Pokemon (Yes of No): ").lower()
        if extra == "yes":
            selection = pf.Selecting_Pokemon(player_2, count, player_2_mode_of_selection, Pokemon_ID, Pokemon_list, Health, Power, selected_pokemon)
            extracted_pokemon = selection.Selecting()
            player_2_Pokemon_Storage.append(extracted_pokemon[0])
            player_2_Pokemon_Health.append(extracted_pokemon[1])
            player_2_Pokemon_Power.append(extracted_pokemon[2])
            selected_pokemon.append(extracted_pokemon[00])
            break
        elif extra == "no":
            break
        else:
            print("Yes or No only.")
        '''

limit = rd.randint(3,4)

Selection(limit)

header_preview = ["Pokemon ID", "Pokemon", "Health", "Power"]
header_battle_summary = ["Battle Number", f"{player_1}'s Pokemon (ID) Name", "Damaged Health", "Power",  "Health Potion Used", "Poison Potion Used", " ", f"{player_2}'s Pokemon (ID) Name", "Damaged Health", "Power", "Health Potion Used", "Poison Potion Used", "Status"]

print(f"\n{player_1}'s Pokemon List\n")

for i in range(0, len(player_1_Pokemon_Storage)):
    Player_1_Pokemon_Preview.append([player_1_Pokemon_Storage[i], Pokemon_list[Pokemon_ID.index(player_1_Pokemon_Storage[i])], player_1_Pokemon_Health[i], player_1_Pokemon_Power[i]])

table1 = tb.tabulate(Player_1_Pokemon_Preview, headers=header_preview, tablefmt= "pretty")
print(table1)


print(f"\n{player_2}'s Pokemon List\n")

for i in range(0, len(player_2_Pokemon_Storage)):
    Player_2_Pokemon_Preview.append([player_2_Pokemon_Storage[i], Pokemon_list[Pokemon_ID.index(player_2_Pokemon_Storage[i])], player_2_Pokemon_Health[i], player_2_Pokemon_Power[i]])

table2 = tb.tabulate(Player_2_Pokemon_Preview, headers=header_preview, tablefmt= "pretty")
print(table2)


def Battle():
    player_1_win_count = 0
    player_2_win_count = 0
    draw_count = 0
    battle_count = 1
    while True:
        battle_outcome = pf.Battle_Simulation(player_1_Pokemon_Storage, player_1_Pokemon_Health, player_1_Pokemon_Power, 
                                            player_2_Pokemon_Storage, player_2_Pokemon_Health, player_2_Pokemon_Power, 
                                            Health_Potions, Poison_Potions, player_1_used_health_potions, 
                                            player_1_used_poison_potions, player_2_used_health_potions, player_2_used_poison_potions,
                                            Pokemon_list, Pokemon_ID, player_1, player_2, player_1_win_count, player_2_win_count, draw_count)
        results = battle_outcome.Versus()
        if results != None:
            Battle_Summary.append([battle_count, f"{results[0]}. {results[1]}", f"{results[16]}", f"{results[3]}", f"{results[18]}", f"{results[19]}", " ", f"{results[4]} {results[5]}", f"{results[17]}", f"{results[7]}", f"{results[20]}", f"{results[21]}", results[12]])
            table_summary = tb.tabulate(Battle_Summary, headers=header_battle_summary, tablefmt= "pretty")
            print(table_summary)
            pinpointer = player_1_Pokemon_Storage.index(results[0])
            player_1_Pokemon_Health[pinpointer] = results[2]
            if results[8] == "None":
                pass
            else:
                player_1_used_health_potions.append(results[8])
            
            if results[9] == "None":
                pass
            else:
                player_1_used_poison_potions.append(results[9])
            
            player_1_win_count = results[13]

            pinpointer = player_2_Pokemon_Storage.index(results[4])
            player_2_Pokemon_Health[pinpointer] = results[6]
            if results[10] == "None":
                pass
            else:
                player_2_used_health_potions.append(results[10])
            
            if results[11] == "None":
                pass
            else:
                player_2_used_poison_potions.append(results[11])
            
            player_2_win_count = results[14]

            draw_count = results[15]
        else:
            break
        battle_count += 1

    
    print("\nThe Battle is Over, Deciding the Overall Winner")
    if player_1_win_count > player_2_win_count:
        print(f"The Overall Winner is {player_1}")
    if player_1_win_count == player_2_win_count:
        print(f"The Overall Winner is no one. It's a Draw!")
    else:
        print(f"The Overall Winner is {player_2}")
    
    print(f"{player_1}: {player_1_win_count} Wins / {(battle_count - player_1_win_count - 1) - draw_count} Loses|| {player_2}: {player_2_win_count} Wins / {(battle_count - player_2_win_count - 1) - draw_count} Loses")
    print(f"Total draws: {draw_count}")

Battle()


et = t.time()

elapsed_time = et - st

print("\nThank you guys for playing!")

print(f"Total run time: {elapsed_time}")