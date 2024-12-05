import random as rd
import Pokemon_Functions as PF
import tabulate as tb
import numpy as np
import time as t
import array as arr

player_1 = input("Enter Player 1's name: ")
player_2 = input("Enter Player 2's name: ")
while True:
    if player_2 == player_1:
        print("Enter another name")
        player_2 = input("Enter Player 2's name: ")

    else:
        break

print(f"Greetings, {player_1} and {player_2}. Welcome to Pokemon Battle: The ULTIMATUM")

print("Before we start, Here's how the game works:")
print("Players will have 3 Pokemons to select.")
print("Players will do a cointoss to know who gets to pick their set of Pokemon in an alternate way.")
print("The Selection Phase is separated into 3 rounds.")
print("The first round of selection is selecting a juvenile Pokemon,")
print("The second round of selection is selecting a fully evolved Pokemon,")
print("The third round of selection is selecting a legendary Pokemon")
print("After the selection phase, here comes the battle phase")
print("The game will pair the Pokemon in the same group (e.g., Juvenile vs Juvenile)")
print("Players will have the choice to select a potion that will affect the stats of their Pokemon as well as their oponent's")
print("After that, both Pokemon will attack each other.")
print("The damage dealt can be decreased, increased or remain the same depending on the type of Pokemon")
print("The winner of the round will be determined based on who has the greater power?? remaining.")
print("After the battle, the system will adjust the health of both Pokemon.")
print("The winner will gain health while the loser will lose health")
print("The fatigue factor will also be instilled on both pokemon which decrease their health.")
print("The battle phase will go on until one player has no more Pokemon to battle")
print("The winner will be determined on who has the most wins.")

print("Now you know how this works. Let us get started")

