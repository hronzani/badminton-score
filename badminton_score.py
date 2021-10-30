#Placar eletronico, inicialmente planejado para ser usado em raspberry, usando pygame
#Idealizado para Badminton, porem pode ser adaptado para qualquer esporte
#Desenvolvido por Ricardo Hoffmann - ronzani@gmail.com - @hronzani

import pygame, os
import sys

os.environ['SDL_VIDEO_CENTERED'] = '1' # You have to call this before pygame.init()

if sys.version_info.major == 2:
    jog1 = raw_input("Entre com jogador 1: ")
    msg = 'Nome deve possuir ate 12 caracteres'
    while (len(jog1) > 12):
        print (msg)
        jog1 = raw_input("Entre com jogador 1: ")

    jog2 = raw_input("Entre com jogador 2: ")
    while (len(jog2) > 12):
        print (msg)
        jog2 = raw_input("Entre com jogador 2: ")

if sys.version_info.major == 3:
    jog1 = input("Entre com jogador 1: ")
    while (len(jog1) > 12):
        print('Nome tem que ter menos de 12 caracteres')
        jog1 = input("Entre com jogador 1: ")

    jog2 = input("Entre com jogador 2: ")
    while (len(jog2) > 12):
        print('Nome tem que ter menos de 12 caracteres')
        jog2 = input("Entre com jogador 2: ")

pygame.init()

info = pygame.display.Info() # You have to call this before pygame.display.set_mode()

screen_width = 800
screen_height = 600

#Uncomment the below to use fullscreen on pc with better resolutions (not tested, the cursor focus may need adjusts)
#screen_width,screen_height = info.current_w,info.current_h

window_width,window_height = screen_width-10,screen_height-10

win = pygame.display.set_mode((window_width,window_height))
pygame.mouse.set_visible(False)
pygame.display.update()

pygame.display.set_caption("Scoreboard") #Caso fosse mostrado

x = 2
y = 2
width = 70
height = 70
step = 50
game1 = 1
game2 = 0
game3 = 0
gcurrent = 0
saque = 0

score = [[0,0,0],[0,0,0]]

font = pygame.font.SysFont("arial", 60, True)
titl = pygame.font.SysFont("arial", 15, False)
ric  = pygame.font.SysFont("arial", 10, False)
# The first argument is the font, next is size # and then True to make our font bold

torneio = "RIO BONITO OPEN DE BADMINTON"
titulo = titl.render(torneio, 1, (255,255,255))
dev = ric.render("by @hronzani", 1, (255,255,255))

p1 = font.render(jog1, 1, (255,165,0)) # Arguments are: text, anti-aliasing, color
p2 = font.render(jog2 , 1, (0,255,0)) 

p11 = font.render(str(score[0][0]) , 1, (255,165,0)) #jogador1 game1
p12 = font.render(str(score[0][1]) , 1, (255,165,0)) #jogador1 game2
p13 = font.render(str(score[0][2]) , 1, (255,165,0)) #jogador1 game3

p21 = font.render(str(score[1][0]) , 1, (0,255,0)) #jogador2 game1
p22 = font.render(str(score[1][1]) , 1, (0,255,0)) #jogador2 game2
p23 = font.render(str(score[1][2]) , 1, (0,255,0)) #jogador2 game3

run = True

