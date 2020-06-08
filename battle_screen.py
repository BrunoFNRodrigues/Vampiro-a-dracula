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
    #Escolhe o modo do heroi
    player.lutando = True
   
    
    DONE = 0
    PLAYING = 1
    WIN = True
    state = PLAYING
    SUA_VEZ = True
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
                #Verifica se turno do jogador
                if SUA_VEZ:
                    #Verifica se apertou alguma tecla.
                    if event.type == pygame.KEYDOWN:
                        #Seleciona opções no menu de combate
                        keys_down[event.key] = True
                        #Define a função de ataque
                        if event.key == pygame.K_1:
                            player.attack()
                            boss.health -= player.damage
                            SUA_VEZ = False
                        #Define a ação de defender
                        if event.key == pygame.K_2:
                            guard = True
                            SUA_VEZ = False
                        #Define a ação de usar cura
                        if event.key == pygame.K_3:
                            if player.health<100:
                                player.health += (random.randint(5,15))
                                SUA_VEZ = False
                        #Define a ação de fugir
                        if event.key == pygame.K_4:
                            WIN = False
                            state = DONE
                else:
                    #Vez do chefe
                    pygame.time.delay(500)
                    boss.attack()
                    if guard:
                        guard = False
                        damage= boss.damage-10
                        if damage < 0:
                            damage = 0
                    else:
                        damage = boss.damage
                    player.health -= damage
                    SUA_VEZ = True            

    #======Atualiza o estado do jogo=======
    #Atualiza os status dos personagens
        all_sprites.update()

        if state == PLAYING:
            #Verifica se player morreu
            if player.health <= 0:
                #Toca o som de morte
                assets[DYING_SOUND].play()
                WIN = False
                state = DONE
            #Verifica se chefão morreu
            if boss.health <= 0:
                #Toca o som de morte
                assets[DYING_SOUND].play()
                WIN = True
                state = DONE

        #====Gera saídas=====
        window.fill(BLACK) #Preenche com a cor preta
        window.blit(assets[BACKGROUND], (0, 0))
        #Desenhando os personagens
        all_sprites.draw(window)

        #Desenha a vida
        #Heroi
        text_surface = assets[SCORE_FONT].render("{:03}".format(player.health), True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (player.rect.centerx, player.rect.top)
        window.blit(text_surface, text_rect)
        #Dracula
        text_surface = assets[SCORE_FONT].render("{:03}".format(boss.health), True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (boss.rect.right, boss.rect.top)
        window.blit(text_surface, text_rect)

        pygame.display.update() # Atualiza o novo frame

    return state       