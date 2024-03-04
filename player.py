from pokemon import Pokemon
import random


class Player:
    def __init__(self):
        self.name = input('Whats your name')
        self.my_team = draw()
        self.choice =int(input("which pokemon you choose 1/2/3"))
        self.current_pokemon = self.my_team[self.choice-1]


    def set_new_current_pokemon(self):
        choice = int(input("which pokemon you choose 1/2"))
        self.choice = choice
        self.current_pokemon = self.my_team[self.choice-1]


    def remove_pokemon(self):
        if 0 <= self.choice < len(self.my_team):
            self.my_team.pop(self.choice -1 )
            


class Comp:
    def __init__(self):
        self.team = draw()
        self.current_pokemon = current_pokemon(random.randint(1,len(self.team)),self.team)


def draw():
    p1 = Pokemon()
    p2 = Pokemon()
    p3 = Pokemon()
    print(p1.name,p2.name,p3.name)
    return [p1,p2,p3]


# def current_pokemon(choice,team):
#     if choice == 1:
#         current_pokemon = team[0]
#         print(f'move choices:\n{current_pokemon.moves}')

#     elif choice == 2:
#         current_pokemon = team[1]
#         print(f'move choices:\n{current_pokemon.moves}')

#     elif choice == 3:
#         current_pokemon = team[2]
#         print(f'move choices:\n{current_pokemon.moves}')

#     else:
#         print('Sorry command unvalid')

#     return current_pokemon    


player = Player()

# comp = Comp()
# print(comp.current_pokemon.name)

#for each print name then can delete the obj if pokemon is dead

current_pokemon = 150
enemy_pok = 150

def move_choice(choice, pokemon):
    if choice == 1:
        move = pokemon.moves[0]
    elif choice == 2:
        move = pokemon.moves[1]
    elif choice == 2:
        move = pokemon.moves[2]
    return move    

def hp(current_pokemon_hp):
    if current_pokemon_hp <0:
        print('Your pokemon lost')
        #remove pokemon from team
        player.remove_pokemon()
        #choose your next pokemon
        player.set_new_current_pokemon()    


print(player.my_team[0].name)


# player.set_new_current_pokemon()
# player.my_team[player.current_pokemon] = {'lol'}
print(player.current_pokemon.name)