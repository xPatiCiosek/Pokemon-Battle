class Game:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent

    def play(self):  
        while True:
            # Player moves first
            damage = self.player.make_next_move(self.opponent)
            self.opponent.current_pokemon.hp -= damage
            print(f"{self.opponent.current_pokemon.name}'s hp: {self.opponent.current_pokemon.hp}\n")

            if self.opponent.current_pokemon.hp <= 0:
                self.opponent.remove_pokemon()
                if len(self.opponent.my_team) > 0:
                    self.opponent.set_new_current_pokemon()
                else:
                    print("you won")
                    break;    

            # Opponent moves next
            damage = self.opponent.make_next_move(self.player)
            self.player.current_pokemon.hp -= damage

            print(f"{self.player.current_pokemon.name}'s hp: {self.player.current_pokemon.hp}")
            if self.player.current_pokemon.hp <= 0:
                self.player.remove_pokemon()
                if len(self.player.my_team) > 0:
                    self.player.set_new_current_pokemon()
                else:
                    print("your opponent won")
                    break; 
        
   