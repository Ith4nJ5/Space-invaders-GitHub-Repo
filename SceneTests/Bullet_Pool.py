from Bullet import Bullet

class Bullet_Pool():
    pool = []

    def __init__(self):
        self.pool = [Bullet(300, 610),Bullet(300, 610),Bullet(300, 610),Bullet(300, 610),Bullet(300, 610),Bullet(300, 610)]

    def draw(self, screen):
        for bullet in self.pool:
            bullet.draw(screen)

    def update(self):
        for bullet in self.pool:
            bullet.update()