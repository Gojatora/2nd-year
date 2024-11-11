import Pokemon_Functions as pf #imports the file created by the programmer which contains two classes that will be called as "pf"
import random as rd #imports the random module that will be called as "rd"
import array as arr #imports the array module that will be called as "arr"
import tabulate as tb #imports the tabulate modules that will be called as "tb"
import time as t #imports the time module that will be called as "t"

st = t.time() #stores the starting time of the game

player_1 = input("Enter Player 1's name: ")
player_2 = input("Enter Player 2's name: ")
while True:
    if player_2 == player_1:
        print("Enter another name")
        player_2 = input("Enter Player 2's name: ")

    else:
        break

print(f"\nGreetings, {player_1} and {player_2}. Welcome to Pokemon Battle Royale: Power, Strategy, and Fatigue")
t.sleep(2)
print("\nHow does this game work?")
t.sleep(1)
print("\nBoth players will take turns when picking their desired Pokemon \nand the program will select the first player to select based on a coin flip")
t.sleep(2)
print("\nBoth players can choose either to have 3 or 4 pokemons")
t.sleep(1)
print("If both players chose the same pokemon count, that count will be set.")
t.sleep(1)
print("If not, the program will decide on 50/50")
t.sleep(2)
print("\nBoth players can choose whether they will pick their \ndesired Pokemon themselves or let the Computer determine their Pokemon picks")
t.sleep(1)
print("Each Pokemon has its unique Health and Power.")
t.sleep(2)
print("\nOnce the Pokemon selection is finished, they will proceed to battle each other.")
t.sleep(2)
print("\nThe battle simulation goes like this:")
t.sleep(1)
print("The program will randomly pair up each Pokemon to battle each other.")
t.sleep(2)
print("\nBefore both Pokemon attack each other, Both Players are allowed to use limited amount of \nhealth potions which heals their pokemon and poison potion to damage each other's Pokemon.")
t.sleep(2)
print("\nThen both Pokemons will attack each other which damages them and decrease their health.")
t.sleep(2)
print("\nThe program will decide the winner of each battle based on their remaining health.")
t.sleep(2)
print("\nAfter each battle, both pokemons will have a decreased in health due to fatigue.")
t.sleep(2)
print("\nThis battle will continue until either side do not have Pokemons to battle.")
t.sleep(2)
print("\nOnce either side has no remaining Pokemon to battle, the program will \nannounce the overall winner based on the amount of battles won of both players.")
t.sleep(2)

print("\nEnough yapping! It's time to get this show started!")
t.sleep(2)

