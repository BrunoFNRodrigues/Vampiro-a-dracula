#-------INCIANDO---------
#Importa e incia as biblietecas
import pygame 
from config import *
from assets import *
from sprites import *

def win_screen(window):
    #Variveis de ajuste
    clock = pygame.time.Clock()

    assets = load_assets()

    #Carregando tela
    background = assets[WINBACK]
    background_rect = background.get_rect()

    assets[WIN_MUSIC].play()

    running = True
    while running:
        #Velocidade do jogo
        clock.tick(FPS)

        #Trata eventos
        for event in pygame.event.get():
            #Verifica se foi fechado
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

        #Redesenha a tela
        window.fill(GREY)
        window.blit(background, background_rect)

        pygame.display.update()

    return state
            

