import pygame
from dino_runner.components.components.obstacle import Obstacle
from dino_runner.components.components.obstacle_manager import ObstacleManager
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.score import Score

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, DINO_START, DINO_DEAD


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.death_count = 0
        self.score = Score()

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
                
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacle()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.score.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((161,130,98))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def Text_on_screen(self, text, pos):
        font = pygame.font.Font(FONT_STYLE, 30)
        text_component = font.render(text, True, (17,12,16))
        text_rect = text_component.get_rect()
        text_rect.center = pos
        self.screen.blit(text_component, text_rect)

    def show_menu(self):
        # pintar mi ventana
        self.screen.fill((161,130,98))
        # mostrar mensaje de bienvenida
        if self.death_count == 0:
            self.Text_on_screen("Press any key to start",(SCREEN_HEIGHT - 40, SCREEN_WIDTH // 3))
            self.screen.blit(DINO_START, (SCREEN_HEIGHT - 70, SCREEN_WIDTH // 6))
            self.Text_on_screen("Just have fun :3",(SCREEN_HEIGHT - 40, SCREEN_WIDTH // 2))
        else:
            self.Text_on_screen("I am dead :'3", (SCREEN_HEIGHT - 40, SCREEN_WIDTH // 3))
            self.screen.blit(DINO_DEAD, (SCREEN_HEIGHT - 70, SCREEN_WIDTH // 6))
            self.Text_on_screen("Press any key to restart",(SCREEN_HEIGHT - 40, SCREEN_WIDTH // 2))
            self.Text_on_screen(f"Death Count: {self.death_count}",(950, 50))
           
        pygame.display.update()
        #escuchar eventos
        self.handle_keys_events_on_menu()
    
    def handle_keys_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def on_death(self):
        pygame.display.update()
        self.playing = False
        self.death_count += 1
        self.score = Score()
        self.clock = pygame.time.Clock()
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
