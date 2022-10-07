import pygame
from dino_runner.utils.constants import FONT_STYLE


class Score:
    def __init__(self):
        self.score = 0
       
    def update(self, game):
        self.score += 1
        if self.score % 100 == 0:
            game.game_speed += 5

    def draw(self, screen, y_pos):
        font = pygame.font.Font(FONT_STYLE, 30)
        text_component = font.render(f"Score: {self.score}", True, (17,12,16))
        text_rect = text_component.get_rect()
        text_rect.center = (1000, y_pos)
        screen.blit(text_component, text_rect)