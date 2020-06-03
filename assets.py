import pygame
import os
from config import *

BACKGROUND = 'background'
HEROI_IMG = 'heroi_img'
DRACULA_IMG = 'dracula_img'
SCORE_FONT = 'score_font'
DYING_SOUND = 'dying_sound'
DAMAGING_SOUND = 'damaging_sound'
HEROI2_IMG = 'heroi2_img'


def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'cthulhu.jpg')).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets['background'], (LARGURA, ALTURA))
    assets[HEROI_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'Heroi.png')).convert_alpha()
    assets[HEROI_IMG] = pygame.transform.scale(assets['heroi_img'], (HEROI_LARGURA, HEROI_ALTURA))
    assets[DRACULA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'Dracula.jpg')).convert_alpha()
    assets[DRACULA_IMG] = pygame.transform.scale(assets['dracula_img'], (DRACULA_LARGURA, DRACULA_ALTURA))
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)
    assets[HEROI2_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'Heroi2.jpg')).convert_alpha()
    assets[HEROI2_IMG] = pygame.transform.scale(assets['heroi2_img'], (HEROI_LARGURA, HEROI_ALTURA))
    #Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SOM_DIR, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(0.4)
    assets[DYING_SOUND] = pygame.mixer.Sound(os.path.join(SOM_DIR, 'pew.wav'))
    assets[DAMAGING_SOUND] = pygame.mixer.Sound(os.path.join(SOM_DIR, 'pew.wav'))
    

    return assets