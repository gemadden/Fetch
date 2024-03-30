import pygame
import random
use_audio = True
pygame.display.init()

if use_audio:
    pygame.mixer.init()
    day_music = pygame.mixer.Sound("day_music.MP3")
    sunset_music = pygame.mixer.Sound("sunset_music.WAV")
    night_music = pygame.mixer.Sound("night_music.MP3")
    title_music = pygame.mixer.Sound("title_music.WAV")

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
miles_icon = pygame.image.load("Fetch Art/miles_left.PNG")
miles_icon_rect = miles_icon.get_rect()
bear_icon = pygame.image.load("Fetch Art/bear_left.PNG")
bear_icon_rect = bear_icon.get_rect()
eevee_icon = pygame.image.load("Fetch Art/eevee_left.PNG")
eevee_icon_rect = eevee_icon.get_rect()
willow_icon = pygame.image.load("Fetch Art/willow_left.PNG")
willow_icon_rect = willow_icon.get_rect()
grey_bear = pygame.image.load("Fetch Art/bear_locked.png")
grey_miles = pygame.image.load("Fetch Art/miles_locked.png")
grey_eevee = pygame.image.load("Fetch Art/eevee_locked.png")
grey_willow = pygame.image.load("Fetch Art/willow_locked.png")

oliver_right_img = pygame.image.load("Fetch Art/oliver_right.png")
oliver_left_img = pygame.image.load("Fetch Art/oliver_left.png")
lulu_right_img = pygame.image.load("Fetch Art/lulu_right.PNG")
lulu_left_img = pygame.image.load("Fetch Art/lulu_left.PNG")
miles_right_img = pygame.image.load("Fetch Art/miles_right.PNG")
miles_left_img = pygame.image.load("Fetch Art/miles_left.PNG")
bear_right_img = pygame.image.load("Fetch Art/bear_right.PNG")
bear_left_img = pygame.image.load("Fetch Art/bear_left.PNG")
eevee_right_img = pygame.image.load("Fetch Art/eevee_right.PNG")
eevee_left_img = pygame.image.load("FEtch Art/eevee_left.PNG")
willow_right_img = pygame.image.load("Fetch Art/willow_right.PNG")
willow_left_img = pygame.image.load("Fetch Art/willow_left.PNG")


characters_right_img = [oliver_right_img, lulu_right_img, miles_right_img, bear_right_img, eevee_right_img] # , willow_right_img]
characters_left_img = [oliver_left_img, lulu_left_img, miles_left_img, bear_left_img, eevee_left_img,] #  eevee_left_img, willow_left_img]


# oliver is default character
chosen_character = oliver_icon
chosen_rect = pygame.Rect(5, 5, 100, 100)

level_one_icon = pygame.image.load("Fetch Art/ball_level.PNG")
level_one_rect = level_one_icon.get_rect()
level_two_icon = pygame.image.load("Fetch Art/stick_level.PNG")
level_two_rect = level_two_icon.get_rect()
level_three_icon = pygame.image.load("Fetch Art/mailman_level.png")
level_three_rect = level_three_icon.get_rect()
grey_level_two_icon = pygame.image.load("Fetch Art/stick_level_locked.PNG")
grey_level_three_icon = pygame.image.load("Fetch Art/mailman_level_locked.PNG")


ball_img = pygame.image.load("Fetch Art/tennis_ball.png")
stick_img = pygame.image.load("Fetch Art/stick.png")
mail_img = pygame.image.load("Fetch Art/mailman.png")
chocolate_img = pygame.image.load("Fetch Art/chocolate.png")

day_background_img = pygame.image.load("Fetch Art/day_background.png")
platform_small = pygame.image.load("Fetch Art/platform_small.png")
platform_medium = pygame.image.load("Fetch Art/platform_medium.png")
platform_ground = pygame.image.load("Fetch Art/bottom_platform.png")

