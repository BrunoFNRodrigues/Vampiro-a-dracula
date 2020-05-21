import pygame
import os
import config

BACKGROUND = 'background'
HEROI_IMG = 'heroi_img'
DRACULA_IMG = 'dracula_img'
SCORE_FONT = 'score_font'
DYING_SOUND = 'dying_sound'
DAMAGING_SOUNG = 'damaging_sound'



def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'cthulhu.jpg')).convert()
    assets[HEROI_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'Heroi.jpg')).convert_alpha()
    assets[HEROI_IMG] = pygame.transform.scale(assets['heroi_img'], (HEROI_LARGURA, HEROI_ALTURA))
    assets[DRACULA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'Dracula.jpg')).convert_alpha()
    assets[DRACULA_IMG] = pygame.transform.scale(assets['dracula_img'], (DRACULA_LARGURA, DRACULA_ALTURA))
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)
    
    #Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SND_DIR, 'Tank!'))
    pygame.mixer.music.set_volume(0.4)
    assets[DYING_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'morte.mp3'))
    assets[DAMAGING_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'dano.mp3'))
    

    return assets