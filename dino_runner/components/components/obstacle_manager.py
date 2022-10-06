from .cactus import Cactus
from .birds import Birds
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
import pygame
import random

class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, player, on_death):
        if len(self.obstacles) == 0:
            val = random.randint(0,3)
            if val == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif val == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            else:
                self.obstacles.append(Birds(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                on_death()
                break
        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacle(self):
        self.obstacles == 0