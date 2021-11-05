import pygame, collide
from random import randint
from pygame.constants import KEYDOWN, QUIT
pygame.init()

screenX = 800 
screenY = 600
screen = pygame.display.set_mode((screenX,screenY))
 
player = pygame.image.load('dragon.png')
playerX = screenX/5
playerY=screenY/2
playerY_change=-1

grass = pygame.image.load('cactus.png')
grass = pygame.transform.scale(grass, (40,64))
grassX = screenX-64
grassY = screenY/2
grassX_change = -0.2

cloud = pygame.image.load('cloud.jpg')
cloudX = randint(0,int(screenX*.9))
cloudY = randint(0,int(screenY/7))
cloudX_change = -.1
cloudY_change = -.2

space = "off"
running = True
while running : 

    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space = "on"                

    
    cloudX += cloudX_change
    if space == 'on':
        playerY+= playerY_change
        if(playerY<=screenY/2-64):
            playerY = screenY/2-64
            playerY_change *= -1
        
        if(playerY>=screenY/2):
            playerY = screenY/2
            playerY_change *= -1
            space = "off"
        
    screen.blit( cloud, (cloudX, cloudY) )

    screen.blit(player, (playerX,playerY))

    grassX += grassX_change
    # if grassX<= 400:
    #     screen.blit(grass, (grassX, grassY))    

    screen.blit(grass, (grassX, grassY))
    if collide.collision(playerX, playerY, grassX, grassY) is True:
        running = False

    pygame.display.update()


