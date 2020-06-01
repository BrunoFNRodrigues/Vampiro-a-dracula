import pygame
from sprites import *
from assets import *
from config import *
from Jogo import *

def exploracao_screen(fundo):
    clock = pygame.time.Clock()

    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    
    #Criando o jagador
    player = Hero(groups, assets)
    all_sprites.add(player)
    
    tamanho = 20
    pos_x=LARGURA/2
    pos_y=ALTURA/2

    sair = True

    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.velocidade_y = 0
                    player.velocidade_x-=0.5
                if event.key == pygame.K_d:
                    player.velocidade_y=0
                    player.velocidade_x=0.5
                if event.key == pygame.K_w:
                    player.velocidade_x=0
                    player.velocidade_y=-0.5
                if event.key == pygame.K_s:
                    player.velocidade_x=0
                    player.velocidade_y=0.5
            
        fundo.fill(BLACK)
        pygame.draw.rect(fundo, WHITE, [pos_x,pos_y,tamanho,tamanho])
        pos_x+=player.velocidade_x
        pos_y+=player.velocidade_y
        pygame.display.update()
    
        all_sprites.update()


