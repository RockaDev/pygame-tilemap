import pygame as pg
import sys
from game_files.mapdata import game_map_data
from game_files.__init__ import Window
from game_files.textures import Texture
from game_files.mainPlayer import Player

print('Game is running..')

#CONSTANT VARIABLES
#WIDTH;HEIGHT
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20

#WINDOW
WINDOW = Window.WINDOW

player = Player(x=30,y=500,width=PLAYER_WIDTH,height=PLAYER_HEIGHT,jumpRange=11,GRAVITY=4)

#LOADING MAP FROM MAPDATA.PY
game_map_data = game_map_data
gamemap = player.tile(data=game_map_data,tile_size=17,img_size=20)

#FPS
clock = pg.time.Clock()

while True:
    FPS = 60
    clock.tick(FPS)

    #EVENTS  
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.is_falling = False
                player.isJump = True

    SKY_POSITION = (0,0)

    #CALLED FUNCTIONS
    WINDOW.blit(Texture.sky,SKY_POSITION)
    player.draw_tile()
    player.jump(jumpRange=11)
    player.Draw()
    player.gravity()
    player.handle_keys(speed=3,vel_y=3)
    pg.display.update()
    pg.display.flip()