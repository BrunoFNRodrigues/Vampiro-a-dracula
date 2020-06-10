import pygame
from config import *
from assets import *

def tela_inicial(fundo):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()

    # Carrega o fundo da tela inicial
    background_rect = assets[BACKGROUND].get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = BATTLE
                running = False

        # A cada loop, redesenha o fundo e os sprites
        fundo.fill(BLACK)
        fundo.blit(assets[BACKGROUND], background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state