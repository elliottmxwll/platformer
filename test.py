#Part 14: Mute music button

#import modules
import pygame
from pygame.locals import *
import pickle
from os import path
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512) #these numbers configure mixer to play game sounds without lag
mixer.init()
pygame.init()

clock = pygame.time.Clock()
fps = 60


#create game window
screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

#define font
font = pygame.font.SysFont('Bauhaus 93', 70)
font_score = pygame.font.SysFont('Comic Sans', 30)

#define game variables
tile_size = 50
game_over = 0
main_menu = True
level = 3
max_levels = 7
score = 0

#define colours
white = (255, 255, 255)
blue = (0, 0, 255)

#load images
sun_img = pygame.image.load('img/sun.png')
bg_img = pygame.image.load('img/sky.png')
restart_img = pygame.image.load('img/restart_btn.png')
start_img = pygame.image.load('img/start_btn.png')
exit_img = pygame.image.load('img/exit_btn.png')
mute = pygame.image.load('img/mute_btn.png')
mute_img = pygame.transform.scale(mute, (50, 50))

#load sounds
coin_fx = pygame.mixer.Sound('img/coin.wav')
coin_fx.set_volume(0.5)
jump_fx = pygame.mixer.Sound('img/jump.wav')
jump_fx.set_volume(0.5)
game_over_fx = pygame.mixer.Sound('img/game_over.wav')
game_over_fx.set_volume(0.5)
pygame.mixer.music.load('img/music.wav')
pygame.mixer.music.play(-1, 0.0, 5000) #5000 miliseconds of delay

pygame.mixer.music.play(-1)

button = pygame.Rect(100, 150, 90, 30)
music_paused = False

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # [0] is left mouse button, 1 is mouse down
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0: # == 0 is mouse up
            self.clicked = False

        #draw button
        screen.blit(self.image, self.rect)

        return action

music_button = Button(screen_width - 60, 10, mute_img)

run = True
while run:
    
	
	
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else:
            if music_button.draw():
			# Toggle the boolean variable.
                music_paused = not music_paused
                if music_paused:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
        
            

    screen.blit(bg_img, (0, 0))
    music_button.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()