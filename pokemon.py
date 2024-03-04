import requests
import random

base_url = 'https://pokeapi.co/api/v2/{}'


# pokemon = random.randint(1,1025)

POKEMON = 'pokemon/{}'
MOVES = 'move/{}'


class Pokemon:
    def __init__(self):
        self.name = draw_random_pokemon()
        self.hp = 150
        self.types = get_types(self.name)
        self.moves = get_moves(self.name)


def request(var):
    request = base_url.format(var)
    response = requests.get(request).json()
    return response


def draw_random_pokemon():
    pokemon_name = request(POKEMON.format(random.randint(1,1025)))['name']
    return pokemon_name


def get_types(pokemon_name):
    types = request(POKEMON.format(pokemon_name))['types']

    types_list = []    
    # types
    for type in types:
        types_list.append(type['type']['name'])
    return types_list    


def get_moves(pokemon_name):
    moves = request(POKEMON.format(pokemon_name))['moves']
    move_list = []
    for move in moves:
        # print('MOVE:' + move['move']['name'])
        move_list.append(move['move']['name'])
    return assign_moves(move_list)
      
        
def assign_moves(move_list):
    moves_assigned = []
    move_data_list = []
    if len(move_list) < 3:
        moves_assigned = move_list
    else:
        for i in range(3):
            random_num = random.randint(0,len(move_list)-1)
            moves_assigned.append(move_list[random_num])


    for move in moves_assigned:
        move_data = request(MOVES.format(move))

        move_power = move_data['power']
        move_type = move_data['type']['name']
        move_accuracy = move_data['accuracy']

        move_data_list.append({'name': move,'power': move_power,'type': move_type,'accuracy': move_accuracy})
    return move_data_list

