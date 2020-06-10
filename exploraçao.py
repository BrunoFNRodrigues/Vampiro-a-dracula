import pygame
from sprites import *
from assets import *
from config import *


def exploracao_screen(fundo):
    clock = pygame.time.Clock()

    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    
    #Criando o jagador
    player = Hero(groups, assets)
    all_sprites.add(player)
     
    keys_dowm = {}

    sair = True
    player.lutando = False
    while sair:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                keys_dowm[event.key] = True
                if event.key == pygame.K_a:
                    player.velocidade_x-=50
                if event.key == pygame.K_d:
                    player.velocidade_x +=50
                if event.key == pygame.K_w:
                    player.velocidade_y-=50
                if event.key == pygame.K_s:
                    player.velocidade_y+=50
            
        fundo.fill(BLACK)
        
        #Desenha a vida do Heroi:

        text_surface = assets[SCORE_FONT].render(chr(9829)*5, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (100, ALTURA - 670)
        fundo.blit(text_surface, text_rect)

        all_sprites.update()
        all_sprites.draw(fundo)
        pygame.display.update()
