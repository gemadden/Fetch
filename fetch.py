import pygame
import random
pygame.display.init()
pygame.font.init()
fps_clock = pygame.time.Clock() 
FPS = 30


screen_width = 1500
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FETCH")
screen_rect = screen.get_rect()



start_button_font = pygame.font.SysFont("cooper black", 120) #Font sizes
button_font = pygame.font.SysFont("cooper black", 60)

level_one_button_font = pygame.font.SysFont("cooper black", 50) #Font sizes
character_select_one_button_font = pygame.font.SysFont("cooper black", 40)
level_select_font = pygame.font.SysFont("cooper black", 90)
name_font = pygame.font.SysFont("cooper black", 30)

game_mode = "title screen"

BLACK = [0, 0, 0]
RED = [255, 0, 0]
WHITE = [255, 255, 255]
BLUE = [0, 0, 255]
GREEN = [38, 106, 75]
YELLOW = [255, 255, 0]
ORANGE = [255, 229, 180]

image = pygame.image.load("Fetch Art/title_background.PNG") #Art

#dog art
oliver_icon = pygame.image.load("Fetch Art/oliver_left.PNG")
oliver_icon_rect = oliver_icon.get_rect()
lulu_icon = pygame.image.load("Fetch Art/lulu_left.PNG")
lulu_icon_rect = lulu_icon.get_rect()

level_one_icon = pygame.image.load("Fetch Art/ball_level.PNG")
level_one_rect = level_one_icon.get_rect()
level_two_icon = pygame.image.load("Fetch Art/stick_level.PNG")
level_two_rect = level_two_icon.get_rect()
level_three_icon = pygame.image.load("Fetch Art/mailman_level.png")
level_three_rect = level_three_icon.get_rect()

ball_img = pygame.image.load("Fetch Art/tennis_ball.png")
oliver_right_img = pygame.image.load("Fetch Art/oliver_right.png")
oliver_left_img = pygame.image.load("Fetch Art/oliver_left.png")

day_background_img = pygame.image.load("Fetch Art/day_background.png")

platform_small = pygame.image.load("Fetch Art/platform_small.png")
platform_medium = pygame.image.load("Fetch Art/platform_medium.png")
platform_ground = pygame.image.load("Fetch Art/bottom_platform.png")
# stick_img = pygame.image.load("stick.png")
# mail_img = pygame.image.load("mail.png")
# kibble_img = pygame.image.load("kibble.png")
# bone_img = pygame.image.load("bone.png")
# chocolate_img = pygame.image.load("chocolate.png")
# miles_img = pygame.image.load("miles.png")
# bear_img = pygame.image.load("bear.png")
# neo_img = pygame.image.load("neo.png")
# mail_img = pygame.image.load("mail.png")
# mail_img = pygame.image.load("mail.png")
# mail_img = pygame.image.load("mail.png")
oliver_right = True
oliver_left = False

points_font = pygame.font.SysFont("cooper black", 40)
points = 0
lives = 3

lose_font = pygame.font.SysFont("cooper black", 70)
restart_font = pygame.font.SysFont("cooper black", 40)
restart_rect = pygame.Rect(750, 500, 50, 100)

platform_height = 40
platform_color = GREEN
bottom_platform = pygame.Rect(
    screen_rect.left,
    screen_rect.bottom - platform_height,
    screen_rect.right - screen_rect.left,
    platform_height
)

platforms = [
    bottom_platform,
    pygame.Rect(0, 550, 700, platform_height),
    pygame.Rect(1000, 775, 500, platform_height),
]

# player rectangle
# player_location_x = 0 # comment out if dont want velocity
# player_location_y = 0
player_rect = pygame.Rect(0, 0, 150, 100)

# run and jump
player_velocity_x = 0
player_velocity_y = 0
player_rect.bottom = bottom_platform.top -1
GRAVITATIONAL_CONSTANT = 0.7
is_standing = False

# object spawn
objects = [
    pygame.Rect(random.randint(0, screen_width), random.randint(-screen_height, 0), 50, 50),
    pygame.Rect(random.randint(0, screen_width), random.randint(-screen_height, 0), 50, 50),
    pygame.Rect(random.randint(0, screen_width), random.randint(-screen_height, 0), 50, 50),
]

