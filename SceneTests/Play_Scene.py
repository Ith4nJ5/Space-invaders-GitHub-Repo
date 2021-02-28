from Scene import Scene
from Ship import Ship
from Alien_Fleet import Alien_Fleet
import pygame

class Play_Scene(Scene):
    pygame.font.init()
    player1 = Ship(300, 580)
    alienFleet = Alien_Fleet(10, 5)
    myfont = pygame.font.Font("arial.ttf", 20)

    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        super().__init__('PlayScene')


    def start(self):
        print('Se inicia: ', self.name)

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player1.moveL = True
            if event.key == pygame.K_RIGHT:
                self.player1.moveR = True
            if event.key == pygame.K_SPACE:
                self.player1.shooting()
        else:
            self.player1.moveL = False
            self.player1.moveR = False
        print('', pygame.key)

    def update(self):
        for bullet in self.player1.gun.pool:
            for alien in self.alienFleet.fleet:
                if (bullet.posY > alien.posY) and (bullet.posY < (alien.posY + alien.tamY)) and (bullet.posX >= alien.posX) and (bullet.posX <= (alien.posX + alien.tamX)):
                    alien.destroyed = True
                    bullet.shot = False
        self.player1.update()
        self.alienFleet.update()
        self.scoreText = self.myfont.render("Score: " + str(self.alienFleet.score.score), 1, (0,255,0))
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player1.draw(self.screen)
        self.alienFleet.draw(self.screen)
        self.screen.blit(self.scoreText,(10,10))

    def exit(self):
        print('Termina: ', self.name)