sunset_background_img = pygame.image.load("Fetch Art/sunset_background.png")
sunset_platform_small = pygame.image.load("Fetch Art/platform_small_sunset1.png")
sunset_platform_medium = pygame.image.load("Fetch Art/platform_medium_sunset1.png")
sunset_platform_ground = pygame.image.load("Fetch Art/platform_big_sunset1.png")

night_background_img = pygame.image.load("Fetch Art/night_background.png")
night_platform_small = pygame.image.load("Fetch Art/platform_small_night.png")
night_platform_medium = pygame.image.load("Fetch Art/platform_medium_night.png")
night_platform_ground = pygame.image.load("Fetch Art/platform_big_night.png")

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

# oliver_right = True
# oliver_left = False
# lulu_right = True
# lulu_left = False

character_is_facing_left = False

new_game = True
points_font = pygame.font.SysFont("cooper black", 40)
points = 0
lives = 3

lose_font = pygame.font.SysFont("cooper black", 70)
restart_font = pygame.font.SysFont("cooper black", 40)
restart_rect = pygame.Rect(600, 500, 300, 70)
return_rect = pygame.Rect(600, 600, 300, 70)
platform_height = 40
platform_color = GREEN
bottom_platform = pygame.Rect(
    -10,
    screen_rect.bottom - platform_height,
    1520,
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
player_rect = pygame.Rect(0, 0, 200, 150)

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

enemies = [
    pygame.Rect(random.randint(0, screen_width), random.randint(-screen_height, 0), 50, 50),
]

level_one_complete = False
level_two_complete = False
level_three_complete = False

if use_audio:
    pygame.mixer.music.load("title_music.WAV")
    pygame.mixer.music.play()

paused_mode_1 = False
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

                if instructions_button.collidepoint(mouse_pos): #Level select screen
                    game_mode = "instructions"

        screen.fill((0,0,0))
    
        screen.blit(image, [0, 0]) #Draws background

        start_button = pygame.Rect(230, 500, 500, 100) #Draws start button
        pygame.draw.rect(screen, GREEN, start_button)
    
        instructions_button = pygame.Rect(230, 620, 500, 100) #Draws start button
        pygame.draw.rect(screen, GREEN, instructions_button)

        text_surface = button_font.render("Start Game", True, [0, 0, 0]) #Writes Start Game
        screen.blit(text_surface, [300, 510])

        text_surface = button_font.render("How To Play", True, [0, 0, 0]) #Writes Start Game
        screen.blit(text_surface, [300, 630])

        text_surface = start_button_font.render("Fetch!", True, [0, 0, 0]) #Writes Fetch!
        screen.blit(text_surface, [300, 300])

        text_surface = name_font.render("Created by Abby, Elisabeth, and G", True, [0, 0, 0,])
        screen.blit(text_surface, [225, 420])


    if game_mode == "instructions":

        screen.blit(image, [0, 0])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game_running = False

        back_button_rect = pygame.Rect(0,0,200,100)   #back button
        pygame.draw.rect(screen, GREEN, back_button_rect)
        back_text = button_font.render("Back", True, [0,0,0])
        screen.blit(back_text, [20, 20])

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if back_button_rect.collidepoint(mouse_pos): #back button function
                    game_mode = "title screen"


        text_surface = start_button_font.render("How To Play", True, [0, 0, 0]) #Writes Fetch!
        screen.blit(text_surface, [50, 80])

        text_surface = name_font.render("Goal: Catch 20 tennis balls before 3 reach the ground!", True, [0, 0, 0,])
        screen.blit(text_surface, [50, 220])

        text_surface = name_font.render("Complete levels to unlock new dogs!", True, [0, 0, 0,])
        screen.blit(text_surface, [50, 340])

        text_surface = name_font.render("Chocolate is poisonous to dogs...", True, [0, 0, 0,])
        screen.blit(text_surface, [50, 300])

        # text_surface = name_font.render("Collect food to give your dog extra energy!", True, [0, 0, 0,])
        # screen.blit(text_surface, [50, 420])

        text_surface = name_font.render("Use arrow keys to move your dog!", True, [0, 0, 0,])
        screen.blit(text_surface, [50, 260])


    if game_mode == "second title screen":


        if not level_one_complete and not level_two_complete:
            screen.blit(day_background_img, [0, 0])

        if level_one_complete and not level_two_complete:
            screen.blit(sunset_background_img, [0, 0])

        if level_one_complete and level_two_complete:
            screen.blit(night_background_img, [0, 0])

        screen.blit(chosen_character, chosen_rect)

        #screen.blit(level_one_icon, [250, 300]) #Draws icon art
        level_one_rect.x = 250
        level_one_rect.y = 300
        screen.blit(level_one_icon, level_one_rect)

        level_two_rect.x = 650
        level_two_rect.y = 300
        if not level_one_complete:
            screen.blit(grey_level_two_icon, level_two_rect)
        else:
            screen.blit(level_two_icon, level_two_rect)

        level_three_rect.x = 1050
        level_three_rect.y = 300
        if not level_two_complete:
            screen.blit(grey_level_three_icon, level_three_rect)
        else:
            screen.blit(level_three_icon, level_three_rect)

        oliver_icon_rect.x = 70
        oliver_icon_rect.y = 750
        screen.blit(oliver_icon, oliver_icon_rect)

        lulu_icon_rect.x = 270
        lulu_icon_rect.y = 750
        screen.blit(lulu_icon, lulu_icon_rect)
        
        miles_icon_rect.x = 480
        miles_icon_rect.y = 750
        if level_one_complete:
            screen.blit(miles_icon, miles_icon_rect)
        else:
            screen.blit(grey_miles, miles_icon_rect)

        bear_icon_rect.x = 690
        bear_icon_rect.y = 750        
        if level_one_complete:
            screen.blit(bear_icon, bear_icon_rect)
        else:
            screen.blit(grey_bear, bear_icon_rect)

        eevee_icon_rect.x = 900
        eevee_icon_rect.y = 750
        if level_two_complete:
            screen.blit(eevee_icon, eevee_icon_rect)
        else:
            screen.blit(grey_eevee, eevee_icon_rect)

        willow_icon_rect.x = 1110
        willow_icon_rect.y = 750
        if level_two_complete:
            screen.blit(willow_icon, willow_icon_rect)
        else:
            screen.blit(grey_willow, willow_icon_rect)


        text_surface = level_one_button_font.render("Level One", True, [255, 255, 255]) # Writes levels text
        screen.blit(text_surface, [210, 470])

        text_surface = level_one_button_font.render("Level Two", True, [255, 255, 255])
        screen.blit(text_surface, [610, 470])

        text_surface = level_one_button_font.render("Level Three", True, [255, 255, 255])
        screen.blit(text_surface, [990, 470])

        text_surface = character_select_one_button_font.render("Oliver", True, [255, 255, 255]) # Writes character select text
        screen.blit(text_surface, [115, 900])

        text_surface = character_select_one_button_font.render("LuLu", True, [255, 255, 255])
        screen.blit(text_surface, [325, 900])

        text_surface = character_select_one_button_font.render("Miles", True, [255, 255, 255])
        screen.blit(text_surface, [540, 900])

        text_surface = character_select_one_button_font.render("Bear", True, [255, 255, 255])
        screen.blit(text_surface, [760, 900])

        text_surface = character_select_one_button_font.render("Willow", True, [255, 255, 255])
        screen.blit(text_surface, [1150, 900])

        text_surface = character_select_one_button_font.render("Eevee", True, [255, 255, 255])
        screen.blit(text_surface, [955, 900])

        text_surface = level_select_font.render("Select A Level", True, [255, 255, 255])
        screen.blit(text_surface, [420, 100])

        text_surface = level_select_font.render("Pick Your Character", True, [255, 255, 255])
        screen.blit(text_surface, [250, 650])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game_running = False
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if level_one_rect.collidepoint(mouse_pos):
                    game_mode = "level_one"
                    if use_audio:
                        print ("here")
                        pygame.mixer.music.stop()
                        day_music.play(loops = -1)

                if event.type == pygame.MOUSEBUTTONDOWN: 
                    mouse_pos = pygame.mouse.get_pos()
                if level_two_rect.collidepoint(mouse_pos) and level_one_complete:
                    game_mode = "level_two"
                    if use_audio:
                        day_music.stop()
                        sunset_music.play(loops = -1)

                if event.type == pygame.MOUSEBUTTONDOWN:  
                    mouse_pos = pygame.mouse.get_pos()
                if level_three_rect.collidepoint(mouse_pos) and level_two_complete:
                    game_mode = "level_three"
                    if use_audio:
                        sunset_music.stop()
                        night_music.play(loops = -1)

                if event.type == pygame.MOUSEBUTTONDOWN: #Makes character select buttons work
                    mouse_pos = pygame.mouse.get_pos()
                    if oliver_icon_rect.collidepoint(mouse_pos):
                        chosen_character = oliver_icon

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if lulu_icon_rect.collidepoint(mouse_pos):
                        chosen_character = lulu_icon

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if miles_icon_rect.collidepoint(mouse_pos) and level_one_complete:
                        chosen_character = miles_icon

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if bear_icon_rect.collidepoint(mouse_pos) and level_one_complete:
                       chosen_character = bear_icon
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if eevee_icon_rect.collidepoint(mouse_pos) and level_two_complete:
                        chosen_character = eevee_icon
                        
                if event.type == pygame.MOUSEBUTTONDOWN and level_two_complete:
                    mouse_pos = pygame.mouse.get_pos()
                    if willow_icon_rect.collidepoint(mouse_pos):
                        chosen_character = willow_icon

        
    if game_mode == "level_one":
        

        if new_game:
            points = 0
            lives = 3
            player_rect.bottom = bottom_platform.top
            player_velocity_x = 0
            player_velocity_y = 0
            paused_mode_1 = False
            new_game = False
            for object in objects:
                object.x = random.randint(0, screen_width)
                object.y = random.randint(-screen_height, 0)
            for enemy in enemies:
                enemy.x = random.randint(0, screen_width)
                enemy.y = random.randint(-screen_height, 0)

        if paused_mode_1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if restart_rect.collidepoint(mouse_pos):
                        new_game = True
                        paused_mode_1 = False
                    if return_rect.collidepoint(mouse_pos):
                        new_game = True
                        paused_mode_1 = False
                        game_mode = "second title screen"
                        

        if not paused_mode_1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT: #changes how fast player moves left and right
                        player_velocity_x = 20
                        character_is_facing_left = False
                        
                        # oliver_left = False
                        # oliver_right = True
                        # lulu_left = False
                        # lulu_right = True
                    if event.key == pygame.K_LEFT:
                        player_velocity_x = -20
                        character_is_facing_left = True

                        # oliver_right = False
                        # oliver_left = True
                        # lulu_left = True
                        # lulu_right = False
                    if event.key == pygame.K_UP and is_standing: # allows character to jump
                        player_velocity_y = -20
                        if use_audio:
                            pygame.mixer.music.load("dog_bark.WAV")
                            pygame.mixer.music.play()
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

            new_enemies = []
            for enemy in enemies: # loop through all objects
                
                collide = enemy.colliderect(player_rect) # for object in the index, did it get hit?

                # if object leave the screen
                if enemy.top >= screen_height:
                    new_enemy = pygame.Rect(random.randint(0, screen_width), 0, 50, 50)
                    new_enemy.bottom = 0
                    new_enemies.append(new_enemy)
                    continue
                if collide:
                    lives = lives - 1
                    new_enemy = pygame.Rect(random.randint(0, screen_width), 0, 50, 50)
                    new_enemy.bottom = 0
                    new_enemies.append(new_enemy)
                    continue
                new_enemies.append(enemy)


            objects = new_objects
            for object in objects:
                object.centery = object.centery + 6

            enemies = new_enemies
            for enemy in enemies:
                enemy.centery = enemy.centery + 6

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

        if chosen_character == oliver_icon:
            if character_is_facing_left:
                screen.blit(oliver_left_img, player_rect)
            else:
                screen.blit(oliver_right_img, player_rect)

        if chosen_character == lulu_icon:
            if character_is_facing_left:
                screen.blit(lulu_left_img, player_rect)
            else:
                screen.blit(lulu_right_img, player_rect)

        if chosen_character == miles_icon:
            if character_is_facing_left:
                screen.blit(miles_left_img, player_rect)
            else:
               screen.blit(miles_right_img, player_rect)

        if chosen_character == bear_icon:
            if character_is_facing_left:
                screen.blit(bear_left_img, player_rect)
            else:
                screen.blit(bear_right_img, player_rect)

        if chosen_character == eevee_icon:
            if character_is_facing_left:
                screen.blit(eevee_left_img, player_rect)
            else:
                screen.blit(eevee_right_img, player_rect)

        if chosen_character == willow_icon:
            if character_is_facing_left:
                screen.blit(willow_left_img, player_rect)
            else:
                screen.blit(willow_right_img, player_rect)
        

        for platform in platforms:
            if platform.w == 500:
                screen.blit(platform_small, platform)
            if platform.w == 700:
                screen.blit(platform_medium, platform)
            if platform == bottom_platform:
                screen.blit(platform_ground, platform)
        for object in objects:
            screen.blit(ball_img, object)
        for enemy in enemies:
            screen.blit(chocolate_img, enemy)

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

        if points == 20:
            paused_mode_1 = True
            level_one_complete = True
            pygame.draw.rect(screen, [255, 255, 255], restart_rect)
            pygame.draw.rect(screen, [255, 255, 255], return_rect)

            text_surface = lose_font.render("You win!!", True, [255, 255, 255])
            screen.blit(text_surface, [575, 400])

            text_surface = restart_font.render("Restart", True, [0, 0, 0])
            screen.blit(text_surface, [675, 510])

            text_surface = restart_font.render("Return", True, [0, 0, 0])
            screen.blit(text_surface, [675, 610])

            # if event.type == pygame.MOUSEBUTTONDOWN: #Makes start button work
            #     mouse_pos = pygame.mouse.get_pos()
            #     if restart_rect.collidepoint(mouse_pos): #Level select screen
            #         game_mode = "second title screen"

        if lives == 0:
            paused_mode_1 = True
            pygame.draw.rect(screen, [255, 255, 255], restart_rect)
            pygame.draw.rect(screen, [255, 255, 255], return_rect)

            text_surface = lose_font.render("You lose!", True, [255, 255, 255])
            screen.blit(text_surface, [600, 400])

            text_surface = restart_font.render("Restart", True, [0, 0, 0])
            screen.blit(text_surface, [675, 510])

            text_surface = restart_font.render("Return", True, [0, 0, 0])
            screen.blit(text_surface, [675, 610])
                # if event.type == pygame.MOUSEBUTTONDOWN: #Makes start button work
            # mouse_pos = pygame.mouse.get_pos()
            # if restart_rect.collidepoint(mouse_pos): #Level select screen
            #     game_mode = "second title screen"

    if game_mode == "level_two":

        if new_game:
            points = 0
            lives = 3
            player_rect.bottom = bottom_platform.top
            paused_mode_1 = False
            new_game = False
            for object in objects:
                object.x = random.randint(0, screen_width)
                object.y = random.randint(-screen_height, 0)
            for enemy in enemies:
                enemy.x = random.randint(0, screen_width)
                enemy.y = random.randint(-screen_height, 0)

        if paused_mode_1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if restart_rect.collidepoint(mouse_pos):
                        new_game = True
                        paused_mode_1 = False
                    if return_rect.collidepoint(mouse_pos):
                        new_game = True
                        paused_mode_1 = False
                        game_mode = "second title screen"
                        

        if not paused_mode_1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT: # changes how fast player moves left and right
                        player_velocity_x = 20
                        character_is_facing_left = False
                        # oliver_left = False
                        # oliver_right = True
                        # lulu_left = False
                        # lulu_right = True
                    if event.key == pygame.K_LEFT:
                        player_velocity_x = -20
                        character_is_facing_left = True
                        # oliver_right = False
                        # oliver_left = True
                        # lulu_left = False
                        # lulu_right = True
                    if event.key == pygame.K_UP and is_standing: # allows character to jump
                        player_velocity_y = -20
                        if use_audio:
                            pygame.mixer.music.load("dog_bark.WAV")
                            pygame.mixer.music.play()
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

            new_enemies = []
            for enemy in enemies: # loop through all objects
                
                collide = enemy.colliderect(player_rect) # for object in the index, did it get hit?

                # if object leave the screen
                if enemy.top >= screen_height:
                    new_enemy = pygame.Rect(random.randint(0, screen_width), 0, 50, 50)
                    new_enemy.bottom = 0
                    new_enemies.append(new_enemy)
                    continue
                if collide:
                    lives = lives - 1
                    new_enemy = pygame.Rect(random.randint(0, screen_width), 0, 50, 50)
                    new_enemy.bottom = 0
                    new_enemies.append(new_enemy)
                    continue
                new_enemies.append(enemy)


            objects = new_objects
            for object in objects:
                object.centery = object.centery + 7

            enemies = new_enemies
            for enemy in enemies:
                enemy.centery = enemy.centery + 7
        # new_objects = []
        # for object in objects: # loop through all objects

        #     collide = object.colliderect(player_rect) # for object in the index, did it get hit?
        #     if not collide: #did not hit
        #         #KILLA
        #         new_objects.append(object) #copying all old into new except for one hit
        #     else:
        #         new_objects.append(pygame.Rect(random.randint(0, screen_width), random.randint(-screen_height, 0), 50, 50))

            
        # objects = new_objects

        screen.blit(sunset_background_img, [0,0])


        if chosen_character == oliver_icon:
            if character_is_facing_left:
                screen.blit(oliver_left_img, player_rect)
            else:
                screen.blit(oliver_right_img, player_rect)

        if chosen_character == lulu_icon:
            if character_is_facing_left:
                screen.blit(lulu_left_img, player_rect)
            else:
                screen.blit(lulu_right_img, player_rect)

        if chosen_character == miles_icon:
            if character_is_facing_left:
                screen.blit(miles_left_img, player_rect)
            else:
               screen.blit(miles_right_img, player_rect)

        if chosen_character == bear_icon:
            if character_is_facing_left:
                screen.blit(bear_left_img, player_rect)
            else:
                screen.blit(bear_right_img, player_rect)

        if chosen_character == eevee_icon:
            if character_is_facing_left:
                screen.blit(eevee_left_img, player_rect)
            else:
                screen.blit(eevee_right_img, player_rect)

        if chosen_character == willow_icon:
            if character_is_facing_left:
                screen.blit(willow_left_img, player_rect)
            else:
                screen.blit(willow_right_img, player_rect)

        for platform in platforms:
            if platform.w == 500:
                screen.blit(sunset_platform_small, platform)
            if platform.w == 700:
                screen.blit(sunset_platform_medium, platform)
            if platform == bottom_platform:
                screen.blit(sunset_platform_ground, platform)
        for object in objects:
            screen.blit(stick_img, object)
        for enemy in enemies:
            screen.blit(chocolate_img, enemy)

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

        if points == 20:
            paused_mode_1 = True
            level_two_complete = True
            pygame.draw.rect(screen, [255, 255, 255], restart_rect)
            pygame.draw.rect(screen, [255, 255, 255], return_rect)

            text_surface = lose_font.render("You win!!", True, [255, 255, 255])
            screen.blit(text_surface, [575, 400])

            text_surface = restart_font.render("Restart", True, [0, 0, 0])
            screen.blit(text_surface, [675, 510])

            text_surface = restart_font.render("Return", True, [0, 0, 0])
            screen.blit(text_surface, [675, 610])

            # if event.type == pygame.MOUSEBUTTONDOWN: #Makes start button work
            #     mouse_pos = pygame.mouse.get_pos()
            #     if restart_rect.collidepoint(mouse_pos): #Level select screen
            #         game_mode = "second title screen"

        if lives == 0:
            paused_mode_1 = True
            pygame.draw.rect(screen, [255, 255, 255], restart_rect)
            pygame.draw.rect(screen, [255, 255, 255], return_rect)

            text_surface = lose_font.render("You lose!", True, [255, 255, 255])
            screen.blit(text_surface, [600, 400])

            text_surface = restart_font.render("Restart", True, [0, 0, 0])
            screen.blit(text_surface, [675, 510])

            text_surface = restart_font.render("Return", True, [0, 0, 0])
            screen.blit(text_surface, [675, 610])
                # if event.type == pygame.MOUSEBUTTONDOWN: #Makes start button work
            # mouse_pos = pygame.mouse.get_pos()
            # if restart_rect.collidepoint(mouse_pos): #Level select screen
            #     game_mode = "second title screen"

    if game_mode == "level_three":

        if new_game:
            points = 0
            lives = 3
            player_rect.bottom = bottom_platform.top
            paused_mode_1 = False
            new_game = False
            for object in objects:
                object.x = random.randint(0, screen_width)
                object.y = random.randint(-screen_height, 0)
            for enemy in enemies:
                enemy.x = random.randint(0, screen_width)
                enemy.y = random.randint(-screen_height, 0)

        if paused_mode_1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if restart_rect.collidepoint(mouse_pos):
                        new_game = True
                        paused_mode_1 = False
                    if return_rect.collidepoint(mouse_pos):
                        new_game = True
                        paused_mode_1 = False
                        game_mode = "second title screen"
                        

        if not paused_mode_1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT: # changes how fast player moves left and right
                        player_velocity_x = 20
                        character_is_facing_left = False
                        # oliver_left = False
                        # oliver_right = True
                        # lulu_left = False
                        # lulu_right = True
                    if event.key == pygame.K_LEFT:
                        player_velocity_x = -20
                        character_is_facing_left = True
                        # oliver_right = False
                        # oliver_left = True
                        # lulu_left = False
                        # lulu_right = True
                    if event.key == pygame.K_UP and is_standing: # allows character to jump
                        player_velocity_y = -20
                        if use_audio:
                            pygame.mixer.music.load("dog_bark.WAV")
                            pygame.mixer.music.play()
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

            new_enemies = []
            for enemy in enemies: # loop through all objects
                
                collide = enemy.colliderect(player_rect) # for object in the index, did it get hit?

                # if object leave the screen
                if enemy.top >= screen_height:
                    new_enemy = pygame.Rect(random.randint(0, screen_width), 0, 50, 50)
                    new_enemy.bottom = 0
                    new_enemies.append(new_enemy)
                    continue
                if collide:
                    lives = lives - 1
                    new_enemy = pygame.Rect(random.randint(0, screen_width), 0, 50, 50)
                    new_enemy.bottom = 0
                    new_enemies.append(new_enemy)
                    continue
                new_enemies.append(enemy)


            objects = new_objects
            for object in objects:
                object.centery = object.centery + 8

            enemies = new_enemies
            for enemy in enemies:
                enemy.centery = enemy.centery + 8
        # new_objects = []
        # for object in objects: # loop through all objects

        #     collide = object.colliderect(player_rect) # for object in the index, did it get hit?
        #     if not collide: #did not hit
        #         #KILLA
        #         new_objects.append(object) #copying all old into new except for one hit
        #     else:
        #         new_objects.append(pygame.Rect(random.randint(0, screen_width), random.randint(-screen_height, 0), 50, 50))

            
        # objects = new_objects

        screen.blit(night_background_img, [0,0])


        if chosen_character == oliver_icon:
            if character_is_facing_left:
                screen.blit(oliver_left_img, player_rect)
            else:
                screen.blit(oliver_right_img, player_rect)

        if chosen_character == lulu_icon:
            if character_is_facing_left:
                screen.blit(lulu_left_img, player_rect)
            else:
                screen.blit(lulu_right_img, player_rect)

        if chosen_character == miles_icon:
            if character_is_facing_left:
                screen.blit(miles_left_img, player_rect)
            else:
               screen.blit(miles_right_img, player_rect)

        if chosen_character == bear_icon:
            if character_is_facing_left:
                screen.blit(bear_left_img, player_rect)
            else:
                screen.blit(bear_right_img, player_rect)

        if chosen_character == eevee_icon:
            if character_is_facing_left:
                screen.blit(eevee_left_img, player_rect)
            else:
               screen.blit(eevee_right_img, player_rect)

        if chosen_character == willow_icon:
            if character_is_facing_left:
                screen.blit(willow_left_img, player_rect)
            else:
                screen.blit(willow_right_img, player_rect)

        for platform in platforms:
            if platform.w == 500:
                screen.blit(night_platform_small, platform)
            if platform.w == 700:
                screen.blit(night_platform_medium, platform)
            if platform == bottom_platform:
                screen.blit(night_platform_ground, platform)
        for object in objects:
            screen.blit(mail_img, object)
        for enemy in enemies:
            screen.blit(chocolate_img, enemy)

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

        if points == 20:
            paused_mode_1 = True
            pygame.draw.rect(screen, [255, 255, 255], restart_rect)
            pygame.draw.rect(screen, [255, 255, 255], return_rect)

            text_surface = lose_font.render("You win!!", True, [255, 255, 255])
            screen.blit(text_surface, [575, 400])

            text_surface = restart_font.render("Restart", True, [0, 0, 0])
            screen.blit(text_surface, [675, 510])

            text_surface = restart_font.render("Return", True, [0, 0, 0])
            screen.blit(text_surface, [675, 610])

            # if event.type == pygame.MOUSEBUTTONDOWN: #Makes start button work
            #     mouse_pos = pygame.mouse.get_pos()
            #     if restart_rect.collidepoint(mouse_pos): #Level select screen
            #         game_mode = "second title screen"

        if lives == 0:
            paused_mode_1 = True
            pygame.draw.rect(screen, [255, 255, 255], restart_rect)
            pygame.draw.rect(screen, [255, 255, 255], return_rect)

            text_surface = lose_font.render("You lose!", True, [255, 255, 255])
            screen.blit(text_surface, [600, 400])

            text_surface = restart_font.render("Restart", True, [0, 0, 0])
            screen.blit(text_surface, [675, 510])

            text_surface = restart_font.render("Return", True, [0, 0, 0])
            screen.blit(text_surface, [675, 610])
                # if event.type == pygame.MOUSEBUTTONDOWN: #Makes start button work
            # mouse_pos = pygame.mouse.get_pos()
            # if restart_rect.collidepoint(mouse_pos): #Level select screen
            #     game_mode = "second title screen"


    pygame.display.flip()
    fps_clock.tick(FPS)