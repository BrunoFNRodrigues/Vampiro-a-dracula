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
        self.rect.centerx = LARGURA / 4
        self.rect.top = 20
        self.groups = groups
        self.assets = assets
        self.health = 100
        self.velocidade_x=0
        self.velocidade_y=0
    def update(self):
        # Atualização da posição do jogador
        self.rect.x += self.velocidade_x
        # Mantem dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > ALTURA:
            self.rect.bottom = ALTURA

    def attack(self):
        #Gera o dano do ataque 
        self.damage = random.randint(5,15) #ERRO AO DEFINIR DANO ALEATÓRIO
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
       self.assets = assets
    def attack(self):
        #Gera o dano do ataque
        self.damage = random.randint(1,15)
        self.assets[DAMAGING_SOUND].play()
