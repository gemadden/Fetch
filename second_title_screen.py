import pygame
pygame.display.init()
pygame.font.init()
fps_clock = pygame.time.Clock() 
FPS = 30

screen_width = 1500
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

BLACK = [0, 0, 0]
RED = [255, 0, 0]
WHITE = [255, 255, 255]
BLUE = [0, 0, 255]
GREEN = [80, 200, 120]
YELLOW = [255, 255, 0]
ORANGE = [255, 229, 180]

level_one_button_font = pygame.font.SysFont("cooper black", 50) #Font sizes
character_select_one_button_font = pygame.font.SysFont("cooper black", 40)
level_select_font = pygame.font.SysFont("cooper black", 90)

#dog art

oliver_icon = pygame.image.load("Fetch Art/oliver_right.PNG")


is_game_running = True
while is_game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False

        if event.type == pygame.MOUSEBUTTONDOWN: # Makes level one button work
            mouse_pos = pygame.mouse.get_pos()
            if level_one_button.collidepoint(mouse_pos):
                print("level one")
        if event.type == pygame.MOUSEBUTTONDOWN: # Makes level two button work
            mouse_pos = pygame.mouse.get_pos()
            if level_two_button.collidepoint(mouse_pos):
                print("level two")
        if event.type == pygame.MOUSEBUTTONDOWN:  # Makes level three button work
            mouse_pos = pygame.mouse.get_pos()
            if level_three_button.collidepoint(mouse_pos):
                print("level three")

        if event.type == pygame.MOUSEBUTTONDOWN: # Makes character select Olver work
            mouse_pos = pygame.mouse.get_pos()
            if character_one_button.collidepoint(mouse_pos):
                print("oliver")
        if event.type == pygame.MOUSEBUTTONDOWN: # Makes character select LuLu work
            mouse_pos = pygame.mouse.get_pos()
            if character_two_button.collidepoint(mouse_pos):
                print("LuLu")
        if event.type == pygame.MOUSEBUTTONDOWN: # Makes character select Miles work
            mouse_pos = pygame.mouse.get_pos()
            if character_three_button.collidepoint(mouse_pos):
                print("miles")
        if event.type == pygame.MOUSEBUTTONDOWN: # Makes character select Bear work
            mouse_pos = pygame.mouse.get_pos()
            if character_four_button.collidepoint(mouse_pos):
                print("bear")
        if event.type == pygame.MOUSEBUTTONDOWN: # Makes character select Willow work
            mouse_pos = pygame.mouse.get_pos()
            if character_five_button.collidepoint(mouse_pos):
                print("willow")
        if event.type == pygame.MOUSEBUTTONDOWN: # Makes character select Eevee work
            mouse_pos = pygame.mouse.get_pos()
            if character_six_button.collidepoint(mouse_pos):
                print("eevee")
        if event.type == pygame.MOUSEBUTTONDOWN: # Makes character select Meo work
            mouse_pos = pygame.mouse.get_pos()
            if character_seven_button.collidepoint(mouse_pos):
                print("meo")

                
    screen.fill((0,0,0))
    level_one_button = pygame.Rect(250, 300, 150, 150) # Draws level buttons
    pygame.draw.rect(screen, YELLOW, level_one_button)

    level_two_button = pygame.Rect(650, 300, 150, 150) 
    pygame.draw.rect(screen, ORANGE, level_two_button)

    level_three_button = pygame.Rect(1050, 300, 150, 150) 
    pygame.draw.rect(screen, BLUE, level_three_button)

    character_one_button = pygame.Rect(100, 800, 100, 100) # Draws character buttons
    pygame.draw.rect(screen, BLUE, character_one_button)

    character_two_button = pygame.Rect(300, 800, 100, 100)
    pygame.draw.rect(screen, BLUE, character_two_button)

    character_three_button = pygame.Rect(500, 800, 100, 100)
    pygame.draw.rect(screen, BLUE, character_three_button)
    
    character_four_button = pygame.Rect(700, 800, 100, 100)
    pygame.draw.rect(screen, BLUE, character_four_button)

    character_five_button = pygame.Rect(900, 800, 100, 100)
    pygame.draw.rect(screen, BLUE, character_five_button)

    character_six_button = pygame.Rect(1100, 800, 100, 100)
    pygame.draw.rect(screen, BLUE, character_six_button)

    character_seven_button = pygame.Rect(1300, 800, 100, 100)
    pygame.draw.rect(screen, BLUE, character_seven_button)

    text_surface = level_one_button_font.render("Level One", True, [255, 255, 255]) # Writes levels text
    screen.blit(text_surface, [210, 470])

    text_surface = level_one_button_font.render("Level Two", True, [255, 255, 255])
    screen.blit(text_surface, [610, 470])

    text_surface = level_one_button_font.render("Level Three", True, [255, 255, 255])
    screen.blit(text_surface, [990, 470])

    text_surface = character_select_one_button_font.render("Oliver", True, [255, 255, 255]) # Writes character select text
    screen.blit(text_surface, [85, 900])

    text_surface = character_select_one_button_font.render("LuLu", True, [255, 255, 255])
    screen.blit(text_surface, [300, 900])

    text_surface = character_select_one_button_font.render("Miles", True, [255, 255, 255])
    screen.blit(text_surface, [500, 900])

    text_surface = character_select_one_button_font.render("Bear", True, [255, 255, 255])
    screen.blit(text_surface, [704, 900])

    text_surface = character_select_one_button_font.render("Willow", True, [255, 255, 255])
    screen.blit(text_surface, [875, 900])

    text_surface = character_select_one_button_font.render("Eevee", True, [255, 255, 255])
    screen.blit(text_surface, [1093, 900])

    text_surface = character_select_one_button_font.render("Meo", True, [255, 255, 255])
    screen.blit(text_surface, [1310, 900])

    text_surface = level_select_font.render("Select A Level", True, [255, 255, 255])
    screen.blit(text_surface, [420, 100])

    text_surface = level_select_font.render("Pick Your Character", True, [255, 255, 255])
    screen.blit(text_surface, [250, 670])

    pygame.display.flip()
    fps_clock.tick(FPS)