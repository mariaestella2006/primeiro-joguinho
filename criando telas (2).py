import pygame
from pygame.locals import * 
from sys import exit
from random import randint

pygame.init()

#variaveis
altura_janela= 480
largura_janela= 640
titulo_janela= "primeiro joguinho"

#informaços do retangulo
pos_x_rect= 500
pos_y_rect= 200
largura_rect= 25
altura_rect= 25
rgb_rect= 255,192,203
fonte= pygame.font.SysFont('arial', 40, True, False)
pontos= 0 

#informaçoes do circulo
pos_x_cir= 200
pos_y_cir= 200
raio=15
rgb_circle= 213,39,106

tela = pygame.display.set_mode((largura_janela,altura_janela))
relogio= pygame.time.Clock ()
pygame.display.set_caption(titulo_janela)

while True:
    relogio.tick(30)
    tela.fill((0,0,0))
    mensagem= f'Pontos: {pontos}'
    caixa_texto= fonte.render(mensagem, False, (255,255,255))
    
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            exit()
            
        # if event.type == KEYDOWN:
        #     if event.key == K_a:
        #         pos_x_rect -=5
        #     if event.key == K_d:
        #         pos_x_rect +=5
        #     if event.key == K_w:
        #         pos_y_rect -= 5
        #     if event.key == K_s:
        #         pos_y_rect += 5
    
    if pygame.key.get_pressed()[K_a]:
        pos_x_rect -= 10
    elif pygame.key.get_pressed()[K_d]:
        pos_x_rect += 10
    elif pygame.key.get_pressed()[K_w]:
        pos_y_rect -= 10
    elif pygame.key.get_pressed()[K_s]:
        pos_y_rect += 10
        
    if pos_x_rect >= largura_janela:
        pos_x_rect = 0 
    elif pos_x_rect <= 0:
        pos_x_rect = largura_janela
    if pos_y_rect >= altura_janela:
        pos_y_rect = 0
    elif pos_y_rect <=0:
        pos_y_rect = altura_janela
    
    
    retangulo= pygame.draw.rect(tela, (rgb_rect) , (pos_x_rect,pos_y_rect,largura_rect,altura_rect)) 
    
    circulo= pygame.draw.circle(tela , (rgb_circle), (pos_x_cir,pos_y_cir), raio)
    
    if retangulo.colliderect(circulo):
        pos_x_cir = randint(40,600)
        pos_y_cir = randint(40,600)
        pontos +=1
    
    tela.blit(caixa_texto, (400,40))
    pygame.display.update()
    
