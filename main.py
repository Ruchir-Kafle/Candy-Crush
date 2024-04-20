import pygame
from sys import exit
import random

class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Candy Crush")

        self.clock = pygame.time.Clock()

        self.screen.fill((178, 255, 255))

        self.board = [[0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0]]
        
        for i, row in enumerate(self.board):
            for j, tile in enumerate(row):
                temporary_surface = pygame.Surface((120, 120))
                temporary_rectangle = temporary_surface.get_rect(topleft=(i*120, j*120))

                self.board[i][j] = random.randint(1, 3)

                if self.board[i][j] == 1:
                    temporary_surface.fill((255,0,0))
                if self.board[i][j] == 2:
                    temporary_surface.fill((0,255,0))
                if self.board[i][j] == 3:
                    temporary_surface.fill((0,0,255))
                
                self.screen.blit(temporary_surface, temporary_rectangle)

    def user_inputs(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
    def update(self) -> None:
        pygame.display.update()
        self.clock.tick(10)

    def main_loop(self) -> None:
        while True:
            self.user_inputs()

            self.update()


if __name__ == "__main__":
    game_object = Game()
    game_object.main_loop()