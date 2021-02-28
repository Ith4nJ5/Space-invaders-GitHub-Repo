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
                if j == 0:
                    self.fleet.append(Alien(posX, posY, 3, (255,0,0)))
                elif j == 1 or j == 2:
                    self.fleet.append(Alien(posX, posY, 2, (255,255,0)))
                else:
                    self.fleet.append(Alien(posX, posY, 1, (255,255,255)))
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
                self.score.plus(i.score)
            if i.land == True:
                self.land = True
            i.update()
