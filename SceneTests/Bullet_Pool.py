from Bullet import Bullet

class Bullet_Pool():
    pool = []

    def __init__(self, poolS):
        for i in range(poolS):
            self.pool.append(Bullet(300, 610))

    def shoot(self, posX, posY):
        for bullet in self.pool:
            if bullet.shot == False:
                bullet.fire(posX, posY)
                break        

    def draw(self, screen):
        for bullet in self.pool:
            bullet.draw(screen)

    def update(self):
        for bullet in self.pool:
            bullet.update()