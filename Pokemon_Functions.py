import random as rd
import tabulate as tb

class Selecting_Pokemon:
    def __init__(self, player, count, dtype, Pokemon_list, stage, selected_pokemon):
        self.player = player
        self.count = count
        self.dtype = dtype
        self.Pokemon_list = Pokemon_list
        self.stage = stage
        self.selected_pokemon = selected_pokemon
    
    def Selecting(self):
        while True:
            try:
                choice = int(input(f"{self.player}, choose your {self.stage[self.count]} Pokemon: "))
                if choice in self.Pokemon_list["ID"]:
                    if self.Pokemon_list[self.Pokemon_list["ID"] == choice][0][5] == self.count:
                        if choice not in self.selected_pokemon:
                            print(f"{self.player} selected {self.Pokemon_list[self.Pokemon_list["ID"] == choice][0][1]}. {self.Pokemon_list[self.Pokemon_list["ID"] == choice][0][1]} is now unavailable.\n")
                            break
                        else:
                            print("This Pokemon is not available. Select again\n")
                    else:
                        print(f"Select a {self.stage[self.count]} Pokemon")
                else:
                    print("This Pokemon does not exist. Select again\n")
            except ValueError:
                print("Choose a Pokemon by entering their corresponding number\n")
        return self.Pokemon_list[self.Pokemon_list["ID"] == choice]

