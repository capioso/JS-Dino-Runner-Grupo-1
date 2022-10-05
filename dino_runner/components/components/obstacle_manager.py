from .cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
import pygame
import random

class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        val = random.randint(0,3)
        
        if len(self.obstacles) == 0:
            if val % 2 == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            else:
                self.obstacles.append(Cactus(LARGE_CACTUS))
        
            #self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)