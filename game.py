class Game:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent

    def play(self):  
        while True:
            # Player moves first
            self.attack(self.player, self.opponent)

            if self.opponent.current_pokemon.hp <= 0:
                self.opponent.remove_pokemon()
                if len(self.opponent.my_team) > 0:
                    self.opponent.set_new_current_pokemon()
                else:
                    print("you won")
                    break;    

            # Opponent moves next
            self.attack(self.opponent, self.player)

            if self.player.current_pokemon.hp <= 0:
                self.player.remove_pokemon()
                if len(self.player.my_team) > 0:
                    self.player.set_new_current_pokemon()
                else:
                    print("your opponent won")
                    break; 


    def attack(self, attacker, defender):
        damage = attacker.make_next_move(defender)
        defender.current_pokemon.hp -= damage
        print(f"{defender.current_pokemon.name}'s hp: {defender.current_pokemon.hp}\n")