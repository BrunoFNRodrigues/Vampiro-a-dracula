import pygame
import config
import assets


class Hero(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construindo o sprite
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[HEROI_IMG]
        self.rect = self.image.get_rect()
        self.rect.left = LARGURA / 4
        self.rect.top = 10 
        self.groups = groups
        self.assets = assets


