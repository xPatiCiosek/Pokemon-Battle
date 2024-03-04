from pokemon import Pokemon
import random

#logic


p1 = Pokemon()
p2 = Pokemon()
p3 = Pokemon()

p4 = Pokemon()
p5 = Pokemon()
p6 = Pokemon()

def draw():
    return p1,p2,p3

def draw_comp():
    return p4,p5,p6


my_team = draw()
opponent_team = draw_comp()


print(f'Your pokemon:{p1.name},{p2.name},{p3.name}')
# print(f'Your opponents pokemon:{p4.name},{p5.name},{p6.name}')

my_choice = int(input("which pokemon you choose 1/2/3"))
comp_choice = random.randint(1,3)

def current_pokemon(choice,team):
    if choice == 1:
        current_pokemon = team[0]
        print(f'move choices:\n{current_pokemon.moves}')

    elif choice == 2:
        current_pokemon = team[1]
        print(f'move choices:\n{current_pokemon.moves}')

    elif choice == 3:
        current_pokemon = team[2]
        print(f'move choices:\n{current_pokemon.moves}')

    else:
        print('Sorry command unvalid')

    return current_pokemon    


my_current_pokemon = current_pokemon(my_choice, my_team)
comp_current_pokemon = current_pokemon(comp_choice,opponent_team)

# print(comp_current_pokemon.name, comp_current_pokemon.hp)

def move_choice(choice, pokemon):
    if choice == 1:
        move = pokemon.moves[0]
    elif choice == 2:
        move = pokemon.moves[1]
    elif choice == 2:
        move = pokemon.moves[2]
    return move    

