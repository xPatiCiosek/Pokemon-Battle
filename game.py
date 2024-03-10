class Game:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent

    def play(self):  
        while True:
            # Player moves first
            self.attack(self.player, self.opponent)
            if self.defeat_checker(self.opponent):
                print('Congrats! You won!!!')
                break

            # Opponent moves next
            self.attack(self.opponent, self.player)
            if self.defeat_checker(self.player):
                print('Oh no! Your opponent won this time')
                break


    @staticmethod
    def attack(attacker, defender):
        damage = attacker.make_next_move(defender)
        defender.current_pokemon.hp -= damage
        print(f"{defender.current_pokemon.name}'s hp: {defender.current_pokemon.hp}\n")

    @staticmethod
    def defeat_checker(user):
        if user.current_pokemon.hp <= 0:
                user.remove_pokemon()
                if len(user.my_team) > 0:
                    user.set_new_current_pokemon()
                    return False
                else:
                    return True
                
