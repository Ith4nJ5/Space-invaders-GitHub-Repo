from Scene import Scene
from Ship import Ship
from Alien_Fleet import Alien_Fleet
import pygame

class Play_Scene(Scene):
    pygame.font.init()
    player1 = Ship(300, 580)
    alienFleet = Alien_Fleet(10, 5)
    myfont = pygame.font.Font("arial.ttf", 20)
    gamefont = pygame.font.Font("arial.ttf", 50)
    victory = False
    gameOver = False

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
            if self.victory == True or self.gameOver == True:
                if event.key == pygame.K_r:
                    self.app.change_scene('intro')
        else:
            self.player1.moveL = False
            self.player1.moveR = False
        print('', pygame.key)

    def update(self):
        if self.victory == False and self.gameOver == False:
            if self.alienFleet.score.score == 9000:
                self.victory = True
            else:
                for alien in self.alienFleet.fleet:
                    if alien.land == True:
                        self.gameOver = True
            for bullet in self.player1.gun.pool:
                for alien in self.alienFleet.fleet:
                    if (bullet.posY > alien.posY) and (bullet.posY < (alien.posY + alien.tamY)) and (bullet.posX >= alien.posX) and (bullet.posX <= (alien.posX + alien.tamX)):
                        alien.lifes -= 1
                        bullet.shot = False
            self.player1.update()
            self.alienFleet.update()
            self.scoreText = self.myfont.render("Score: " + str(self.alienFleet.score.score), 1, (0,255,0))
            self.victoryText = self.gamefont.render("You Won!", 1, (0, 255, 0))
            self.gameOverText = self.gamefont.render("You Lost!", 1, (255, 0, 0))
            self.restartText = self.myfont.render("Press R to go back to the main menu", 1, (255, 255, 255))
        pass

    def draw(self):
        if self.victory == False and self.gameOver == False:
            self.screen.fill((0, 0, 0))
            self.player1.draw(self.screen)
            self.alienFleet.draw(self.screen)
            self.screen.blit(self.scoreText,(300 - (self.scoreText.get_width()/2), 5))
        if self.victory == True:
            self.screen.blit(self.victoryText,(300 - (self.victoryText.get_width()/2), 250 - (self.victoryText.get_height()/2)))
            self.screen.blit(self.restartText,(300 - (self.restartText.get_width()/2), 350 - (self.restartText.get_height()/2)))
        elif self.gameOver == True:
            self.screen.blit(self.gameOverText,(300 - (self.gameOverText.get_width()/2), 250 - (self.gameOverText.get_height()/2)))
            self.screen.blit(self.restartText,(300 - (self.restartText.get_width()/2), 350 - (self.restartText.get_height()/2)))

    def exit(self):
        print('Termina: ', self.name)

