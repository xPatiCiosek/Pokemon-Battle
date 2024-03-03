import requests
import random

base_url = 'https://pokeapi.co/api/v2/{}'

moves_list = []
# move = 'pound'

pokemon = random.randint(1,1025)

POKEMON = 'pokemon/{}'.format(pokemon)
MOVES = 'move/{}'


request = base_url.format(POKEMON)
response = requests.get(request).json()

# power of the move
# print(response['power'])
# # type of the move
# print(response['type']['name'])
# # accuracy of the move
# print(response['accuracy'])



# random pokemon by pokedex number
# print(response)


# name of the pokemon
print('NAME:' + response['name'])


# types
types =response['types']
for type in types:
    print('TYPE:' + type['type']['name'])



# moves
moves =response['moves']
for move in moves:
    # print('MOVE:' + move['move']['name'])
    moves_list.append(move['move']['name'])

# print(moves_list)

moves_assigned = []
if len(moves_list) < 3:
    moves_assigned = moves_list
else:
    for i in range(3):
        random_num = random.randint(0,len(moves_list)-1)
        moves_assigned.append(moves_list[random_num])

print(moves_assigned) 

for move in moves_assigned:
    request = base_url.format(MOVES.format(move))
    response = requests.get(request).json()
    
    # power of the move
    print(response['power'])
    # type of the move
    print('MOVE TYPE:'+response['type']['name'])
    # accuracy of the move
    print(response['accuracy'])
# 