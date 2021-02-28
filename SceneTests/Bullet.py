import pygame

class Bullet():
    posX = 300
    posY = 610
    speed = 8
    tamX = 3
    tamY = 9
    shot = False

    def __init__(self, posX, posY):
        self.posX = posX - (self.tamX/2)
        self.posY = posY - (self.tamY/2)

    def fire(self, posX):
        self.posX = posX
        self.shot = True

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.posX, self.posY, self.tamX, self.tamY))

    def update(self):
        if self.shot == True:
            self.posY -= self.speed
        if self. shot == False:
            self.posY = 610
        if self.posY < -10:
            self.shot = False