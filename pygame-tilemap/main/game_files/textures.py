import pygame as pg

class Texture:
    GRASS_IMAGE = pg.image.load(r'C:\Users\mineo\Desktop\pygame-tilemap\main\game_files\assets\platform.jpg')
    sky = pg.image.load(r'C:\Users\mineo\Desktop\pygame-tilemap\main\game_files\assets\sky.png')
    sky = pg.transform.scale(sky,(800,599))
    player = pg.image.load(r'C:\Users\mineo\Desktop\pygame-tilemap\main\game_files\assets\player.png')