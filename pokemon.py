import random
from request import Request
from move import Move

POKEMON = 'pokemon/{}'

class Pokemon:
    def __init__(self):
        pokemon_request = Request(POKEMON.format(random.randint(1,1025)))
        pokemon_data = pokemon_request.get_content()
        self.name = pokemon_data['name']
        self.initial_hp = self.get_hp(pokemon_data)
        self.hp = self.get_hp(pokemon_data)
        self.attack = self.get_attack(pokemon_data)
        self.defense = self.get_defense(pokemon_data)
        self.speed = self.get_speed(pokemon_data)
        self.types = self.get_types(pokemon_data)
        self.moves = self.get_moves(pokemon_data)

    @staticmethod
    def get_hp(pokemon_data):
        return pokemon_data['stats'][0]['base_stat']
    
    @staticmethod
    def get_attack(pokemon_data):
        return pokemon_data['stats'][1]['base_stat']
    
    @staticmethod
    def get_defense(pokemon_data):
        return pokemon_data['stats'][2]['base_stat']
    
    @staticmethod
    def get_speed(pokemon_data):
        return pokemon_data['stats'][5]['base_stat']
    
    @staticmethod
    def get_types(pokemon_data):
        types_list = [] 
        types = pokemon_data['types']
            
        for type in types:
            types_list.append(type['type']['name'])
        return types_list 
    
    @staticmethod
    def get_moves(pokemon_data):
        move_list = []
        moves = pokemon_data['moves']
        for move in moves:
            move_list.append(move['move']['name'])
        return Move.assign_moves(move_list)
      
        


