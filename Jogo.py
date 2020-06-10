#===inciando===
#Importa e inicia pacotes
import  pygame
import random
from config import *
from battle_screen import battle_screen
from exploraçao import exploracao_screen
from win_screen import win_screen
from over_screen import over_screen
from tela_inicial import tela_inicial

pygame.init()
pygame.mixer.init()

#=====>Gera telas
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Vampiro a Dracula')

state = BATTLE
while state != QUIT:
    if state == INIT:
        state = tala_incial(window)
    elif state == GAME:
        state = exploracao_screen(window)
    elif state == BATTLE:
        state = battle_screen(window)
    elif state == WIN:
        state = win_screen(window)
    elif state == OVER:
        state = over_screen(window)
    else:
        state = QUIT

#_______ENCERRANDO________
pygame.quit() #Função que finaliza o pygame