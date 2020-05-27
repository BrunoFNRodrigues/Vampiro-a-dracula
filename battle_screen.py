#-------INCIANDO---------
#Importa e incia as biblietecas
import pygame
import random 
from config import *
from assets import *
from sprites import *

def battle_screen(window):
    # Variveis de ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    
    #Criando o jagador
    player = Hero(groups, assets)
    all_sprites.add(player)
    #Criando o Boss
    boss = Boss(assets)
    all_sprites.add(boss)
    #
   
    
    DONE = 0
    PLAYING = 1
    WIN = True
    state = PLAYING

    keys_down = {}
    guard = False

    #======Ciclo principal=======
    pygame.mixer.music.play(loops=-1)
    while state != DONE:
        clock.tick(FPS)

        #Trata eventos
        for event in pygame.event.get():
            #Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            #Só verifica o teclado se está no estado
            if state == PLAYING:
                #Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    #Seleciona opções no menu de combate
                    keys_down[event.key] = True
                    #Define a função de ataque
                    if event.key == pygame.K_1:
                        player.attack()
                        boss.health -= player.damage
                    #Define a ação de defender
                    if event.key == pygame.K_2:
                        guard = True
                    #Define a ação de usar cura
                    if event.key == pygame.K_3:
                        if player.health<100:
                            player.health += 5+(randint(0,10))
                    #Define a ação de fugir
                    if event.key == pygame.K_4:
                        state = DONE
                        WIN = False

    #======Atualiza o estado do jogo=======
    #Atualiza os status dos personagens
        all_sprites.update()

        if state == PLAYING:
            #Verifica se player morreu
            if player.health == 0:
                #Toca o som de morte
                assets[DYING_SOUND].play()
                WIN = False
                state = DONE
            #Verifica se chefão morreu
            if boss.health == 0:
                #Toca o som de morte
                assets[DYING_SOUND].play()
                WIN = True
                state = DONE

        #====Gera saídas=====
        window.fill(BLACK) #Preenche com a cor preta
        window.blit(assets[BACKGROUND], (0, 0))
        #Desenhando os personagens
        all_sprites.draw(window)

        #Desenha as barras de vida
        #Heroi
        text_surface = assets[SCORE_FONT].render(chr(9829) * player.health, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (100, ALTURA - 10)
        window.blit(text_surface, text_rect)
        #Dracula
        text_surface = assets[SCORE_FONT].render(chr(9829) * boss.health, True, GREY)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, ALTURA - 30)
        window.blit(text_surface, text_rect)

        pygame.display.update() # Atualiza o novo frame

            