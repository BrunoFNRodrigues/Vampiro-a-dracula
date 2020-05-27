import pygame
import random
from config import *
from assets import *


class Hero(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construindo o sprite
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[HEROI_IMG]
        self.rect = self.image.get_rect()
        self.rect.left = LARGURA / 4
        self.rect.top = 20
        self.groups = groups
        self.assets = assets
        self.health = 100
    def attack(self):
        #Gera o dano do ataque 
        self.damage = 20 #ERRO AO DEFINIR DANO ALEATÓRIO
        self.assets[DAMAGING_SOUND].play()

class Boss(pygame.sprite.Sprite):
    def __init__(self, assets):
       # Construindo o sprit
       pygame.sprite.Sprite.__init__(self)

       self.image = assets[DRACULA_IMG]
       self.rect = self.image.get_rect()
       self.rect.right = LARGURA*3 / 4
       self.rect.top = 20
       self.health = 200
