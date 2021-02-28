import pygame

class Ship():
    posX = 300
    posY = 500
    moveR = False
    moveL = False
    speed = 2
    tamX = 30
    tamY = 10

    def __init__(self, posX, posY):
        self.posX = posX - (self.tamX/2)
        self.posY = posY - (self.tamY/2)
        self.moveR = False
        self.moveL = False
        self.speed = 2
    
    def movingR(self):
        self.posX += self.speed
    
    def movingL(self):
        self.posX -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.posX, self.posY, self.tamX, self.tamY))

    def update(self):
        if self.moveR == True:
            self.movingR()
        
        if self.moveL == True:
            self.movingL()