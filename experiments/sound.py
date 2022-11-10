import pygame
from pygame.locals import *
from pygame import mixer

pygame.init()
width = 1000
height = 500
window = pygame.display.set_mode((width, height))
bg_img = pygame.image.load('bg.jpg')
bg_img = pygame.transform.scale(bg_img, (width, height))

mixer.init()
mixer.music.load('bgmusic.mp3')
mixer.music.play()

runing = True
while runing:
    window.blit(bg_img, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
    pygame.display.update()
pygame.quit()
