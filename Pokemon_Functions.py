import random as rd
import time as t

#This class serves as a function for players to select their Pokemon
class Selecting_Pokemon:
    def __init__(self, player, count, player_mode_of_selection, Pokemon_ID, Pokemon_list, Health, Power, selected_pokemon):
        self.player = player
        self.count = count
        self.player_mode_of_selection = player_mode_of_selection
        self.Pokemon_ID = Pokemon_ID
        self.Pokemon_list = Pokemon_list
        self.Health = Health
        self.Power = Power
        self.selected_pokemon = selected_pokemon
    
    def Selecting(self):
            if self.player_mode_of_selection == "yes":
                print(f"The Computer is selecting {self.player}'s Pokemon {self.count}")
                while True:
                    choice = rd.choice(self.Pokemon_ID)
                    if choice not in self.selected_pokemon:
                        pinpointer = self.Pokemon_ID.index(choice)
                        print(f"{self.player} selected {self.Pokemon_list[pinpointer]}. {self.Pokemon_list[pinpointer]} is now unavailable.\n")
                        break
                    else:
                        pass
                t.sleep(2)
                return [self.Pokemon_ID[pinpointer], self.Health[pinpointer], self.Power[pinpointer]]
            
            else:
                while True:
                    try:
                        choice = int(input(f"{self.player}, choose your Pokemon {self.count}: "))
                        if choice in self.Pokemon_ID:
                            if choice not in self.selected_pokemon:
                                pinpointer = self.Pokemon_ID.index(choice)
                                print(f"{self.player} selected {self.Pokemon_list[pinpointer]}. {self.Pokemon_list[pinpointer]} is now unavailable.\n")
                                break
                            else:
                                print("This Pokemon is not available. Select again\n")
                        else:
                            print("This Pokemon does not exist. Select again\n")
                    except ValueError:
                        print("Choose a Pokemon by entering their corresponding number\n")
                t.sleep(1)
                return [self.Pokemon_ID[pinpointer], self.Health[pinpointer], self.Power[pinpointer]]

