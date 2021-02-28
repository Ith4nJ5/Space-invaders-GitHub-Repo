from Alien import Alien
from Score import Score

class Alien_Fleet:
    fleet = []
    land = False
    score = Score()

    def __init__(self, fleetX, fleetY):
        posX = 15
        posY = 15
        for i in range(fleetX):
            for j in range(fleetY):
                self.fleet.append(Alien(posX, posY))
                posY += 62
            posX += 45
            posY = 15

    def draw(self, screen):
        for i in self.fleet:
            i.draw(screen)

    def update(self):
        for i in self.fleet:
            if i.destroyed == True:
                self.fleet.remove(i)
                self.score.plus(100)
            if i.land == True:
                self.land = True
            i.update()
