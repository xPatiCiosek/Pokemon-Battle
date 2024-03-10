from player import Player
from game import Game

player = Player()

print('\nYour opponent will be Computer.')
computer = Player(npc=True)

game = Game(player, computer)

game.play()