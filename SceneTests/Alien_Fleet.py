from Alien import Alien

class Alien_Fleet:
    fleet = []
    land = False

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
            i.update()
        for j in self.fleet:
            if j.land == True:
                self.land = True
