import pygame
import os
from config import *

BACKGROUND = 'background'
BACKGROUND2 = 'background2'
WINBACK = 'winback'
OVERBACK = 'overback'
HEROI_IMG = 'heroi_img'
DRACULA_IMG = 'dracula_img'
SCORE_FONT = 'score_font'
DYING_SOUND = 'dying_sound'
DAMAGING_SOUND = 'damaging_sound'
LOSE_MUSIC = 'lose_music'
WIN_MUSIC = 'win_music'
HEAL_MUSIC = 'heal_sound'

som_tela_inicial = 'som_tela_inicial'

def load_assets():
    assets = {}
    #Carrega as imagens do jogo
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'Castle.png')).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets['background'], (LARGURA, ALTURA))
    assets[BACKGROUND2] = pygame.image.load(os.path.join(IMG_DIR, 'dungeonFloor.png')).convert()
    assets[BACKGROUND2] = pygame.transform.scale(assets['background2'], (LARGURA, ALTURA))
    assets[WINBACK] = pygame.image.load(path.join(IMG_DIR, 'win.png')).convert_alpha()
    assets[WINBACK] = pygame.transform.scale(assets['winback'], (LARGURA, ALTURA))
    assets[OVERBACK] = pygame.image.load(path.join(IMG_DIR, 'lose.png')).convert_alpha()
    assets[OVERBACK] = pygame.transform.scale(assets['overback'], (LARGURA, ALTURA))
    assets[HEROI_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'Heroi.png')).convert_alpha()
    assets[HEROI_IMG] = pygame.transform.scale(assets['heroi_img'], (HEROI_LARGURA, HEROI_ALTURA))
    assets[DRACULA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'vampire.png')).convert_alpha()
    assets[DRACULA_IMG] = pygame.transform.scale(assets['dracula_img'], (DRACULA_LARGURA, DRACULA_ALTURA))
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)
    
    #Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SOM_DIR, 'Boss_battle.ogg'))
    pygame.mixer.music.set_volume(0.4)
    assets[DYING_SOUND] = pygame.mixer.Sound(os.path.join(SOM_DIR, 'pew.wav'))
    assets[DAMAGING_SOUND] = pygame.mixer.Sound(os.path.join(SOM_DIR, 'expl3.wav'))
    assets[LOSE_MUSIC] = pygame.mixer.Sound(os.path.join(SOM_DIR, 'lose.ogg'))
    assets[WIN_MUSIC] = pygame.mixer.Sound(os.path.join(SOM_DIR, 'win.ogg'))
    assets[HEAL_MUSIC] = pygame.mixer.Sound(os.path.join(SOM_DIR, '0054.wav'))


    assets[som_tela_inicial] = pygame.mixer.Sound(os.path.join(SOM_DIR, 'exploração.wav'))

    return assets