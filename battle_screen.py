#-------INCIANDO---------
#Importa e incia as biblietecas
import pygame
import random
from config import ALTURA, LARGURA, FPS
from assets import load_assets, BACKGROUND

def battle_screen(window):
    # Variveis de ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    #Criando o jagador
    player = Hero(groups, assets)
    all_sprites.add(player)
    #Criando o Boss
    boss = Boss(groups, assets)
    all_sprites.add(boss)

        WIN = 0
        PLAYING = 1
        DAMAGING = 2
        LOSE = 3
        state = PLAYING

        keys_down = {}
        hero_health = 100
        boss_health = 300
        guard = True

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
                            damage = 10+random.randint(1,15)
                            boss_health -= damage
                        #Define a ação de defender
                        if event.key == pygame.K_2:
                            guard = True
                        #Define a ação de usar cura
                        if event.key == pygame.K_3:
                            if hero_health<100:
                                hero_health += 5+random.randint(0,10)
                        #Define a ação de fugir
                        if event.key == pygame.k_4:
                            state = DONE
                        