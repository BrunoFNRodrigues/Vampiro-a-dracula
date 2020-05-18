import pygame

branco=(255,255,255)
preto=(0,0,0)


largura=1100
altura=720
tamanho = 20
pos_x=largura/2
pos_y=altura/2

fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Dracula Adventure')

sair = True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
        if event.type == pygame.KEYDOWN:
            keys_down[event.key] = True
            if event.key == pygame.K_a:
                pos_x-=15
            if event.key == pygame.K_d:
                pos_x+=15
            if event.key == pygame.K_w:
                pos_y-=15
            if event.key == pygame.K_s:
                pos_y+=15
        if event.type == pygame.KEYUP:
            if event.key in keys_down and keys_down[event.key]:
                if event.key == pygame.K_a:
                    player.speedx += 15
                if event.key == pygame.K_d:
                    player.speedx -= 15
                if event.key == pygame.K_w:
                    player.speedx += 15
                if event.key == pygame.K_s:
                    player.speedx -= 15

    fundo.fill(preto)
    pygame.draw.rect(fundo, branco, [pos_x,pos_y,tamanho,tamanho])
        
    pygame.display.update()

pygame.quit()

