from Scene import Scene
import pygame

class Intro_Scene(Scene):
    pygame.font.init()
    titlefont = pygame.font.Font("arial.ttf", 50)
    myfont = pygame.font.Font("arial.ttf", 20)
    titleText = titlefont.render("Space Invaders", 1, (255,255,255))
    startText = myfont.render("Press any key to start", 1, (255,255,255))

    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        super().__init__('IntroScene')

    def start(self):
        print('Se inicia: ', self.name)

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            self.app.change_scene('play')

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.titleText,(300 - (self.titleText.get_width()/2), 250 - (self.titleText.get_height()/2)))
        self.screen.blit(self.startText,(300 - (self.startText.get_width()/2), 350 - (self.startText.get_height()/2)))

    def exit(self):
        print('Termina: ', self.name)