paused_mode = False
is_game_running = True
while is_game_running:

    if game_mode == "title screen":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN: #Makes start button work
                mouse_pos = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_pos): #Level select screen
                    game_mode = "second title screen"

        screen.fill((0,0,0))
    
        screen.blit(image, [0, 0]) #Draws background

        start_button = pygame.Rect(230, 500, 500, 100) #Draws start button
        pygame.draw.rect(screen, GREEN, start_button)

    
        text_surface = button_font.render("Start Game", True, [0, 0, 0]) #Writes Start Game
        screen.blit(text_surface, [300, 510])

        text_surface = start_button_font.render("Fetch!", True, [0, 0, 0]) #Writes Fetch!
        screen.blit(text_surface, [300, 300])

        text_surface = name_font.render("Created by Abby, Elisabeth, and G", True, [0, 0, 0,])
        screen.blit(text_surface, [225, 420])

    if game_mode == "second title screen":
        screen.fill((0,0,0))

        #screen.blit(level_one_icon, [250, 300]) #Draws icon art
        level_one_rect.x = 250
        level_one_rect.y = 300
        screen.blit(level_one_icon, level_one_rect)

        level_two_rect.x = 650
        level_two_rect.y = 300
        screen.blit(level_two_icon, level_two_rect)

        level_three_rect.x = 1050
        level_three_rect.y = 300
        screen.blit(level_three_icon, level_three_rect)

        oliver_icon_rect.x = 50
        oliver_icon_rect.y = 750
        screen.blit(oliver_icon, oliver_icon_rect)

        lulu_icon_rect.x = 250
        lulu_icon_rect.y = 760
        screen.blit(lulu_icon, lulu_icon_rect)
        


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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game_running = False
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if level_one_rect.collidepoint(mouse_pos):
                    game_mode = "level_one"

                if event.type == pygame.MOUSEBUTTONDOWN: 
                    mouse_pos = pygame.mouse.get_pos()
                if level_two_rect.collidepoint(mouse_pos):
                    game_mode = "level_two"

                if event.type == pygame.MOUSEBUTTONDOWN:  
                    mouse_pos = pygame.mouse.get_pos()
                if level_three_rect.collidepoint(mouse_pos):
                    game_mode = "level_three"

                if event.type == pygame.MOUSEBUTTONDOWN: #Makes character select buttons work
                    mouse_pos = pygame.mouse.get_pos()
                    if oliver_icon_rect.collidepoint(mouse_pos):
                        print("oliver")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if oliver_icon_rect.collidepoint(mouse_pos):
                        print("LuLu")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if character_three_button.collidepoint(mouse_pos):
                        print("miles")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if character_four_button.collidepoint(mouse_pos):
                        print("bear")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if character_five_button.collidepoint(mouse_pos):
                        print("willow")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if character_six_button.collidepoint(mouse_pos):
                        print("eevee")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if character_seven_button.collidepoint(mouse_pos):
                        print("meo")
        
    if game_mode == "level_one":
        if paused_mode:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if restart_rect.collidepoint(mouse_pos):
                        paused_mode = False
                        game_mode = "second title screen"
                        

        if not paused_mode:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT: # changes how fast player moves left and right
                        player_velocity_x = 20
                        oliver_left = False
                        oliver_right = True
                    if event.key == pygame.K_LEFT:
                        player_velocity_x = -20
                        oliver_right = False
                        oliver_left = True
                    if event.key == pygame.K_UP and is_standing: # allows character to jump
                        player_velocity_y = -20
                    if event.key == pygame.K_DOWN: # ALLOWS 
                        player_velocity_y = 10

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        player_velocity_x = 0
                    if event.key == pygame.K_LEFT:
                        player_velocity_x = 0


            player_rect.x = player_rect.x + player_velocity_x # comment out if dont want velocity
            if player_rect.right < 0:
                player_rect.left = screen_width
            if player_rect.left > screen_width:
                player_rect.right = 0
            player_velocity_y = player_velocity_y + GRAVITATIONAL_CONSTANT
            player_rect.bottom = player_rect.bottom + player_velocity_y

            # object respawn
            new_objects = []
            for object in objects: # loop through all objects
                
                collide = object.colliderect(player_rect) # for object in the index, did it get hit?

                # if object leave the screen
                if object.top >= screen_height:
                    lives = lives - 1
                    new_object = pygame.Rect(random.randint(0, screen_width), 0, 50, 50)
                    new_object.bottom = 0
                    new_objects.append(new_object)
                    continue
                if collide:
                    points = points + 1
                    new_object = pygame.Rect(random.randint(0, screen_width), 0, 50, 50)
                    new_object.bottom = 0
                    new_objects.append(new_object)
                    continue
                new_objects.append(object)


            objects = new_objects
            for object in objects:
                object.centery = object.centery + 5
        # # collision
        # new_objects = []
        # for object in objects: # loop through all objects

        #     collide = object.colliderect(player_rect) # for object in the index, did it get hit?
        #     if not collide: #did not hit
        #         #KILLA
        #         new_objects.append(object) #copying all old into new except for one hit
        #     else:
        #         new_objects.append(pygame.Rect(random.randint(0, screen_width), random.randint(-screen_height, 0), 50, 50))

            
        # objects = new_objects

        screen.blit(day_background_img, [0,0])

        #screen.blit(oliver_img, player_rect)
        if oliver_left and not oliver_right:
            screen.blit(oliver_left_img, player_rect)
        if oliver_right and not oliver_left:
            screen.blit(oliver_right_img, player_rect)

        for platform in platforms:
            if platform.w == 500:
                screen.blit(platform_small, platform)
            if platform.w == 700:
                screen.blit(platform_medium, platform)
            if platform == bottom_platform:
                screen.blit(platform_ground, platform)
        for object in objects:
            screen.blit(ball_img, object)

        

        is_standing = False
        index = player_rect.collidelist(platforms)
        if index != -1: #did hit
            touching_platform = platforms[index]
            is_just_touching_down = player_rect.bottom - touching_platform.top < platform_height
            is_descending = player_velocity_y > 0

            if is_just_touching_down and is_descending:
                player_rect.bottom = touching_platform.top # - player_rect.height
                is_standing = True
                player_velocity_y = 1

        text_surface = points_font.render("Points: " + str(points), True, [255, 255, 255])
        screen.blit(text_surface, [5, 0])
        text_surface = points_font.render("Lives: " + str(lives), True, [255, 255, 255])
        screen.blit(text_surface, [5, 45])

        if points == 1:
            paused_mode = True
            restart_rect = pygame.Rect(600, 500, 300, 70)
            pygame.draw.rect(screen, [255, 255, 255], restart_rect)

            text_surface = lose_font.render("You win!!", True, [255, 255, 255])
            screen.blit(text_surface, [575, 400])


            text_surface = restart_font.render("Return", True, [0, 0, 0])
            screen.blit(text_surface, [675, 510])

            # if event.type == pygame.MOUSEBUTTONDOWN: #Makes start button work
            #     mouse_pos = pygame.mouse.get_pos()
            #     if restart_rect.collidepoint(mouse_pos): #Level select screen
            #         game_mode = "second title screen"

        if lives == 0:
            paused_mode = True
            restart_rect = pygame.Rect(600, 500, 300, 70)
            pygame.draw.rect(screen, [255, 255, 255], restart_rect)

            text_surface = lose_font.render("You lose!", True, [255, 255, 255])
            screen.blit(text_surface, [600, 400])


            text_surface = restart_font.render("Restart", True, [0, 0, 0])
            screen.blit(text_surface, [675, 510])
                # if event.type == pygame.MOUSEBUTTONDOWN: #Makes start button work
            # mouse_pos = pygame.mouse.get_pos()
            # if restart_rect.collidepoint(mouse_pos): #Level select screen
            #     game_mode = "second title screen"

    pygame.display.flip()
    fps_clock.tick(FPS)
