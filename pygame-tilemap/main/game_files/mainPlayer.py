import pygame as pg
from game_files.textures import Texture
from game_files.__init__ import Window

WINDOW = Window.WINDOW
CONTINUE = True
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20
img_size = 17
img = pg.transform.scale(Texture.GRASS_IMAGE,(img_size,img_size))


class Player(object):
    def __init__(self,x,y,width,height,jumpRange,GRAVITY):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isJump = False
        self.vel_y = 0
        self.index = 0
        self.jumpRange = jumpRange
        self.is_falling = True
        self.GRAVITY = GRAVITY

    #DRAW PLAYER + COLLISION WITH BLOCKS
    def Draw(self):
        self.player = Texture.player
        self.player = pg.transform.scale(self.player,(PLAYER_WIDTH,PLAYER_HEIGHT))
        self.player_rect = self.player.get_rect()
        WINDOW.blit(self.player,dest=(self.x,self.y))
        self.player_rect.x = round(self.x)
        self.player_rect.y = round(self.y)

        #COLLISION WITH BLOCKS
        for tile in self.tile_list:
            if self.player_rect.colliderect(tile[1]):
                self.player_rect.bottom = tile[1].top
                self.y = self.player_rect.y


    #CONTROLS      
    def handle_keys(self,speed,vel_y):
        keys = pg.key.get_pressed()
        self.speed = speed
        self.vel_y = vel_y
        if keys[pg.K_RIGHT]:
            if CONTINUE == True:
                self.x += speed
        if keys[pg.K_LEFT]:
            if CONTINUE == True:
                self.x -= speed

    #MAKE PLAYER TO JUMP WHEN KEY SPACE IS PRESSED
    def jump(self,jumpRange):
        if CONTINUE == True:
            if self.isJump == True:
                self.is_falling = False
                if self.jumpRange >= -11:
                    self.is_falling = False
                    neg = 1
                    if self.jumpRange < 0:
                        neg = -1
                    self.y -= self.jumpRange**2 * 0.1 * neg
                    self.jumpRange -= 1
                else:
                    self.is_falling = True
                    self.isJump = False
                    self.jumpRange = jumpRange

    #GRAVITY TO MAKE PLAYER FALL
    def gravity(self):
        if self.is_falling == True:
            if self.isJump == False:
                self.y += self.GRAVITY


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