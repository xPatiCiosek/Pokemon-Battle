import random
from request import Request

MOVES = 'move/{}'

class Move:
    def __init__(self, move_data):
        self.name = move_data['name']
        self.type = move_data['type']['name']
        self.power = self.get_power(move_data)
        
    @staticmethod
    def get_power(move_data):
        if move_data['power'] is None:
            power = 0
        else:
            power = move_data['power']
        return power    

    @staticmethod
    def assign_moves(move_list):
        moves_assigned = []
        move_data_list = []
        if len(move_list) < 3:
            moves_assigned = move_list
        else:
            moves_assigned = random.sample(move_list, k=3)

        for move in moves_assigned:
            move_request = Request(MOVES.format(move))
            move_data = move_request.get_content()
            move_data_list.append(Move(move_data)) 
        return move_data_list
      