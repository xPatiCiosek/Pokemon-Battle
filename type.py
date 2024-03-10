from request import Request


TYPE = 'type/{}'

class Damage_type_data:
    def __init__(self, type):
        type_request = Request(TYPE.format(type))
        type_data = type_request.get_content()['damage_relations']
        self.name = type
        self.double_damage_to = self.get_double_damage_to(type_data)
        self.half_damage_to = self.get_half_damage_to(type_data)
        self.no_damage_to = self.get_no_damage_to(type_data)

    @staticmethod
    def get_double_damage_to(type_data):
        types = []
        for type in type_data['double_damage_to']:
            types.append(type['name'])
        return types    

    @staticmethod
    def get_half_damage_to(type_data):
        types = []
        for type in type_data['half_damage_to']:
            types.append(type['name'])
        return types
    
    @staticmethod
    def get_no_damage_to(type_data):
        types = []
        for type in type_data['no_damage_to']:
            types.append(type['name'])
        return types
    
    
    def assign_damage(self, pokemon_types):
        power = []
        for type in pokemon_types:
            if type in self.double_damage_to:
                power.append(2)
            elif type in self.half_damage_to:
                power.append(0.5)
            elif type in self.no_damage_to:
                power.append(0)
            else: 
                power.append(1)
        return max(power)        

    