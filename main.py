from player import Player
from game import Game

player = Player()

print('Your opponent will be Computer.')
computer = Player(npc=True)

game = Game(player, computer)
game.play()