while run:
    pygame.time.delay(200)
        
    cursor1 = font.render(str(score[0][gcurrent]) , 1, (255,165,0))
    cursor2 = font.render(str(score[1][gcurrent]) , 1, (0,255,0))

       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_2: #a tecla 2 mostra o placar do game2 na tela
                game2 = 1  #Habilita placar para game2
                gcurrent = 1 #escrita na matriz de score na segunda coluna
                saque = 0
            if event.key == pygame.K_3:  #a tecla 3 mostra o placar do game3 na tela
                game3 = 1  #Habilita placar para game3
                gcurrent = 2 #escrita na matriz de score na terceira coluna
                saque = 0
            if event.key == pygame.K_4:
                game2 = 0  #Inibe placar para game2
                gcurrent = 0 #escrita na matrix de score na primeira coluna
                saque = 0
            if event.key == pygame.K_5:
                game3 = 0  #inibe placar para game3
                gcurrent = 1 #escrita na matrix de score na segunda coluna
                saque = 0
            if event.key == pygame.K_a:
                score[0][gcurrent] += 1 #A letra a incrementa o placar do jogador1 no game atual
                saque = 1
            if event.key == pygame.K_z:
                score[0][gcurrent]-= 1 #A letra z decrementa o placar do jogador1 no game atual (caso de algum erro)
                saque = 1
                if score[0][gcurrent] <= 0:  # Evitar placar negativo
                    score[0][gcurrent] = 0 
            if event.key == pygame.K_j:
                score[1][gcurrent] += 1 #A letra j incrementa o placar do jogador2 no game atual
                saque = 2
            if event.key == pygame.K_m:
                score[1][gcurrent]-= 1 #A letra m decrementa o placar do jogador2 no game atual (caso de algum erro)
                saque = 2
                if score[1][gcurrent] <= 0:  # Evitar placar negativo
                    score[1][gcurrent] = 0 
            if event.key == pygame.K_9: #Outra alternativa para quit
                run = False
     
    win.fill((0,0,0))  # Fills the screen with black
    #Escreve os nomes dos jogadores
    win.blit(p1, (10, window_height/4)) 
    win.blit(p2, (10, window_height/2))
    win.blit(titulo, (0.35*window_width, 0.95*window_height))
    win.blit(dev, (0.90*window_width, 0.97*window_height))
    

    #Mostra placar do primeiro game
    if game1 == 1:
        cursor1 = font.render(str(score[0][gcurrent]) , 1, (255,165,0))
        cursor2 = font.render(str(score[1][gcurrent]) , 1, (0,255,0))
    
        if gcurrent == 0:
            if saque == 1: #Foco no placar1
                pygame.draw.rect(win, (255,165,0), (0.45*window_width + step - x, window_height/4 - y, width, height))
                cursor1 = font.render(str(score[0][0]) , 1, (0,0,0))
                cursor2 = font.render(str(score[1][0]) , 1, (0,255,0))
        
            if saque == 2: #Foco no placar2
                pygame.draw.rect(win, (0,255,0), (0.45*window_width +step - x, window_height/2 - y, width, height))
                cursor2 = font.render(str(score[1][0]) , 1, (0,0,0))
    
            win.blit(cursor1, (0.45*window_width + step, window_height/4))
            win.blit(cursor2, (0.45*window_width + step, window_height/2))
        else:
            if score[0][0]>score[1][0]: #Jogador1 venceu o game, deixa o foco no placar1
                pygame.draw.rect(win, (255,165,0), (0.45*window_width + step - x, window_height/4 - y, width, height))
                p11 = font.render(str(score[0][0]) , 1, (0,0,0))
                p21 = font.render(str(score[1][0]) , 1, (0,255,0))
            else:
                pygame.draw.rect(win, (0,255,0), (0.45*window_width + step - x, window_height/2 - y, width, height))
                p11 = font.render(str(score[0][0]) , 1, (255,165,0))
                p21 = font.render(str(score[1][0]) , 1, (0,0,0))
            
            win.blit(p11, (0.45*window_width + step, window_height/4))
            win.blit(p21, (0.45*window_width + step, window_height/2))
    
    #Mostra placar do segundo game
    if game2 == 1:
    
        cursor1 = font.render(str(score[0][gcurrent]) , 1, (255,165,0))
        cursor2 = font.render(str(score[1][gcurrent]) , 1, (0,255,0))

        
        if gcurrent == 1:
            if saque == 1: #Foco no placar1
                pygame.draw.rect(win, (255,165,0), (0.6*window_width + step - x, window_height/4 - y, width, height))
                cursor1 = font.render(str(score[0][1]) , 1, (0,0,0)) # Arguments are: text, anti-aliasing, color
                cursor2 = font.render(str(score[1][1]) , 1, (0,255,0))
        
            if saque == 2: #Foco no placar2
                pygame.draw.rect(win, (0,255,0), (0.6*window_width + step - x, window_height/2 - y, width, height))
                cursor2 = font.render(str(score[1][1]) , 1, (0,0,0))
    
            win.blit(cursor1, (0.6*window_width + step, window_height/4))
            win.blit(cursor2, (0.6*window_width + step, window_height/2))
        else:
            if score[0][1]>score[1][1]: #Jogador1 venceu o game
                pygame.draw.rect(win, (255,165,0), (0.6*window_width + step - x, window_height/4 - y, width, height))
                p12 = font.render(str(score[0][1]) , 1, (0,0,0))
                p22 = font.render(str(score[1][1]) , 1, (0,255,0))
            else:
                pygame.draw.rect(win, (0,255,0), (0.6*window_width + step - x, window_height/2 - y, width, height))
                p12 = font.render(str(score[0][1]) , 1, (255,165,0))
                p22 = font.render(str(score[1][1]) , 1, (0,0,0))
            
            win.blit(p12, (0.6*window_width + step, window_height/4))
            win.blit(p22, (0.6*window_width + step, window_height/2))
            
    #Mostra placar do terceiro game     
    if game3 == 1:
    
        cursor1 = font.render(str(score[0][gcurrent]) , 1, (255,165,0))
        cursor2 = font.render(str(score[1][gcurrent]) , 1, (0,255,0))

        
        if gcurrent == 2:
            if saque == 1: #Foco no placar1
                pygame.draw.rect(win, (255,165,0), (0.75*window_width + step - x, window_height/4 - y, width, height))
                cursor1 = font.render(str(score[0][2]) , 1, (0,0,0))
                cursor2 = font.render(str(score[1][2]) , 1, (0,255,0))
        
            if saque == 2: #Foco no placar2
                pygame.draw.rect(win, (0,255,0), (0.75*window_width + step - x, window_height/2 - y, width, height))
                cursor2 = font.render(str(score[1][2]) , 1, (0,0,0))
    
            win.blit(cursor1, (0.75*window_width + step, window_height/4))
            win.blit(cursor2, (0.75*window_width + step, window_height/2))
        else:
            if score[0][2]>score[1][2]: #Jogador1 venceu o game
                pygame.draw.rect(win, (255,165,0), (0.75*window_width + step - x, window_height/4 - y, width, height))
                p13 = font.render(str(score[0][2]) , 1, (0,0,0))
                p23 = font.render(str(score[1][2]) , 1, (0,255,0))
            else:
                pygame.draw.rect(win, (0,255,0), (0.75*window_width + step - x, window_height/2 - y, width, height))
                p13 = font.render(str(score[0][2]) , 1, (255,165,0))
                p23 = font.render(str(score[1][2]) , 1, (0,0,0))
            
            win.blit(p13, (0.75*window_width + step, window_height/4))
            win.blit(p23, (0.75*window_width + step, window_height/2))
        
    pygame.display.update() 
    
pygame.quit()