#This class serves as a function for battle simulation
class Battle_Simulation:
    def __init__(self, player_1_Pokemon_Storage, player_1_Pokemon_Health, player_1_Pokemon_Power, 
                        player_2_Pokemon_Storage, player_2_Pokemon_Health, player_2_Pokemon_Power, 
                        Health_Potions, Poison_Potions, player_1_used_health_potions, 
                        player_1_used_poison_potions, player_2_used_health_potions, player_2_used_poison_potions,
                        Pokemon_list, Pokemon_ID, player_1, player_2, player_1_win_count, player_1_lose_count, player_2_win_count, player_2_lose_count, draw_count):
        
        self.player_1_Pokemon_Storage = player_1_Pokemon_Storage
        self.player_1_Pokemon_Health = player_1_Pokemon_Health
        self.player_1_Pokemon_Power = player_1_Pokemon_Power
        self.player_2_Pokemon_Storage = player_2_Pokemon_Storage
        self.player_2_Pokemon_Health = player_2_Pokemon_Health
        self.player_2_Pokemon_Power = player_2_Pokemon_Power
        self.Health_Potions = Health_Potions
        self.Poison_Potions = Poison_Potions
        self.player_1_used_health_potions = player_1_used_health_potions
        self.player_1_used_poison_potions = player_1_used_poison_potions  
        self.player_2_used_health_potions = player_2_used_health_potions
        self.player_2_used_poison_potions = player_2_used_poison_potions  
        self.Pokemon_ID = Pokemon_ID
        self.Pokemon_list = Pokemon_list
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1_win_count = player_1_win_count
        self.player_1_lose_count = player_1_lose_count
        self.player_2_win_count = player_2_win_count
        self.player_2_lose_count = player_2_lose_count
        self.draw_count = draw_count
    
    def Versus(self):
        if self.player_1_Pokemon_Health.count(0) == 3 and self.player_2_Pokemon_Health.count(0) == 3:
            print("Both players do not have Pokemons left to battle. The battle is over")
            return None
        else:
            p1_pokemon_count = 0
            p1_pokemon_current_count = len(self.player_1_Pokemon_Storage)
            while p1_pokemon_count < p1_pokemon_current_count:
                p1 = rd.choice(self.player_1_Pokemon_Storage)
                index = self.player_1_Pokemon_Storage.index(p1)
                p1_health = self.player_1_Pokemon_Health[index]
                if p1_health <= 0:
                    self.player_1_Pokemon_Storage.pop(index)
                    self.player_1_Pokemon_Health.pop(index)
                    p1_pokemon_count += 1
                else:
                    p1_power = self.player_1_Pokemon_Power[index]
                    break
            else:
                print(f"\n{self.player_1} Does not have any Pokemon left to battle. The battle is over")
                t.sleep(2)
                return None

            p2_pokemon_count = 0
            p2_pokemon_current_count = len(self.player_2_Pokemon_Storage)
            while p2_pokemon_count < p2_pokemon_current_count:
                p2 = rd.choice(self.player_2_Pokemon_Storage)
                index = self.player_2_Pokemon_Storage.index(p2)
                p2_health = self.player_2_Pokemon_Health[index]
                if p2_health <= 0:
                    self.player_2_Pokemon_Storage.pop(index)
                    self.player_2_Pokemon_Health.pop(index)
                    p2_pokemon_count += 1
                else:
                    p2_power = self.player_2_Pokemon_Power[index]
                    break
            else:
                print(f"\n{self.player_2} Does not have any Pokemon left to battle. The battle is over")
                return None
        
        p1_pokemon_name = self.Pokemon_list[self.Pokemon_ID.index(p1)]
        p2_pokemon_name = self.Pokemon_list[self.Pokemon_ID.index(p2)]
        
        print("\nIt's time for a Pokemon Battle!!!")
        t.sleep(2)
        print(f"\n{p1_pokemon_name} (Health: {p1_health} | Power: {p1_power}) VS {p2_pokemon_name} (Health: {p2_health} | Power: {p2_power})")
        t.sleep(2)
        
        #This is where the program allows both players to select health and poison potions
        if len(self.player_1_used_health_potions) != 2:
            while True:
                hpotion1 = input(f"\n{self.player_1}, Do you want to use a health potion (Yes or No)?: ").lower()
                if hpotion1 == "yes":
                    try:
                        hchoice1 = int(input("Select one health potion (1: Normal Health Potion | 2: Advanced Health Potion): "))
                        if hchoice1 not in self.player_1_used_health_potions:
                            if hchoice1 == 1:
                                print(f"{self.player_1} used Normal Health Potion {p1_pokemon_name}' health increased by 55")
                                p1_health += 55
                                break
                            elif hchoice1 == 2:
                                print(f"{self.player_1} used Advanced Health Potion {p1_pokemon_name}' health increased by 65")
                                p1_health += 65
                                break
                            else:
                                print("Choose 1 and 2 only")
                        else:
                            print("You already used this potion. Select a different one")
                    except ValueError:
                        print("Choose a health potion by entering their corresponding number\n")
                elif hpotion1 == "no":
                    hchoice1 = "None"
                    break
                else:
                    print("Choose between Yes and No only.")
                t.sleep(2)
        else:
            hchoice1 = "None"
            print(f"{self.player_1} does not have available health potions.")
            t.sleep(2)
        if len(self.player_1_used_poison_potions) != 2:
            while True:
                ppotion1 = input(f"\n{self.player_1}, Do you want to use a poison potion (Yes or No)?: ").lower()
                if ppotion1 == "yes":
                    try:
                        pchoice1 = int(input("Select one poison potion (1: Normal Poison Potion | 2: Advanced Poison Potion): "))
                        if pchoice1 not in self.player_1_used_poison_potions:
                            if pchoice1 == 1:
                                print(f"{self.player_1} used Normal Poison Potion {p2_pokemon_name}' health decreased by 20")
                                p1_health -= 20
                                break
                            elif pchoice1 == 2:
                                print(f"{self.player_1} used Advanced Poison Potion {p2_pokemon_name}' health decreased by 35")
                                p1_health -= 35
                                break
                            else:
                                print("Choose 1 and 2 only")
                        else:
                            print("You already used this potion. Select a different one")
                    except ValueError:
                        print("Choose a health poison by entering their corresponding number\n")
                elif ppotion1 == "no":
                    pchoice1 = "None"
                    break
                else:
                    print("Choose between Yes and No only.")
                t.sleep(2)
        else:
            pchoice1 = "None"
            print(f"{self.player_1} does not have available poison potions.")
            t.sleep(2)
        if len(self.player_2_used_health_potions) != 2:
            while True:
                hpotion2 = input(f"\n{self.player_2}, Do you want to use a health potion (Yes or No)?: ").lower()
                if hpotion2 == "yes":
                    try:
                        hchoice2 = int(input("Select one health potion (1: Normal Health Potion | 2: Advanced Health Potion): "))
                        if hchoice2 not in self.player_2_used_health_potions:
                            if hchoice2 == 1:
                                print(f"{self.player_2} used Normal Health Potion {p1_pokemon_name}' health increased by 55")
                                p2_health += 55
                                break
                            elif hchoice2 == 2:
                                print(f"{self.player_2} used Advanced Health Potion {p1_pokemon_name}' health increased by 65")
                                p2_health += 65
                                break
                            else:
                                print("Choose 1 and 2 only")
                        else:
                            print("You already used this potion. Select a different one")
                    except ValueError:
                        print("Choose a health potion by entering their corresponding number\n")
                elif hpotion2 == "no":
                    hchoice2 = "None"
                    break
                else:
                    print("Choose between Yes and No only.")
                t.sleep(2)
        else:
            hchoice2 = "None"
            print(f"{self.player_2} does not have available health potions.")
            t.sleep(2)
        if len(self.player_2_used_poison_potions) != 2:
            while True:
                ppotion2 = input(f"\n{self.player_2}, Do you want to use a poison potion (Yes or No)?: ").lower()
                if ppotion2 == "yes":
                    try:
                        pchoice2 = int(input("Select one health potion (1: Normal Poison Potion | 2: Advanced Poison Potion): "))
                        if pchoice2 not in self.player_2_used_poison_potions:
                            if pchoice2 == 1:
                                print(f"{self.player_2} used Normal Poison Potion {p1_pokemon_name}' health decreased by 20")
                                p1_health -= 20
                                break
                            elif pchoice2 == 2:
                                print(f"{self.player_2} used Advanced Poison Potion {p1_pokemon_name}' health decreased by 35")
                                p1_health -= 35
                                break
                            else:
                                print("Choose 1 and 2 only")
                        else:
                            print("You already used this potion. Select a different one")
                    except ValueError:
                        print("Choose a health poison by entering their corresponding number\n")
                elif ppotion2 == "no":
                    pchoice2 = "None"
                    break
                else:
                    print("Choose between Yes and No only.")
                t.sleep(2)
        else:
            pchoice2 = "None"
            print(f"{self.player_2} does not have available poison potions.")
            t.sleep(2)
        
        if hchoice1 == 1:
            p1_hpotion = "Normal Health Potion"
        elif hchoice1 == 2:
            p1_hpotion = "Advance Health Potion"
        else:
            p1_hpotion = "None"

        if pchoice1 == 1:
            p1_ppotion = "Normal Poison Potion"
        elif pchoice1 == 2:
            p1_ppotion = "Advance Poison Potion"
        else:
            p1_ppotion = "None"

        if hchoice2 == 1:
            p2_hpotion = "Normal Health Potion"
        elif hchoice2 == 2:
            p2_hpotion = "Advance Health Potion"
        else:
            p2_hpotion = "None"

        if pchoice2 == 1:
            p2_ppotion = "Normal Poison Potion"
        elif pchoice2 == 2:
            p2_ppotion = "Advance Poison Potion"
        else:
            p2_ppotion = "None"
        
        attack_roll = rd.uniform(0.25, 0.45)
        p1_damage = int(p1_power * attack_roll)
        p2_health -= p1_damage
        print(f"\n{p1_pokemon_name} attacks {p2_pokemon_name}. It dealt {p1_damage} damage!")
        t.sleep(2)
        print(f"{p2_pokemon_name}'s new health: {p2_health}")

        p2_damage = int(p2_power * attack_roll)
        p1_health -= p2_damage

        print(f"\n{p2_pokemon_name} attacks {p1_pokemon_name}. It dealt {p2_damage} damage!")
        t.sleep(2)
        print(f"{p1_pokemon_name}'s new health: {p1_health}")

        heatlh_increase_roll = rd.randint(5,10)
        heatlh__decrease_roll = rd.randint(4,8)
        fatigue_roll = rd.randint(2, 4)

     
        p1_health_result = p1_health
        p2_health_result = p2_health

        #Adjusts the Pokemon's health. The winner gains health while the loser loses health
        if p1_health > p2_health:
            self.player_1_win_count += 1
            self.player_2_lose_count += 1
            print(f"\n{self.player_1} wins this round")
            t.sleep(1)
            status = f"{self.player_1} wins"
            print(f"{p1_pokemon_name} health increases while {p2_pokemon_name} health decreases")
            t.sleep(2)
            p1_health += heatlh_increase_roll
            p2_health -= heatlh__decrease_roll

        elif p1_health == p2_health:
            self.draw_count += 1
            print(f"\nIt's a draw! No increase or decrease in health on both Pokemon due to draw")
            t.sleep(2)
            status = f"Draw"
   

        else:
            self.player_2_win_count += 1
            self.player_1_lose_count += 1
            print(f"\n{self.player_2} wins this round")
            t.sleep(1)
            status = f"{self.player_2} wins"
            print(f"{p2_pokemon_name} health increases while {p1_pokemon_name} health decreases")
            t.sleep(2)
            p2_health += heatlh_increase_roll
            p1_health -= heatlh__decrease_roll

        #After health adjustments, the program will decrease both Pokemon's health due to fatigue
        print(f"\nPokemon's health decreases due to fatigue")
        t.sleep(1)
        p1_health -= fatigue_roll
        p2_health -= fatigue_roll

        print(f"{p1_pokemon_name}'s new health: {p1_health} | {p2_pokemon_name}'s new health: {p2_health}\n")
        t.sleep(2)

        if p1_health > 0:
            pass
        else:
            print(f"{p1_pokemon_name}'s health reaches 0 or below. They are out!")
            t.sleep(1)

        if p2_health > 0:
            pass
        else:
            print(f"{p2_pokemon_name}'s health reaches 0 or below. They are out!")
            t.sleep(1)


        return [p1, p1_pokemon_name, p1_health, p1_power, 
                p2, p2_pokemon_name, p2_health, p2_power, 
                hchoice1, pchoice1, hchoice2, pchoice2, 
                status, self.player_1_win_count, self.player_1_lose_count, self.player_2_win_count, self.player_2_lose_count, self.draw_count,
                p1_health_result, p2_health_result, p1_hpotion, p1_ppotion, p2_hpotion, p2_ppotion]
