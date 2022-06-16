import pygame, sys, random
from game import create_screen, screen_width, screen_height, gameplay


screen = create_screen()
# Load image frames
player_surf = pygame.image.load("assets/joe/0.png").convert_alpha()
game_over_surf = pygame.image.load("assets/gameOver.png").convert_alpha()

# scale image frames
player_surf = pygame.transform.scale(player_surf, (30, 43))
game_over_surf = pygame.transform.scale(game_over_surf, (230, 150))

# creating spikes
spikes_surf = pygame.image.load("assets/spikes.png").convert_alpha()
spikes_surf = pygame.transform.scale(spikes_surf, (100, 20))

player_rect = pygame.Rect(110, screen_height - 145 ,30,43) # x, y, width, height

spikes_rect1 = pygame.Rect(310, screen_height - 110 ,100,20)
spikes_rect2 = pygame.Rect(510, screen_height - 110 ,100,20)


player_vel_x = 0
player_vel_y = 0

def key_down(event):
    global player_vel_x, player_vel_y

    if(event.type == pygame.KEYDOWN):
        if(event.key == pygame.K_RIGHT):
            player_vel_x = 5
        elif(event.key == pygame.K_LEFT):
            player_vel_x = -5
        elif(event.key == pygame.K_SPACE):
            player_vel_y = -15


def key_up(event):
    global player_vel_x
    if(event.type == pygame.KEYUP):
        if(event.key == pygame.K_RIGHT):
            player_vel_x = 0
        elif(event.key == pygame.K_LEFT):
            player_vel_x = 0



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        key_down(event)
        key_up(event)

    gameplay()

    screen.blit(spikes_surf,spikes_rect1)
    screen.blit(spikes_surf,spikes_rect2)
    screen.blit(player_surf,player_rect)


    # updating x and y co-ordinate
    player_rect.x += player_vel_x
    player_rect.y += player_vel_y


    # adding gravity
    player_vel_y += 0.8


    if(spikes_rect1.colliderect(player_rect)):
        screen.blit(game_over_surf,(screen_width / 2 - 120,100))
        player_vel_x = 0
        player_vel_y = 0

    if(spikes_rect2.colliderect(player_rect)):
        screen.blit(game_over_surf,(screen_width / 2 - 120,100))
        player_vel_x = 0
        player_vel_y = 0


    pygame.display.update()
