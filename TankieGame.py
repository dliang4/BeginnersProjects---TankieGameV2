import turtle
#Intergrate turtles

class TankMain():

    def __init__(self, name):
        self.Tname = name
        self.Thealth = 50
        self.Thitpoint = 25

    def attack(self, target):
        target.gethit(self.Thitpoint)

    def gethit(self, damagedone):
        self.Thealth = self.Thealth - damagedone

    def __str__(self):
        return "Health of " + str(self.Tname) + " is now " + str(self.Thealth)


Bob = TankMain("Bob")
Cat = TankMain("Cat")
Players = {"Bob" : Bob, "Cat" : Cat}
PlayersL = [Bob, Cat]

while len(PlayersL) != 1:
    for x in Players:
        print("{0} is still alive!".format(x))
    attacker = input("Who attacks?:")
    attacked = input("Who gets attacked?:")
    try:
        Players[attacker].attack(Players[attacked])
    except KeyError:
        print("Wrong players!")

    for p in PlayersL:
        if p.Thealth == 0:
            PlayersL.remove(p)

    for players in Players:
        print(Players[players])
    print("---------------")


print("GameOver!")
print("Winner is:" + " " + (PlayersL[0]).Tname)

