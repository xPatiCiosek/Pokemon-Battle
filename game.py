class Game:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent

    def play(self):  
        if self.opponent.current_pokemon.speed > self.player.current_pokemon.speed: 
            # First move belongs to opponent
            self.first_move_to(self.opponent,self.player)
        else:
            # First move belongs to player
            self.first_move_to(self.player, self.opponent)

    def first_move_to(self, first_player ,second_player): 
        while True:
            self.attack(first_player, second_player)
            if self.defeat_checker(second_player):
                print('Congrats! You won!!!')
                break
            
            self.attack(second_player, first_player)
            if self.defeat_checker(first_player):
                print('Oh no! Your opponent won this time')
                break           

    @staticmethod
    def attack(attacker, defender):
        damage = attacker.make_next_move(defender)
        defender.current_pokemon.hp -= damage
        print(f"{defender.current_pokemon.name}'s hp: {defender.current_pokemon.hp}\n")

    @staticmethod
    def defeat_checker(player):
        if player.current_pokemon.hp <= 0:
                player.remove_pokemon()
                if len(player.my_team) > 0:
                    player.set_new_current_pokemon()
                    return False
                else:
                    return True
                
