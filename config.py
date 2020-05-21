from os import path

# Define a pasta das imagens e audios.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SOM_DIR = path.join(path.dirname(__file__), 'assets', 'som')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'fnt')

# Dados de tela.
LARGURA = 1100
ALTURA = 720
FPS = 60 # Taxa de atualização em frames por segundo

#Comandos
#Movimentação (W,A,S,D)
#Interagir (E)

#=====Tamanho dos elementos=====

#Heroi
HEROI_ALTURA = 100
HEROI_LARGURA = 50

#Drácula
DRACULA_ALTURA = 150
DRACULA_LARGURA = 75

#Cores
BLACK = (0,0,0)
RED = (255,0,0)

#Estados de jogo
INIT = 0
GAME = 1
OVER = 2
QUIT = 3
