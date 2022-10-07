from .cactus import Cactus
from .birds import Birds
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.score import Score
import random


class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, player, on_death):
        if len(self.obstacles) == 0:
            val = random.randint(0,2)
            if val == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif val == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            else:
                self.obstacles.append(Birds(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.dino_rect.colliderect(obstacle.rect):
                
                if on_death():
                    
                    self.obstacles.remove(obstacle)
                else:
                    break
        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacle(self):
        self.obstacles = []