#-------INCIANDO---------
#Importa e incia as biblietecas
import pygame
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
        health = 100

        #======Ciclo principal=======
        pygame.mixer.music.play(loops=-1)
        while state != DONE:
            clock.tick(FPS)

            #Trate eventos
            for event in pygame.event.get():
                #Verifica consequências
                if event.type == pygame.QUIT:
                    state = DONE
                #Só verifica o teclado se está no estado
                if state == PLAYING:
                    #Verifica se apertou alguma tecla.
                    if event.type == pygame.KEYDOWN:
                        