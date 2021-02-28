import pygame

class Alien():
    posX = 15
    posY = 15
    speed = 4
    tamX = 30
    tamY = 30
    destroyed = False
    land = False

    def __init__(self, posX, posY):
        self.posX = posX - (self.tamX/2)
        self.posY = posY - (self.tamY/2)
        self.speed = 2

    def jump(self):
        self.posY += 31
        self.speed = -self.speed

    def boundaries(self):
        if self.posX > (600 - self.tamX):
            self.posX = (600 - self.tamX)
            self.jump()
        
        if self.posX < 0:
            self.posX = 0
            self.jump()
        
        if self.posY >= 600:
            self.land = True

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.posX, self.posY, self.tamX, self.tamY))

    def update(self):
        self.posX += self.speed
        self.boundaries()
