from pokemon import Pokemon
import random


class Player:
    def __init__(self):
        self.name = input('Whats your name')
        self.my_team = draw()


class Comp:
    def __init__(self):
        self.opponent_team = draw()


def draw():
    p1 = Pokemon()
    p2 = Pokemon()
    p3 = Pokemon()
    return p1,p2,p3


player = Player()
comp = Comp()

print(player.my_team[0].name)
print(player.my_team[1].name)

print(comp.opponent_team[0].name)

# print(f'Your pokemon:{p1.name},{p2.name},{p3.name}')

