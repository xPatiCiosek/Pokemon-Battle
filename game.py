class Game:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
    
    def play(self):
        # Player moves first
        damage = self.player.make_next_move()
        self.opponent.current_pokemon.hp -= damage
        # Opponent moves next
        damage = self.opponent.make_next_move()
        self.player.current_pokemon.hp -= damage