#This function is the main operation of the program which contains pokemon selection as well as battle simulation
def Battle():
    # Pokemon_ID storage via arrays for Pokemon's ID number which can also be used as an index finder
    Pokemon_ID = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                             11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                             21, 22, 23, 24, 25, 26, 27, 28, 29, 30])

    Pokemon_list = ["Raichu", "Charizard", "Venusaur", "Blastoise", "Wigglypuff", "Gengar", "Sylveon", "Snorlax", "Mewtwo", "Lucario",
                        "Greninja", "Togepi", "Lunala", "Latias", "Gyarados", "Dragonite", "Snivy", "Kyogre", "Zoroark", "Groudon",
                        "Aggron", "Regirock", "Deoxys", "Froslass", "Altaria", "Milotic", "Crobat", "Flareon", "Gallade", "Steelix"]

    Health = arr.array('i', [84, 97, 87, 90, 107, 92, 95, 106, 107, 89, 
                            90, 82, 105, 80, 95, 91, 83, 94, 99, 86, 
                            95, 85, 89, 93, 92, 95, 85, 77, 88, 102])

    Power = arr.array('i', [90, 84, 99, 83, 79, 74, 78, 110, 88, 99, 
                            95, 86, 109, 80, 109, 97, 75, 99, 84, 96, 
                            98, 88, 96, 80, 70, 75, 90, 104, 112, 85])

    selected_pokemon = arr.array('i', []) # This serves as storage for selected Pokemon to avoid duplication
    
    #The following uses arrays for player 1's Pokemon storage as well as its corresponding health and power
    player_1_Pokemon_Storage = arr.array('i', []) 
    player_1_Pokemon_Health = arr.array('i', [])
    player_1_Pokemon_Power = arr.array('i', [])

    #The following uses arrays for player 2's Pokemon storage via arrays as well as its corresponding health and power
    player_2_Pokemon_Storage = arr.array('i', [])
    player_2_Pokemon_Health = arr.array('i', [])
    player_2_Pokemon_Power = arr.array('i', [])

    #The following are ID for health and poison potions
    Health_Potions = arr.array('i', [1, 2])
    Poison_Potions = arr.array('i', [1, 2])

    #The following uses arrays as storage for used health and poison potions
    player_1_used_health_potions = arr.array('i', [])
    player_1_used_poison_potions = arr.array('i', [])
    player_2_used_health_potions = arr.array('i', [])
    player_2_used_poison_potions = arr.array('i', [])

    #The following stores each player's Pokemon and their stats that will be used to display after Pokemon selection
    Player_1_Pokemon_Preview = []
    Player_2_Pokemon_Preview = []

    #The following will store the battle history details that will be displayed after each battles
    Battle_Summary_1 = [] 
    Battle_Summary_2 = []

    print("\nPicking turns: Heads or tails?")
    t.sleep(1)
    print("Whoever chose correctly will pick first.")
    t.sleep(1)

    #This blocks simulates which player gets to choose first
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
    t.sleep(1)

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
    t.sleep(1)
    if turn_indicator[f"{player_1}"] == side:
        print(f"\n{player_1} is first to select their list of Pokemon")
    else:
        print(f"\n{player_2} is first to select their list of Pokemon")
    
    t.sleep(1)
    #The program asks if both players can let the computer choose their Pokemon
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

    #The program asks both players the amount of Pokemon's they want
    while True:
        try:
            p1_limit = int(input(f"{player_1}, choose how many Pokemons do you want in your storage, 3 or 4: "))
            if p1_limit > 4:
                print("Choose between 3 and 4 only")
            elif p1_limit < 3:
                print("Choose between 3 and 4 only")
            else:
                break
        except ValueError:
            print("Enter a digit")
    while True:
        try:
            p2_limit = int(input(f"{player_2}, choose how many Pokemons do you want in your storage, 3 or 4: "))
            if p2_limit > 4:
                print("Choose between 3 and 4 only")
            elif p2_limit < 3:
                print("Choose between 3 and 4 only")
            else:
                break
        except ValueError:
            print("Enter a digit")
    if p1_limit == p2_limit:
        print(f"Both Players agreed on the same Pokemon count. They can choose {p1_limit} Pokemon in their arsenal")
        limit = p1_limit
    else:
        print("Both players disagreed on the Pokemon count. Let us decide on 50/50")
        t.sleep(2)
        limit = rd.randint(3,4)
        print(f"The result is.....{limit}. Both players can choose {limit} Pokemon in their arsenal")
    

    t.sleep(2) 
    
    pokemon_preview_list = []
    header_pokemon_list = ["Pokemon ID", "Pokemon"]

    print("\nSelect a Pokemon from this list through 1-30:")
    i = 0
    while i < 30:
        for i in range(0 + i, 5 + i):
            pokemon_preview_list.append([f"{i+1}", f"{Pokemon_list[i]}"])
            i += 1
    table_list = tb.tabulate(pokemon_preview_list, headers=header_pokemon_list, tablefmt= "pretty")
    print(table_list)

    #This block of code is where the Selecting_Pokemon function is called so that both players can selects their Pokemon in alternate turns until the count limit reaches the decided Pokemon count
    #Selected Pokemons are "removed" from the Pokemon list
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

    #This serves as headers when printing the table for pokemon preview
    header_preview = ["Pokemon ID", "Pokemon", "Health", "Power"]
    

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
    
    #This serves as headers when printing the table for battle history
    header_battle_summary_1 = ["Battle Number", f"{player_1}'s Pokemon (ID) Name", "Damaged Health", "Power",  "Health Potion Used", "Poison Potion Used"]
    header_battle_summary_2 = [f"{player_2}'s Pokemon (ID) Name", "Damaged Health", "Power", "Health Potion Used", "Poison Potion Used", "Status"]
    player_1_win_count = 0
    player_1_lose_count = 0
    player_2_win_count = 0
    player_2_lose_count = 0
    draw_count = 0
    battle_count = 1

    #This block of code will repeatedly call the Battle_Simulation class from the Pokemon_Functions file to simulate battles until all Pokemon of either side have 0 health
    while True:
        battle_outcome = pf.Battle_Simulation(player_1_Pokemon_Storage, player_1_Pokemon_Health, player_1_Pokemon_Power, 
                                            player_2_Pokemon_Storage, player_2_Pokemon_Health, player_2_Pokemon_Power, 
                                            Health_Potions, Poison_Potions, player_1_used_health_potions, 
                                            player_1_used_poison_potions, player_2_used_health_potions, player_2_used_poison_potions,
                                            Pokemon_list, Pokemon_ID, player_1, player_2, player_1_win_count, player_1_lose_count, player_2_win_count, player_2_lose_count, draw_count)
        results = battle_outcome.Versus()
        if results != None:
            print("\nBattle Summary:")
            Battle_Summary_1.append([battle_count, f"{results[0]}. {results[1]}", f"{results[18]}", f"{results[3]}", f"{results[20]}", f"{results[21]}"])
            table_summary_1 = tb.tabulate(Battle_Summary_1, headers=header_battle_summary_1, tablefmt= "pretty")
            print(table_summary_1)

            Battle_Summary_2.append([f"{results[4]}. {results[5]}", f"{results[19]}", f"{results[7]}", f"{results[22]}", f"{results[23]}", results[12]])
            table_summary_2 = tb.tabulate(Battle_Summary_2, headers=header_battle_summary_2, tablefmt= "pretty")
            print(table_summary_2)

            pinpointer = player_1_Pokemon_Storage.index(results[0])
            player_1_Pokemon_Health[pinpointer] = results[2] #Updates the health of the Pokemon used in the concluded battle
            if results[8] == "None":
                pass
            else:
                player_1_used_health_potions.append(results[8])
            
            if results[9] == "None":
                pass
            else:
                player_1_used_poison_potions.append(results[9])
            
            pinpointer = player_2_Pokemon_Storage.index(results[4])
            player_2_Pokemon_Health[pinpointer] = results[6] #Updates the health of the Pokemon used in the concluded battle
            if results[10] == "None":
                pass
            else:
                player_2_used_health_potions.append(results[10])
            
            if results[11] == "None":
                pass
            else:
                player_2_used_poison_potions.append(results[11])
            
            player_1_win_count = results[13]
            player_1_lose_count = results[14]
            player_2_win_count = results[15]
            player_2_lose_count = results[16]

            draw_count = results[17]

            #Displays Statistics 
            print(f"{player_1}: {player_1_win_count} Wins / {player_1_lose_count} Loses|| {player_2}: {player_2_win_count} Wins / {(player_2_lose_count) - draw_count} Loses")
            print(f"Total draws: {draw_count}")
            battle_count += 1
        
        else:
            break
        
    #Displays overall winner and final statistics
    print("\nThe Battle is Over, Deciding the Overall Winner")
    t.sleep(3)
    if player_1_win_count > player_2_win_count:
        print(f"The Overall Winner is {player_1}")
    if player_1_win_count == player_2_win_count:
        print(f"The Overall Winner is no one. It's a Draw!")
    else:
        print(f"The Overall Winner is {player_2}")
    t.sleep(2)
    print(f"{player_1}: {player_1_win_count} Wins / {player_1_lose_count} Loses|| {player_2}: {player_2_win_count} Wins / {(player_2_lose_count) - draw_count} Loses")
    t.sleep(1)
    print(f"Total draws: {draw_count}")

    play_again = input("Enter Y to play again or any key to quit: ").upper()
    if play_again == "Y":
        print("Let us play again!\n")
        Battle()
    else:
        pass

Battle()

et = t.time() #stores the ending time of the game

elapsed_time = et - st

print("\nThank you guys for playing!")

print(f"Total run time: {elapsed_time}")
