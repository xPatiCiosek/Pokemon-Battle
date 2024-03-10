from pokemon import Pokemon
import random
from type import Damage_type_data


class Player:
    def __init__(self, npc=False):
        self.npc = npc
        if self.npc:
            self.name = 'Computer'
            self.my_team = self.draw_team()
            self.choice = random.randint(1,3)
        else:
            self.name = input('Whats your name?')
            self.print_rules()
            self.my_team = self.draw_team()
            self.print_team()
            self.choice = int(input("Which pokemon you choose? (1/2/3)"))
        self.current_pokemon = self.my_team[self.choice-1]
        print(f'First pokemon to fight for {self.name} will be {self.current_pokemon.name}. TYPE: {self.current_pokemon.types}')

    
    def print_rules(self):
        print(f"Hi {self.name}, This is a simplified Pokemon battle game.\n"
            "You will get 3 random Pokemon which are assigned 3 random moves.\n"
            "Choose moves wisely [Tip: notice the types of moves and types of your opponents' Pokemon "
            "as some types are more effective against other types!]\nGood Luck!\n")
  
        
    def print_team(self):
        print(f'YOUR TEAM:')
        for index, pokemon in enumerate(self.my_team):
            print(f'{index+1}. {pokemon.name}, TYPE: {pokemon.types}')

    
    def print_moves(self):
        print(f'\nAvailable moves for {self.name}:')
        for index, move in enumerate(self.current_pokemon.moves):
            print(f'{index+1}. {move.name}, TYPE: {move.type}')

    def set_new_current_pokemon(self):
        if self.npc:
            print('\nYour opponents pokemon fainted.')
            self.choice = random.randint(1,len(self.my_team))
            print(f'Next pokemon in {self.my_team[self.choice-1].name}')
        else:
            print('\nYour pokemon fainted.')
            self.print_team()
            self.choice = int(input(f"Which pokemon you choose? (Enter its number)"))
        self.current_pokemon = self.my_team[self.choice -1]

    def remove_pokemon(self):
        self.my_team.pop(self.choice -1 )
         
    def draw_team(self):
        p1 = Pokemon()
        p2 = Pokemon()
        p3 = Pokemon()
        return [p1,p2,p3]

    def make_next_move(self, opponent):      
        if self.npc:
            move_number = random.randint(1, len(self.current_pokemon.moves))
        else:
            self.print_moves()
            move_number = int(input('Which of these moves would you like? (Enter its number)'))
        move = self.current_pokemon.moves[move_number-1]
        print(f'{self.name} chooses to use the move {move.name}...')

        damage = self.damage_calculation(move, opponent)
        return damage
    
    
    def damage_calculation(self, move, opponent):
        # Damage formula
        defense = opponent.current_pokemon.defense
        type_weakness_resistance = Damage_type_data(move.type).assign_damage(opponent.current_pokemon.types)
        damage = round((((self.current_pokemon.attack * move.power / defense) / 50) + 2) * type_weakness_resistance * random.randint(85,100)/20) 
        print(f'Move {move.name} does {damage} damage!')
        return damage