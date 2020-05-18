import pygame
import os
import config

BACKGROUND = 'background'
HEROI_IMG = 'heroi_img'
DRACULA_IMG =   'dracula_img'

def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'cthulhu.jpg')).convert()

    