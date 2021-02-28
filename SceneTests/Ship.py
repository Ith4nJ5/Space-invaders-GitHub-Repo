import pygame
from Bullet_Pool import Bullet_Pool

class Ship():
    posX = 300
    posY = 500
    moveR = False
    moveL = False
    speed = 4
    tamX = 30
    tamY = 10
    gun = Bullet_Pool(10)

    def __init__(self, posX, posY):
        self.posX = posX - (self.tamX/2)
        self.posY = posY - (self.tamY/2)
    
    def movingR(self):
        self.posX += self.speed
    
    def movingL(self):
        self.posX -= self.speed

    def boundaries(self):
        if self.posX > (600 - self.tamX):
            self.posX = (600 - self.tamX)
        
        if self.posX < 0:
            self.posX = 0
    
    def shooting(self):
        self.gun.shoot((self.posX + (self.tamX/2)))

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.posX, self.posY, self.tamX, self.tamY))
        self.gun.draw(screen)

    def update(self):
        self.gun.update()

        self.boundaries()

        if self.moveR == True:
            self.movingR()
        
        if self.moveL == True:
            self.movingL()
