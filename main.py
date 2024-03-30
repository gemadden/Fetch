import pygame
import random
pygame.display.init()
fps_clock = pygame.time.Clock() # creates variable for the FPS
FPS = 30

screen_width = 1500
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FETCH")
screen_rect = screen.get_rect()

BLACK = [0, 0, 0]
RED = [255, 0, 0]
WHITE = [255, 255, 255]
BLUE = [0, 0, 255]
GREEN = [0, 255, 0]




is_game_running = True
while is_game_running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False
    
    


    pygame.display.flip()
    fps_clock.tick(FPS)