class Battle_Simulation:
    def __init__(self):
        return
    def dequeue_pokemon(self, player_1, player_1_queue, player_2, player_2_queue):
        print(f"")
        player_1_current = player_1_queue.pop(0)
        player_2_current = player_2_queue.pop(0)
        display_selected_1 = []
        display_selected_2 = []
        header_display = ["Pokemon ID", "Pokemon Name", "Health", "Power", "Type"]
        display_selected_1.append([f"{player_1_current[0]}", f"{player_1_current[1]}", f"{player_1_current[2]}", f"{player_1_current[3]}", f"{player_1_current[4]}",])
        display_selected_2.append([f"{player_2_current[0]}", f"{player_2_current[1]}", f"{player_2_current[2]}", f"{player_2_current[3]}", f"{player_2_current[4]}",])
        print(f"{player_1}")
        table_list_1 = tb.tabulate(display_selected_1, headers=header_display, tablefmt= "pretty")
        print(table_list_1)
        print("VS")
        print(f"{player_2}")
        table_list_2 = tb.tabulate(display_selected_2, headers=header_display, tablefmt= "pretty")
        print(table_list_2)
        display_selected_1.clear()
        display_selected_2.clear()
        input("Enter to continue:")
        return [player_1_current, player_2_current]
    
    def potion_phase(self, player_1, player_1_current, player_2, player_2_current, p1_potion_stack, p2_potion_stack):
        base_power1 = player_1_current[3]
        base_power2 = player_2_current[3]
        while True:
            if len(p1_potion_stack) != 0:
                current_potion1 = p1_potion_stack.pop(-1)
                print(f"{player_1}, do you wish to use your current potion {current_potion1[1]}")
                p1_choice  = input("Yes or No?: ").lower().capitalize()
                if p1_choice == "Yes":
                    if current_potion1[0] == 1:
                        print(f"{player_1} used Normal Health Potion {player_1_current[1]}'s health increased by 45")
                        player_1_current[2] += 45
                    elif current_potion1[0] == 2:
                        print(f"{player_1} used Normal Health Potion {player_1_current[1]}'s health increased by 65")
                        player_1_current[2] += 65
                    elif current_potion1[0] == 3:
                        print(f"{player_1} used Normal Poison Potion {player_2_current[1]}'s health decreased by 20")
                        player_2_current[2] -= 20
                    elif current_potion1[0] == 4:
                        print(f"{player_1} used Normal Poison Potion {player_2_current[1]}'s health decreased by 35")
                        player_2_current[2] -= 35
                    elif current_potion1[0] == 5:
                        print(f"{player_1} used Enhancement Potion {player_1_current[1]}'s Power temporarily by 15")
                        player_1_current[3] += 15
                    pchoice1 = current_potion1[1]
                    break
                elif p1_choice == "No":
                    pchoice1 = "None"
                    p1_potion_stack.append(current_potion1)
                    break
                else:
                    print("Yes or No Only")
                    p1_potion_stack.append(current_potion1)

        while True:
            if len(p2_potion_stack) != 0:
                current_potion2 = p2_potion_stack.pop(-1)
                print(f"{player_2}, do you wish to use your current potion {current_potion2[1]}")
                p1_choice  = input("Yes or No?: ").lower().capitalize()
                if p1_choice == "Yes":
                    if current_potion2[0] == 1:
                        print(f"{player_2} used Normal Health Potion {player_2_current[1]}'s health increased by 45")
                        player_1_current[2] += 45
                    elif current_potion2[0] == 2:
                        print(f"{player_2} used Normal Health Potion {player_2_current[1]}'s health increased by 65")
                        player_1_current[2] += 65
                    elif current_potion2[0] == 3:
                        print(f"{player_2} used Normal Poison Potion {player_1_current[1]}'s health decreased by 20")
                        player_2_current[2] -= 20
                    elif current_potion2[0] == 4:
                        print(f"{player_2} used Normal Poison Potion {player_1_current[1]}'s health decreased by 35")
                        player_2_current[2] -= 35
                    elif current_potion2[0] == 5:
                        print(f"{player_2} used Enhancement Potion {player_2_current[1]}'s Power temporarily by 15")
                        player_1_current[3] += 15
                    pchoice2 = current_potion2[1]
                    break
                elif p1_choice == "No":
                    pchoice2 = "None"
                    p2_potion_stack.append(current_potion2)
                    break
                else:
                    print("Yes or No ONly")
                    p2_potion_stack.append(current_potion2)
        
        return [player_1_current, player_2_current, pchoice1, pchoice2, base_power1, base_power2]

    
    def battle_phase(self, player_1, player_1_current, player_2, player_2_current, base_power1, base_power2):
        def damage_multiplier(player, curr_pokemon_1, curr_pokemon_2):
            if player == player_1:
                if curr_pokemon_1[4] == "Normal":
                    if curr_pokemon_2[4] in ["Fighting"]:
                        print(f"{curr_pokemon_1[1]} is weak against {curr_pokemon_2[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_1[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_1[1]} is not weak or strong against {curr_pokemon_2[1]}. Damage multiplier is neutral")
                        return curr_pokemon_1[3] * rd.uniform(0.22, 0.28)
                elif curr_pokemon_1[4] == "Fire":
                    if curr_pokemon_2[4] in ["Grass", "Ice"]:
                        print(f"{curr_pokemon_1[1]} is strong against {curr_pokemon_2[1]}. Strong Damage dealt will be increased")
                        return curr_pokemon_1[3] * rd.uniform(0.30, 0.40)
                    elif curr_pokemon_2[4] in ["Water", "Fire"]:
                        print(f"{curr_pokemon_1[1]} is weak against {curr_pokemon_2[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_1[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_1[1]} is not weak or strong against {curr_pokemon_2[1]}. Damage multiplier is neutral")
                        return curr_pokemon_1[3] * rd.uniform(0.22, 0.28)
                elif curr_pokemon_1[4] == "Water":
                    if curr_pokemon_2[4] in ["Fire", "Ground"]:
                        print(f"{curr_pokemon_1[1]} is strong against {curr_pokemon_2[1]}. Strong Damage dealt will be increased")
                        return curr_pokemon_1[3] * rd.uniform(0.30, 0.40)
                    elif curr_pokemon_2[4] in ["Grass", "Water"]:
                        print(f"{curr_pokemon_1[1]} is weak against {curr_pokemon_2[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_1[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_1[1]} is not weak or strong against {curr_pokemon_2[1]}. Damage multiplier is neutral")
                        return curr_pokemon_1[3] * rd.uniform(0.22, 0.28)
                elif curr_pokemon_1[4] == "Electric":
                    if curr_pokemon_2[4] in ["Water"]:
                        print(f"{curr_pokemon_1[1]} is strong against {curr_pokemon_2[1]}. Strong Damage dealt will be increased")
                        return curr_pokemon_1[3] * rd.uniform(0.30, 0.40)
                    elif curr_pokemon_2[4] in ["Grass", "Ground"]:
                        print(f"{curr_pokemon_1[1]} is weak against {curr_pokemon_2[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_1[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_1[1]} is not weak or strong against {curr_pokemon_2[1]}. Damage multiplier is neutral")
                        return curr_pokemon_1[3] * rd.uniform(0.22, 0.28)
                elif curr_pokemon_1[4] == "Grass":
                    if curr_pokemon_2[4] in ["Ground"]:
                        print(f"{curr_pokemon_1[1]} is strong against {curr_pokemon_2[1]}. Strong Damage dealt will be increased")
                        return curr_pokemon_1[3] * rd.uniform(0.30, 0.40)
                    elif curr_pokemon_2[4] in ["Fire", "Poison"]:
                        print(f"{curr_pokemon_1[1]} is weak against {curr_pokemon_2[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_1[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_1[1]} is not weak or strong against {curr_pokemon_2[1]}. Damage multiplier is neutral")
                        return curr_pokemon_1[3] * rd.uniform(0.22, 0.28)
                elif curr_pokemon_1[4] == "Fighting":
                    if curr_pokemon_2[4] in ["Ice", "Normal"]:
                        print(f"{curr_pokemon_1[1]} is strong against {curr_pokemon_2[1]}. Strong Damage dealt will be increased")
                        return curr_pokemon_1[3] * rd.uniform(0.30, 0.40)
                    elif curr_pokemon_2[4] in ["Poison", "Fairy"]:
                        print(f"{curr_pokemon_1[1]} is weak against {curr_pokemon_2[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_1[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_1[1]} is not weak or strong against {curr_pokemon_2[1]}. Damage multiplier is neutral")
                        return curr_pokemon_1[3] * rd.uniform(0.22, 0.28)
                elif curr_pokemon_1[4] == "Poison":
                    if curr_pokemon_2[4] in ["Grass", "Fairy"]:
                        print(f"{curr_pokemon_1[1]} is strong against {curr_pokemon_2[1]}. Strong Damage dealt will be increased")
                        return curr_pokemon_1[3] * rd.uniform(0.30, 0.40)
                    elif curr_pokemon_2[4] in ["Ground"]:
                        print(f"{curr_pokemon_1[1]} is weak against {curr_pokemon_2[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_1[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_1[1]} is not weak or strong against {curr_pokemon_2[1]}. Damage multiplier is neutral")
                        return curr_pokemon_1[3] * rd.uniform(0.22, 0.28)
                elif curr_pokemon_1[4] == "Ground":
                    if curr_pokemon_2[4] in ["Electric"]:
                        print(f"{curr_pokemon_1[1]} is strong against {curr_pokemon_2[1]}. Strong Damage dealt will be increased")
                        return curr_pokemon_1[3] * rd.uniform(0.30, 0.40)
                    elif curr_pokemon_2[4] in ["Grass"]:
                        print(f"{curr_pokemon_1[1]} is weak against {curr_pokemon_2[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_1[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_1[1]} is not weak or strong against {curr_pokemon_2[1]}. Damage multiplier is neutral")
                        return curr_pokemon_1[3] * rd.uniform(0.22, 0.28)
                elif curr_pokemon_1[4] == "Ice":
                    if curr_pokemon_2[4] in ["Ground", "Grass"]:
                        print(f"{curr_pokemon_1[1]} is strong against {curr_pokemon_2[1]}. Strong Damage dealt will be increased")
                        return curr_pokemon_1[3] * rd.uniform(0.30, 0.40)
                    elif curr_pokemon_2[4] in ["Water", "Ice"]:
                        print(f"{curr_pokemon_1[1]} is weak against {curr_pokemon_2[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_1[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_1[1]} is not weak or strong against {curr_pokemon_2[1]}. Damage multiplier is neutral")
                        return curr_pokemon_1[3] * rd.uniform(0.22, 0.28)
                elif curr_pokemon_1[4] == "Fairy":
                    if curr_pokemon_2[4] in ["Fighting"]:
                        print(f"{curr_pokemon_1[1]} is strong against {curr_pokemon_2[1]}. Strong Damage dealt will be increased")
                        return curr_pokemon_1[3] * rd.uniform(0.30, 0.40)
                    elif curr_pokemon_2[4] in ["Fire", "Poison"]:
                        print(f"{curr_pokemon_1[1]} is weak against {curr_pokemon_2[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_1[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_1[1]} is not weak or strong against {curr_pokemon_2[1]}. Damage multiplier is neutral")
                        return curr_pokemon_1[3] * rd.uniform(0.22, 0.28)
                    
            elif player == player_2:
                if curr_pokemon_2[4] == "Normal":
                    if curr_pokemon_1[4] in ["Fighting"]:
                        print(f"{curr_pokemon_2[1]} is weak against {curr_pokemon_1[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_2[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_2[1]} is not weak or strong against {curr_pokemon_1[1]}. Damage multiplier is neutral")
                        return curr_pokemon_2[3] * rd.uniform(0.22, 0.28)
                elif curr_pokemon_2[4] == "Fire":
                    if curr_pokemon_1[4] in ["Grass", "Ice"]:
                        print(f"{curr_pokemon_2[1]} is strong against {curr_pokemon_1[1]}. Strong Damage dealt will be increased")
                        return curr_pokemon_2[3] * rd.uniform(0.30, 0.40)
                    elif curr_pokemon_1[4] in ["Water", "Fire"]:
                        print(f"{curr_pokemon_2[1]} is weak against {curr_pokemon_1[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_2[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_2[1]} is not weak or strong against {curr_pokemon_1[1]}. Damage multiplier is neutral")
                        return curr_pokemon_2[3] * rd.uniform(0.22, 0.28)
                elif curr_pokemon_2[4] == "Water":
                    if curr_pokemon_1[4] in ["Fire", "Ground"]:
                        print(f"{curr_pokemon_2[1]} is strong against {curr_pokemon_1[1]}. Strong Damage dealt will be increased")
                        return curr_pokemon_2[3] * rd.uniform(0.30, 0.40)
                    elif curr_pokemon_1[4] in ["Grass", "Water"]:
                        print(f"{curr_pokemon_2[1]} is weak against {curr_pokemon_1[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_2[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_2[1]} is not weak or strong against {curr_pokemon_1[1]}. Damage multiplier is neutral")
                        return curr_pokemon_2[3] * rd.uniform(0.22, 0.28)
                elif curr_pokemon_2[4] == "Electric":
                    if curr_pokemon_1[4] in ["Water"]:
                        print(f"{curr_pokemon_2[1]} is strong against {curr_pokemon_1[1]}. Strong Damage dealt will be increased")
                        return curr_pokemon_2[3] * rd.uniform(0.30, 0.40)
                    elif curr_pokemon_1[4] in ["Grass", "Ground"]:
                        print(f"{curr_pokemon_2[1]} is weak against {curr_pokemon_1[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_2[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_2[1]} is not weak or strong against {curr_pokemon_1[1]}. Damage multiplier is neutral")
                        return curr_pokemon_2[3] * rd.uniform(0.22, 0.28)
                elif curr_pokemon_2[4] == "Grass":
                    if curr_pokemon_1[4] in ["Ground", "Water"]:
                        print(f"{curr_pokemon_2[1]} is strong against {curr_pokemon_1[1]}. Strong Damage dealt will be increased")
                        return curr_pokemon_2[3] * rd.uniform(0.30, 0.40)
                    elif curr_pokemon_1[4] in ["Fire", "Poison"]:
                        print(f"{curr_pokemon_2[1]} is weak against {curr_pokemon_1[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_2[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_2[1]} is not weak or strong against {curr_pokemon_1[1]}. Damage multiplier is neutral")
                        return curr_pokemon_2[3] * rd.uniform(0.22, 0.28)
                elif curr_pokemon_2[4] == "Fighting":
                    if curr_pokemon_1[4] in ["Ice", "Normal"]:
                        print(f"{curr_pokemon_2[1]} is strong against {curr_pokemon_1[1]}. Strong Damage dealt will be increased")
                        return curr_pokemon_2[3] * rd.uniform(0.30, 0.40)
                    elif curr_pokemon_1[4] in ["Poison", "Fairy"]:
                        print(f"{curr_pokemon_2[1]} is weak against {curr_pokemon_1[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_2[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_2[1]} is not weak or strong against {curr_pokemon_1[1]}. Damage multiplier is neutral")
                        return curr_pokemon_2[3] * rd.uniform(0.22, 0.28)
                elif curr_pokemon_2[4] == "Poison":
                    if curr_pokemon_1[4] in ["Grass", "Fairy"]:
                        print(f"{curr_pokemon_2[1]} is strong against {curr_pokemon_1[1]}. Strong Damage dealt will be increased")
                        return curr_pokemon_2[3] * rd.uniform(0.30, 0.40)
                    elif curr_pokemon_1[4] in ["Ground"]:
                        print(f"{curr_pokemon_2[1]} is weak against {curr_pokemon_1[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_2[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_2[1]} is not weak or strong against {curr_pokemon_1[1]}. Damage multiplier is neutral")
                        return curr_pokemon_2[3] * rd.uniform(0.22, 0.28)
                elif curr_pokemon_2[4] == "Ground":
                    if curr_pokemon_1[4] in ["Electric"]:
                        print(f"{curr_pokemon_2[1]} is strong against {curr_pokemon_1[1]}. Strong Damage dealt will be increased")
                        return curr_pokemon_2[3] * rd.uniform(0.30, 0.40)
                    elif curr_pokemon_1[4] in ["Grass"]:
                        print(f"{curr_pokemon_2[1]} is weak against {curr_pokemon_1[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_2[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_2[1]} is not weak or strong against {curr_pokemon_1[1]}. Damage multiplier is neutral")
                        return curr_pokemon_2[3] * rd.uniform(0.22, 0.28)
                elif curr_pokemon_2[4] == "Ice":
                    if curr_pokemon_1[4] in ["Grass", "Ground"]:
                        print(f"{curr_pokemon_2[1]} is strong against {curr_pokemon_1[1]}. Strong Damage dealt will be increased")
                        return curr_pokemon_2[3] * rd.uniform(0.30, 0.40)
                    elif curr_pokemon_1[4] in ["Water", "Ice"]:
                        print(f"{curr_pokemon_2[1]} is weak against {curr_pokemon_1[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_2[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_2[1]} is not weak or strong against {curr_pokemon_1[1]}. Damage multiplier is neutral")
                        return curr_pokemon_2[3] * rd.uniform(0.22, 0.28)
                elif curr_pokemon_2[4] == "Fairy":
                    if curr_pokemon_1[4] in ["Fighting"]:
                        print(f"{curr_pokemon_2[1]} is strong against {curr_pokemon_1[1]}. Strong Damage dealt will be increased")
                        return curr_pokemon_2[3] * rd.uniform(0.30, 0.40)
                    elif curr_pokemon_1[4] in ["Fire", "Poison"]:
                        print(f"{curr_pokemon_2[1]} is weak against {curr_pokemon_1[1]}. Weak damage multiplier will be applied")
                        return curr_pokemon_2[3] * rd.uniform(0.10, 0.20)
                    else:
                        print(f"{curr_pokemon_2[1]} is not weak or strong against {curr_pokemon_1[1]}. Damage multiplier is neutral")
                        return curr_pokemon_2[3] * rd.uniform(0.22, 0.28)
     
        
        p1_damage = int(damage_multiplier(player_1, player_1_current, player_2_current))
        player_2_current[2] -= p1_damage
        print(f"\n{player_1_current[1]} attacks {player_2_current[1]}. It dealt {p1_damage} damage!")
        
        print(f"{player_2_current[1]}'s new health: {player_2_current[2]}")
        

        p2_damage = int(damage_multiplier(player_2, player_1_current, player_2_current))
        player_1_current[2] -= p2_damage

        print(f"\n{player_2_current[1]} attacks {player_1_current[1]}. It dealt {p2_damage} damage!")
        
        print(f"{player_1_current[1]}'s new health: {player_1_current[2]}")
     
        p1_health_result = player_1_current[2]
        p2_health_result = player_2_current[2]

        player_1_current[3] = base_power1
        player_2_current[3] = base_power2

        input("Enter to continue")
        return [player_1_current, player_2_current, p1_health_result, p2_health_result]
    
    def decision_phase(self, player_1, player_1_current, player_2, player_2_current, draw_count):
        #Adjusts the Pokemon's health. The winner gains health while the loser loses health
        if player_1_current[2] > player_2_current[2]:
            print(f"\n{player_1} wins this round")
            
            status = f"{player_1} wins"
            print(f"{player_1_current[1]} health increases while {player_2_current[1]} health decreases")

        elif player_1_current[2] == player_2_current[2]:
            draw_count += 1
            print(f"\nIt's a draw! No increase or decrease in health on both Pokemon due to draw")
            
            status = "Draw"
   
        else:
            print(f"\n{player_2} wins this round")
            
            status = f"{player_2} wins"
            print(f"{player_2_current[1]} health increases while {player_1_current[1]} health decreases")

        return [player_1_current, player_2_current, draw_count, status]

    def adjusting_health(self, player_1, player_1_current, player_2, player_2_current, status):

        heatlh_increase_roll = rd.randint(5,10)
        heatlh__decrease_roll = rd.randint(4,8)
        fatigue_roll = rd.randint(2, 4)

        if status == f"{player_1} wins":
            player_1_current[2] += heatlh_increase_roll
            player_2_current[2] -= heatlh__decrease_roll

        elif status == "Draw":
            pass
        
        else:
            player_2_current[2] += heatlh_increase_roll
            player_1_current[2] -= heatlh__decrease_roll
            
        #After health adjustments, the program will decrease both Pokemon's health due to fatigue
        print(f"\nPokemon's health decreases due to fatigue")
        
        player_1_current[2] -= fatigue_roll
        player_2_current[2] -= fatigue_roll

        print(f"{player_1_current[1]}'s new health: {player_1_current[2]} | {player_2_current[1]}'s new health: {player_2_current[2]}")

        return [player_1_current, player_2_current]

       
   
    def checking_remaining_pokemon(self, player_1, player_1_current, player_2, player_2_current):
        print(f"For {player_1}:")
        if player_1_current[2] > 0:
            print(f"{player_1_current[1]} can keep going. Returning to queue")
            pass
        else:
            print(f"{player_1_current[1]}'s health reaches 0 or below. They are out!")

        print(f"For {player_2}:")
        if player_2_current[2] > 0:
            print(f"{player_2_current[1]} can keep going. Returning to queue")
            pass
        else:
            print(f"{player_2_current[1]}'s health reaches 0 or below. They are out!")
        
        input("Enter to continue")

        return[player_1_current, player_2_current]