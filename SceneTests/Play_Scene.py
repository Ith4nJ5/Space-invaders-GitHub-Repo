from Scene import Scene
from Ship import Ship
import pygame

class Play_Scene(Scene):
    player1 = Ship(300, 580)

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
        else:
            self.player1.moveL = False
            self.player1.moveR = False
        print('', pygame.key)

    def update(self):
        self.player1.update()
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player1.draw(self.screen)

    def exit(self):
        print('Termina: ', self.name)

