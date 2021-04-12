import pygame
import random
from config import *
from assets import *


class Personagem(pygame.sprite.Sprite):
    def __init__(self, assets, img, fator_vida):
        pygame.sprite.Sprite.__init__(self)
        self.assets = assets
        self.fator_vida = fator_vida
        self.health = 100*fator_vida
        self.image = self.assets[img]
        self.rect = self.image.get_rect()

    def attack(self, min, max):
        self.damage = random.randint(min,max)
        self.assets[DAMAGING_SOUND].play()

class Hero(Personagem):
    def __init__(self, groups, assets, img, fator_vida):
        # Construindo o sprite
        Personagem.__init__(self, assets, img, fator_vida)
        self.groups = groups
        self.velocidade_x=0
        self.velocidade_y=0
        self.rect.centerx = LARGURA/2
        self.rect.centery = ALTURA/2

    def update(self):

        # Atualização da posição do jogador
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y
        # Mantem dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > ALTURA:
            self.rect.bottom = ALTURA

class Hero2(Personagem):
    def __init__(self, groups, assets, img, fator_vida):
        # Construindo o sprite
        Personagem.__init__(self, assets, img, fator_vida)
        self.groups = groups
        self.velocidade_x=0
        self.velocidade_y=0
        self.rect.centerx = LARGURA / 4
        self.rect.top = 445


class Boss(Personagem):
    def __init__(self, assets, img, fator_vida):
       # Construindo o sprit
       Personagem.__init__(self, assets, img, fator_vida)
       self.rect.right = LARGURA*2.9 / 4
       self.rect.top = 350



