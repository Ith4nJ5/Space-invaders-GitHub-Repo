import pygame

class Bullet():
    posX = 300
    posY = 610
    speed = 8
    tamX = 3
    tamY = 9
    shoot = False

    def __init__(self, posX, posY):
        self.posX = posX - (self.tamX/2)
        self.posY = posY - (self.tamY/2)
        self.speed = 2

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.posX, self.posY, self.tamX, self.tamY))

    def update(self):
        if self.shoot == True:
            self.posY -= self.speed
        if self.posY < -10:
            self.posY = 610
            self.shoot = False