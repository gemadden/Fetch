import pygame
import random
pygame.display.init()
pygame.font.init()
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


background = pygame.image.load("Fetch Art/night_background.PNG")
lose_font = pygame.font.SysFont("cooper black", 70)
restart_font = pygame.font.SysFont("cooper black", 40)

is_game_running = True
while is_game_running:
    screen.fill(BLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False
    
    screen.blit(background, [0, 0])

    restart_rect = pygame.Rect(600, 500, 300, 70)
    pygame.draw.rect(screen, [255, 255, 255], restart_rect)

    text_surface = lose_font.render("You lose!", True, [255, 255, 255])
    screen.blit(text_surface, [600, 400])


    text_surface = restart_font.render("Restart", True, [0, 0, 0])
    screen.blit(text_surface, [675, 510])

    if event.type == pygame.MOUSEBUTTONDOWN: #Makes start button work
        mouse_pos = pygame.mouse.get_pos()
        if restart_rect.collidepoint(mouse_pos): #Level select screen
            game_mode = "second title screen"


    pygame.display.flip()
    fps_clock.tick(FPS)