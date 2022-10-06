import random
from .obstacle import Obstacle


class Birds(Obstacle):
    def __init__(self, images):
        self.type = 0
        super().__init__(images, self.type)
        self.index = 0
        self.map = [150,200,250,300]
        self.var = random.randint(0,3)
        self.rect.y = self.map[self.var]

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.images[self.index // 5], self.rect)
        self.index += 1