import pygame
import random
pygame.display.init()
pygame.font.init()
fps_clock = pygame.time.Clock() # creates variable for the FPS
FPS = 60

# screen stuff
screen_width = 1500
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FETCH")
screen_rect = screen.get_rect()


# colors
BLACK = [0, 0, 0]
RED = [255, 0, 0]
WHITE = [255, 255, 255]
BLUE = [0, 0, 255]
GREEN = [0, 255, 0]

game_mode = "level one"

# picture upload
ball_img = pygame.image.load("Fetch Art/tennis_ball.png")
background_img = pygame.image.load("Fetch Art/temp_background.png")
oliver_img = pygame.image.load("Fetch Art/oliver.png")
platform_small = pygame.image.load("Fetch Art/platform_small.png")
platform_medium = pygame.image.load("Fetch Art/platform_medium.png")
platform_ground = pygame.image.load("Fetch Art/platform_big.png")
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
player_rect = pygame.Rect(0, 0, 100, 75)

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
    # screen.fill(BLACK)
    delta_time = fps_clock.tick(FPS) / 1000
    
    # close tab
    if game_mode == "level one":

        if paused_mode:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if restart_rect.collidepoint(mouse_pos):
                        print("i am so tired rn")

        if not paused_mode:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT: # changes how fast player moves left and right
                        player_velocity_x = 20
                    if event.key == pygame.K_LEFT:
                        player_velocity_x = -20
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

        screen.blit(background_img, [0,0])

        screen.blit(oliver_img, player_rect)
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


            text_surface = restart_font.render("Restart", True, [0, 0, 0])
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