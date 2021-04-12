#-------INCIANDO---------
#Importa e incia as biblietecas
import pygame
import random 
from config import *
from assets import *
from sprites import *

def desenhaVida(assets, personagem, window, cor):
    text_surface = assets[SCORE_FONT].render("{:03}".format(personagem.health), True, cor)
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = (personagem.rect.right, personagem.rect.top)
    window.blit(text_surface, text_rect)

def battle_screen(window):
    # Variveis de ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    
    #Criando o jagador
    player = Hero2(groups, assets, HEROI_IMG, 1)
    all_sprites.add(player)
    #Criando o Boss
    boss = Boss(assets, DRACULA_IMG, 2)
    all_sprites.add(boss)
   
    
    DONE = 0
    PLAYING = 1
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
                return QUIT
            #Só libera o teclado se está jogando
            if state == PLAYING:
                #Verifica se turno do jogador
                if SUA_VEZ:
                    #Verifica se apertou alguma tecla.
                    if event.type == pygame.KEYDOWN:
                        #Seleciona opções no menu de combate
                        keys_down[event.key] = True
                        #Define a função de ataque
                        if event.key == pygame.K_1:
                            player.attack(15,22)
                            boss.health -= player.damage
                            SUA_VEZ = False
                        #Define a ação de defender
                        if event.key == pygame.K_2:
                            guard = True
                            SUA_VEZ = False
                        #Define a ação de usar cura
                        if event.key == pygame.K_3:
                            if player.health<100:
                                assets[HEAL_MUSIC].play()
                                player.health += (random.randint(10,15))
                                SUA_VEZ = False
                                if player.health > 100:
                                    player.health = 100
                        #Define a ação de fugir
                        if event.key == pygame.K_4:
                            pygame.mixer.music.stop()
                            return OVER
                                   
                else:
                    #Vez do chefe
                    pygame.time.delay(500)
                    boss.attack(1,15)
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

        #Checa status dos personagens(Pode ser extraido)
        if state == PLAYING:
            #Verifica se player morreu
            if player.health <= 0:
                #Toca o som de morte
                assets[DYING_SOUND].play()
                pygame.mixer.music.stop()
                return OVER
                
            #Verifica se chefão morreu
            if boss.health <= 0:
                #Toca o som de morte
                assets[DYING_SOUND].play()
                pygame.mixer.music.stop()
                return WIN
                
        #====Gera saídas=====
        window.fill(BLACK) #Preenche com a cor preta
        window.blit(assets[BACKGROUND], (0, 0))
        #Desenhando os personagens
        all_sprites.draw(window)

        #Desenha a vida(Pode ser extraido)
        #Heroi
        desenhaVida(assets, player, window, WHITE)

        #Dracula
        desenhaVida(assets, boss, window, RED)

        pygame.display.update() # Atualiza o novo frame

    return state


