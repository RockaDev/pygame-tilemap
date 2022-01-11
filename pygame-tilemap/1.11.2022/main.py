import pygame as pg
import sys
import os
from pygame import image
from pygame import rect
from mapdata import game_map_data

#ASSETS
GRASS_IMAGE = pg.image.load(r'C:\Users\mineo\Desktop\pygame-tilemap-main\1.11.2022\assets\platform.jpg')
sky = pg.image.load(r'C:\Users\mineo\Desktop\pygame-tilemap-main\1.11.2022\assets\sky.png')
CONTINUE = True

#CONSTANT VARIABLES
#WIDTH;HEIGHT
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 598
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20
#COLORS
COLOR_DARKBLUE = 'darkblue'
COLOR_RED = 'red'
#WINDOW
WINDOW = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

sky = pg.transform.scale(sky,(800,599))

class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Draw(self,):
        self.player = pg.image.load(r'C:\Users\mineo\Desktop\pygame-tilemap-main\1.11.2022\assets\player.png')
        self.player = pg.transform.scale(self.player,(PLAYER_WIDTH,PLAYER_HEIGHT))
        self.player_rect = self.player.get_rect()
        WINDOW.blit(self.player,dest=(self.x,self.y))
        self.player_rect.x = self.x
        self.player_rect.y = self.y


        for tile in self.tile_list:
            if tile[1].colliderect(self.player_rect.x,self.player_rect.y,PLAYER_WIDTH,PLAYER_HEIGHT):
                pass




    def handle_keys(self,speed):
        keys = pg.key.get_pressed()
        self.speed = speed
        if keys[pg.K_RIGHT]:
            if CONTINUE == True:
                self.x += speed
        if keys[pg.K_LEFT]:
            if CONTINUE == True:
                self.x -= speed
        if keys[pg.K_DOWN]:
            if CONTINUE == True:
                self.y += speed
        if keys[pg.K_UP]:
            if CONTINUE == True:
                self.y -= speed

    ###########
    ##TILEMAP##
    ###########

    def tile(self,data,tile_size,img_size):
        self.tile_list = []

        #SAVING TILES IN A LIST

        row_count = 0
        self.tile_size = tile_size
        self.img_size = img_size

        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    self.rect_img = img.get_rect()
                    self.rect_img.x = col_count * tile_size
                    self.rect_img.y = row_count * tile_size
                    tile = (img,self.rect_img)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    #DRAWING TILES FROM THE LIST
    def draw_tile(self):
        for tile in self.tile_list:
            WINDOW.blit(tile[0], tile[1])



#FPS
clock = pg.time.Clock()


game_map_data = game_map_data


#PLAYER
player = Player(x=30,y=30,width=PLAYER_WIDTH,height=PLAYER_HEIGHT)


img_size = 17
img = pg.transform.scale(GRASS_IMAGE,(img_size,img_size))
gamemap = player.tile(game_map_data,17,20)



while True:
    FPS = 60
    pg.display.update()
    clock.tick(FPS)

    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    SKY_POSITION = (0,0)

    WINDOW.blit(sky,SKY_POSITION)
    player.draw_tile()
    player.Draw()
    player.handle_keys(speed=3)
    pg.display.update()
    pg.display.flip()