def Main():
    dtype = np.dtype([
        ("ID", "i4"),
        ("Name", "U20"),
        ("Health", "i4"),
        ("Power", "i4"),
        ("Type", "U20"),
        ("Stage", "i4")
    ])

    Pokemon_list = np.array([
        (1, "Ursaring", 90, 130, "Normal", 1), 
        (2, "Snorlax", 160, 110, "Normal", 2), 
        (3, "Regigigas", 110, 115, "Normal", 3),
        (4, "Growlithe", 55, 70, "Fire", 1),
        (5, "Darmanitan", 105, 140, "Fire", 2),
        (6, "Entei", 113, 115, "Fire", 3),
        (7, "Drizzile", 65, 60, "Water", 1), 
        (8, "Samurott", 95, 100, "Water", 2), 
        (9, "Kyogre", 100, 105, "Water", 3),
        (10, "Luxio", 60, 85, "Electric", 1), 
        (11, "Electivire", 75, 123, "Electric", 2), 
        (12, "Zeraora", 88, 112, "Electric", 3),
        (13, "Grovyle", 50, 65, "Grass", 1), 
        (14, "Rillaboom", 100, 125, "Grass", 2), 
        (15, "Ogerpon", 80, 120, "Grass", 3),
        (16, "Machop", 70, 80, "Fighting", 1), 
        (17, "Sawk", 75, 125, "Fighting", 2), 
        (18, "Zamazenta", 92, 130, "Fighting", 3),
        (19, "Nidorino", 61, 70, "Poison", 1), 
        (20, "Weezing", 65, 90, "Poison", 2), 
        (21, "Poipole", 67, 108, "Poison", 3),
        (22, "Trapinch", 45, 100, "Ground", 1), 
        (23, "Sandaconda", 72, 107, "Ground", 2), 
        (24, "Groudon", 100, 150, "Ground", 3),
        (25, "Cubchoo", 55, 70, "Ice", 1), 
        (26, "Avalugg", 95, 117, "Ice", 2), 
        (27, "Glastrier", 100, 145, "Ice", 3),
        (28, "Clefairy", 70, 45, "Fairy", 1), 
        (29, "Florges", 78, 65, "Fairy", 2), 
        (30, "Xerneas", 126, 131, "Fairy", 3)
    ], dtype=dtype)

    player_1_queue = [] 
    player_2_queue = []


    #The following uses arrays as storage for used health and poison potions
    player_1_used_health_potions = arr.array('i', [])
    player_1_used_poison_potions = arr.array('i', [])
    player_2_used_health_potions = arr.array('i', [])
    player_2_used_poison_potions = arr.array('i', [])

    header_selected_pokemon = ["Pokemon ID", "Name", "Health", "Power", "Type"]

    class Pokemon_Storage:
        def __init__(self):
            self.head = None

        def view_pokemon(self):
            list_preview = []
            current = self.head
            while current is not None:
                list_preview.append([f"{current.data[0]}", f"{current.data[1]}", f"{current.data[2]}", f"{current.data[3]}", f"{current.data[4]}",])
                current = current.next
            table_list = tb.tabulate(list_preview, headers=header_selected_pokemon, tablefmt= "pretty")
            print(table_list)

        def insert(self, newdata):
            NewNode = Node(newdata)
            if self.head is None:
                self.head = NewNode
                return
            else:
                lastnode = self.head
                while lastnode.next:
                    lastnode = lastnode.next
                lastnode.next = NewNode
            
        def resetnode(self):
            self.head = None
        
        def printlist(self):
            printmoko = self.head
            while printmoko is not None:
                print(printmoko.data)
                printmoko = printmoko.next

        def insert_to_queue(self, identifier):
            if identifier % 2 != 0:
                current = self.head
                while current.next != None:
                    player_1_queue.append(current.data)
                    current = current.next
                player_1_queue.append(current.data)
            else:
                current = self.head
                while current.next != None:
                    player_2_queue.append(current.data)
                    current = current.next
                player_2_queue.append(current.data)


    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    


    player_1_storage = Pokemon_Storage()
    player_2_storage = Pokemon_Storage()

    while True:
        player_1_coinside = (input(f"\n{player_1}, Heads (H) or Tails (T)?: ")).upper()
        if player_1_coinside == "H":
            player_2_coinside = "T"
            print(f"If {player_1} is heads, then {player_2} is tails")
            break
        elif player_1_coinside == "T":
            player_2_coinside = "H"
            print(f"If {player_1} is tails, then {player_2} is heads")
            break
        else:
            print("Invalid input, H for heads and T for tails only. Try again")
    
    coin = ["H", "T"]
    side = rd.choice(coin)
    if side == "H":
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
    
    selected_pokemon = []
    
    stage = {
        1: "Juvenile",
        2: "Fully Evolved",
        3: "Legendary" 
    }
    count = 1
    while count <= 3:
        if turn_indicator[f"{player_1}"] == side:
            pokemon_preview_list = []
            header_pokemon_list = ["Pokemon ID", "Pokemon", "Type"]
            print(f"{stage[count]} Pokemon:")
            for i in Pokemon_list["ID"]:
                if Pokemon_list[Pokemon_list["ID"] == i][0][5] == count:
                    if Pokemon_list[Pokemon_list["ID"] == i][0][0] not in selected_pokemon:
                        pokemon_preview_list.append([f"{Pokemon_list[Pokemon_list["ID"] == i][0][0]}", f"{Pokemon_list[Pokemon_list["ID"] == i][0][1]}", f"{Pokemon_list[Pokemon_list["ID"] == i][0][4]}"])
                    else:
                        pass
                else:
                    pass
            table_list = tb.tabulate(pokemon_preview_list, headers=header_pokemon_list, tablefmt= "pretty")
            print(table_list)
            selection = PF.Selecting_Pokemon(player_1, count, dtype, Pokemon_list, stage, selected_pokemon)
            extracted_pokemon = selection.Selecting()
            
            player_1_storage.insert(list(extracted_pokemon[0]))
            selected_pokemon.append(extracted_pokemon[0][0])


            pokemon_preview_list.clear()
            for i in Pokemon_list["ID"]:
                if Pokemon_list[Pokemon_list["ID"] == i][0][5] == count:
                    if Pokemon_list[Pokemon_list["ID"] == i][0][0] not in selected_pokemon:
                        pokemon_preview_list.append([f"{Pokemon_list[Pokemon_list["ID"] == i][0][0]}", f"{Pokemon_list[Pokemon_list["ID"] == i][0][1]}", f"{Pokemon_list[Pokemon_list["ID"] == i][0][4]}"])
                    else:
                        pass
                else:
                    pass
            table_list = tb.tabulate(pokemon_preview_list, headers=header_pokemon_list, tablefmt= "pretty")
            print(table_list)
            selection = PF.Selecting_Pokemon(player_2, count, dtype, Pokemon_list, stage, selected_pokemon)
            extracted_pokemon = selection.Selecting()
            
            player_2_storage.insert(list(extracted_pokemon[0]))
            selected_pokemon.append(extracted_pokemon[0][0])

            pokemon_preview_list.clear()
            count += 1
        else:
            pokemon_preview_list = []
            header_pokemon_list = ["Pokemon ID", "Pokemon", "Type"]
            print(f"{stage[count]} Pokemon:")
            for i in Pokemon_list["ID"]:
                if Pokemon_list[Pokemon_list["ID"] == i][0][5] == count:
                    if Pokemon_list[Pokemon_list["ID"] == i][0][0] not in selected_pokemon:
                        pokemon_preview_list.append([f"{Pokemon_list[Pokemon_list["ID"] == i][0][0]}", f"{Pokemon_list[Pokemon_list["ID"] == i][0][1]}", f"{Pokemon_list[Pokemon_list["ID"] == i][0][4]}"])
                    else:
                        pass
                else:
                    pass
            table_list = tb.tabulate(pokemon_preview_list, headers=header_pokemon_list, tablefmt= "pretty")
            print(table_list)
            selection = PF.Selecting_Pokemon(player_2, count, dtype, Pokemon_list, stage, selected_pokemon)
            extracted_pokemon = selection.Selecting()
            
            player_2_storage.insert(list(extracted_pokemon[0]))
            selected_pokemon.append(extracted_pokemon[0][0])

            pokemon_preview_list.clear()
            for i in Pokemon_list["ID"]:
                if Pokemon_list[Pokemon_list["ID"] == i][0][5] == count:
                    if Pokemon_list[Pokemon_list["ID"] == i][0][0] not in selected_pokemon:
                        pokemon_preview_list.append([f"{Pokemon_list[Pokemon_list["ID"] == i][0][0]}", f"{Pokemon_list[Pokemon_list["ID"] == i][0][1]}", f"{Pokemon_list[Pokemon_list["ID"] == i][0][4]}"])
                    else:
                        pass
                else:
                    pass
            table_list = tb.tabulate(pokemon_preview_list, headers=header_pokemon_list, tablefmt= "pretty")
            print(table_list)
            selection = PF.Selecting_Pokemon(player_1, count, dtype, Pokemon_list, stage, selected_pokemon)
            extracted_pokemon = selection.Selecting()
            
            player_1_storage.insert(list(extracted_pokemon[0]))
            selected_pokemon.append(extracted_pokemon[0][0])
            
            pokemon_preview_list.clear()
            
            count += 1
    print(f"{player_1}'s Pokemon")
    player_1_storage.view_pokemon()

    print(f"{player_2}'s Pokemon")
    player_2_storage.view_pokemon()

    i = 1
    player_1_storage.insert_to_queue(i)
    i = 2
    player_2_storage.insert_to_queue(i)
    
    
    player_1_win_count = 0 
    player_2_win_count = 0 
    draw_count = 0

    class Tree:
        def __init__(self, val):
            self.root = val
        
        # Insert a new value into the tree
        def insert(self,newdata):
            NewNode = newdata
            current = self.root
            while current.left != None or current.right != None:
                if current.left != None and current.right == None:
                    current = current.left
                elif current.left == None and current.right != None:
                    current = current.right
            if NewNode.data == f"{player_1} wins":
                current.left = NewNode
                print(f"{current.left.data}")
            elif NewNode.data == f"{player_2} wins":
                current.right = NewNode
                print(f"{current.right.data}")
            else:
                pass
        
        def count(self, player_1_win_count, player_2_win_count):
            current = self.root
            while current.left != None or current.right != None:
                if current.left != None and current.right == None:
                    player_1_win_count += 1
                    current = current.left
                elif current.left == None and current.right != None:
                    player_2_win_count += 1
                    current = current.right
            else:
                pass
            return [player_1_win_count, player_2_win_count]
            
                
    class Status_Node:
            def __init__(self, data):
                self.data = data
                self.left = None
                self.right = None
    
    t = Tree(Status_Node("Winner/Loser Count"))


    p1_potion_stack = []
    p2_potion_stack = []

    def push(player, value):
        if player == player_1:
            p1_potion_stack.append(value)
        else: 
            p2_potion_stack.append(value)

    def potion_purchase(player, potions, points=35):
        while True:
            try:
                print(f"Current points: {points}")
                print("Enter '10' to end purchasing")
                select = int(input(f"{player}, buy a potion by inputting their corresponding ID: "))
                if select == 1:
                    if points >= potions[0][3]:
                        print("Purchase successful. Added to storage")
                        push(player, potions[0])
                        points -= potions[0][3]
                    else:
                        print("Not enough points. Select a different one")
                elif select == 2:
                    if points >= potions[1][3]:
                        print("Purchase successful. Added to storage")
                        push(player, potions[1])
                        points -= potions[1][3]
                    else:
                        print("Not enough points. Select a different one")
                elif select == 3:
                    if points >= potions[2][3]:
                        print("Purchase successful. Added to storage")
                        push(player, potions[2])
                        points -= potions[2][3]
                    else:
                        print("Not enough points. Select a different one")
                elif select == 4:
                    if points >= potions[3][3]:
                        print("Purchase successful. Added to storage")
                        push(player, potions[3])
                        points -= potions[3][3]
                    else:
                        print("Not enough points. Select a different one")
                elif select == 5:
                    if points >= potions[4][3]:
                        print("Purchase successful. Added to storage")
                        push(player, potions[4])
                        points -= potions[4][3]
                    else:
                        print("Not enough points. Select a different one")
                elif select == 10:
                    option = input("Are you sure to end your purchase? Y for yes or any key for no: ").upper()
                    if option == "Y":
                        break
                    else:
                        print("returning to shop")
                else:
                    print("ID does not exist. Try again")
            except ValueError:
                print('Error: Invalid Input. Try again')


    potions = [
        [1, "Normal Health Potion", "Increases health of current Pokemon by 45", 5],
        [2, "Advanced Health Potion", "Increases health of current Pokemon by 65", 12],
        [3, "Normal Poison Potion", "Increases health of current Pokemon by 20", 6],
        [4, "Advanced Poison Potion", "Increases health of current Pokemon by 35", 9],
        [5, "Enhancement Potion", "Temporarily increases power ofcurrent Pokemon by 15", 3]
        ]
    header_potions = ["ID", "Potion name", "Effect", "Cost"]
    table_potion = tb.tabulate(potions, headers=header_potions, tablefmt= "pretty")
    print(f"Potion Shop: Buy your desired potions.\nEMINDER: The use of which potion is based on First In, Last Out\n Strategize the use of potions carefully")
    print(table_potion)

    potion_purchase(player_1, potions)
    potion_purchase(player_2, potions)
       
    Battle_Summary_1 = [] 
    Battle_Summary_2 = []
    header_battle_summary_1 = ["Battle Number", f"{player_1}'s Pokemon (ID) Name", "Damaged Health", "Power",  "Type", "Potion Used"]
    header_battle_summary_2 = [f"{player_2}'s Pokemon (ID) Name", "Damaged Health", "Power", "Type", "Potion Used", "Status"]

    battle_number = 1
    while True:
        print(f"For Battle No. {battle_number}")
        battle = PF.Battle_Simulation()
        battle_queue = [battle.dequeue_pokemon(player_1, player_1_queue, player_2, player_2_queue), 
                        battle.potion_phase, 
                        battle.battle_phase, 
                        battle.decision_phase,
                        battle.adjusting_health, 
                        battle.checking_remaining_pokemon]
        pairing = battle_queue.pop(0)

        potion_selection = battle_queue.pop(0)(player_1, pairing[0], player_2, pairing[1], 
                                            p1_potion_stack, 
                                            p2_potion_stack
                                            )
        

        battle_phase = battle_queue.pop(0)(player_1, potion_selection[0], player_2, potion_selection[1], potion_selection[4], potion_selection[5])

        decision_phase = battle_queue.pop(0)(player_1, battle_phase[0], player_2, battle_phase[1], draw_count)

        print("\nBattle Summary:")
        Battle_Summary_1.append([battle_number,f"{battle_phase[0][0]} {battle_phase[0][1]}", f"{battle_phase[2]}", f"{battle_phase[0][3]}", f"{battle_phase[0][4]}", f"{potion_selection[2]}"])
        table_summary_1 = tb.tabulate(Battle_Summary_1, headers=header_battle_summary_1, tablefmt= "pretty")
        print(table_summary_1)

        Battle_Summary_2.append([f"{battle_phase[1][0]} {battle_phase[1][1]}", f"{battle_phase[3]}", f"{battle_phase[1][3]}", f"{battle_phase[1][4]}", f"{potion_selection[3]}", f"{decision_phase[3]}"])
        table_summary_2 = tb.tabulate(Battle_Summary_2, headers=header_battle_summary_2, tablefmt= "pretty")
        print(table_summary_2)
        input("Enter to continue")

        health_adjustment = battle_queue.pop(0)(player_1, decision_phase[0], player_2, decision_phase[1], decision_phase[3])

        check_health = battle_queue.pop(0)(player_1, health_adjustment[0], player_2, health_adjustment[1])

        t.insert(Status_Node(decision_phase[3]))
        
        if check_health[0][2] > 0:
            player_1_queue.append(check_health[0])
        else:
            pass
        
        if check_health[1][2] > 0:
            player_2_queue.append(check_health[1])
        else:
            pass
        
        if len(player_1_queue) != 0:
            pass
        else:
            print(f"\n{player_1} Does not have any Pokemon left to battle. The battle is over")
            break

        if len(player_2_queue) != 0:
            pass
        else:
            print(f"\n{player_2} Does not have any Pokemon left to battle. The battle is over")
            break
        battle_number += 1
    
    overall_win_count = t.count(player_1_win_count, player_2_win_count)


    if overall_win_count[0] > overall_win_count[1]:
        print(f"{player_1} is the Overall Winner!")
    elif overall_win_count[0] < overall_win_count[1]:
        print(f"{player_1} is the Overall Winner!")
    else:
        print(f"It is a tie!")
    print(f"{player_1}' win count: {overall_win_count[0]} | {player_2}' win count: {overall_win_count[1]}")
    while True:
        play_again = input("Would you guys like to play again? (Yes or No): ").lower()
        if play_again == "yes":
            Main()
        elif play_again == "no":
            print("Thank you for playing")
            break
        else:
            print("Yes or No only")

Main()
