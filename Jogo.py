#===inciando===
#Importa e inicia pacotes
import  pygame
import random
from config import *
from battle_screen import battle_screen

pygame.init()
pygame.mixer.init()

#=====>Gera tela de combate
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Vampiro a Dracula')

state = BATTLE
while state != QUIT:
    if state == BATTLE:
        state = battle_screen(window)
    else:
        state = QUIT

#_______ENCERRANDO________
pygame.quit() #Função que finaliza o pygame