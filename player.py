from pokemon import Pokemon
import random


class Player:
    def __init__(self, npc=False):
        self.npc = npc
        if self.npc:
            self.name = 'Computer'
            self.my_team = self.draw_team()
            self.choice = random.randint(1,3)
        else:
            self.name = input('Whats your name')
            self.my_team = self.draw_team()
            self.choice =int(input("which pokemon you choose 1/2/3"))
        self.current_pokemon = self.my_team[self.choice-1]
        print(f'First pokemon to fight for {self.name} will be {self.current_pokemon.name}')

    def set_new_current_pokemon(self):
        choice = int(input("which pokemon you choose 1/2"))
        self.choice = choice
        self.current_pokemon = self.my_team[self.choice-1]

    def set_second_pokemon(self):
        if self.nc:
            self.choice = random.random(1,2)
        else:
            self.choice = int(input("which pokemon you choose? (1/2) "))
        self.current_pokemon = self.my_team[self.choice -1]

    def set_third_pokemon(self):
        self.choice = 1
        self.current_pokemon = self.my_team[self.choice-1]            

    def remove_pokemon(self):
        self.my_team.pop(self.choice -1 )
            

    def draw_team(self):
        p1 = Pokemon()
        p2 = Pokemon()
        p3 = Pokemon()
        print(p1.name,p2.name,p3.name)
        return [p1,p2,p3]

    def make_next_move(self):
        print(f'Available moves for {self.name}:')
        for index, move in enumerate(self.current_pokemon.moves):
            print(f'{index+1}. {move.name}')
        if self.npc:
            move_number = random.randint(1, len(self.current_pokemon.moves))
        else:
            move_number = int(input('Which of these moves would you like? (Enter its number) '))
        move = self.current_pokemon.moves[move_number-1]
        print(f'{self.name} chooses to use the move {move.name}...')
        damage = random.randint(1, 100)  # Change this to use the formula
        print(f'Move {move.name} does {damage} damage!')
        return damage
 

# def hp(current_pokemon_hp):
#     if current_pokemon_hp <0:
#         print('Your pokemon lost')
#         #remove pokemon from team
#         player.remove_pokemon()
#         #choose your next pokemon
#         player.set_new_current_pokemon()    
