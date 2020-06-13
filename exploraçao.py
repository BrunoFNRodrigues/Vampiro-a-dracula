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
     
    DONE = 0
    PLAYING = 1
    keys_down = {}
    state = PLAYING

    player.lutando = False
    while state != DONE:
        clock.tick(FPS)

        #Trata eventos
        for event in pygame.event.get():
            #Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            #Só libera o teclado se está jogando
            if state == PLAYING:
                # verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:

                    keys_down[event.key] = True
                    if event.key == pygame.K_a:
                        player.velocidade_x -= 8
                    if event.key == pygame.K_d:
                        player.velocidade_x  += 8
                    if event.key == pygame.K_w:
                        player.velocidade_y -= 8
                    if event.key == pygame.K_s:
                        player.velocidade_y  += 8
                    if player.rect.right == LARGURA:
                        if event.key == pygame.K_e:
                            player.assets[DAMAGING_SOUND].play()
                            return BATTLE 

                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_a:
                            player.velocidade_x += 8
                        if event.key == pygame.K_d:
                            player.velocidade_x -= 8
                        if event.key == pygame.K_w:
                            player.velocidade_y += 8
                        if event.key == pygame.K_s:
                            player.velocidade_y  -= 8
   

        all_sprites.update()
        fundo.fill(BLACK)
        
        #Desenha a vida do Heroi:]
        vida_coracao = player.health/20
        vida_coracao = int(vida_coracao)
        text_surface = assets[SCORE_FONT].render(chr(9829)*vida_coracao, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (100, ALTURA - 670)
        fundo.blit(text_surface, text_rect)

        
        all_sprites.draw(fundo)
        pygame.display.update()
        
    return state
