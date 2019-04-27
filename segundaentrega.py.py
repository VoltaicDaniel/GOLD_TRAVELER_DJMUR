# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 19:07:57 2019

@author: Daniel
"""

import pygame
import random




def main():
    pygame.init()
    main_surf = pygame.display.set_mode((500, 560), 0, 32)#crea la pantalla
    pygame.display.set_caption("Gold Traveler")#le da nombre al juego


    posx = 210#posicion jugador en x
    posy = 480#posicion jugador en y
    player = (posx,posy,80,80)#crea el jugador
    colorplayer = (200,10,30)#color de jugador
    colorenemy=(0,0,0)
    colorenemy2=(0,255,0)
    colorenemy3=(0,0,255)
    a1= random.randint(25,50)#da ancho del jugador
    a2= random.randint(25,50)
    #a3=  random.randint(25,50)
    l1= random.randint(25,50)#da largo de jugador
    l2= random.randint(25,50)
    #l3= random.randint(25,50)
    x1 = 111 #x1,x2,x3 son los carriles
    x2 = 210
    x3= 310
    xsuper = [x1,x2,x3]
    x4 = random.choice(xsuper) #el enemigo sale en un carril aleatorio
    x5= random.choice(xsuper)
    #x6= random.choice(xsuper)
    y1= 0
    enemigo = (x4,y1,a1,l1)
    enemigo2 =(x5,y1,a2,l2)
   # enemigo3 =(x6,y1,a3,l3)
    pygame.time.set_timer(pygame.USEREVENT + 1, 560)#se usa despues para el movimiento del enemigo
    carretera = pygame.image.load("carretera.png").convert_alpha()#carretera es el fondo
    carretera = pygame.transform.scale(carretera, (500,560))
    gameover = pygame.image.load("game over.png").convert_alpha()
    gameover = pygame.transform.scale(gameover, (500,500))

    
    while True:
        
        ev = pygame.event.poll()

        if ev.type == pygame.QUIT:#crea la ocasion si el jugador se quiere salir
            break

        if ev.type == pygame.KEYDOWN:#que pasa cuando se oprime una tecla
            key = ev.dict["key"]
            #print(key)#try
            if key == 276:#define la tecla 276 izquierda
                posx -= 100
                while posx <=110:#se crean limites
                    posx+=1

            elif key == 275:#define la tecla 275 derecha
                posx += 100
                while posx>310:#se crean limites
                    posx-=1
            elif key == 273:#defina la tecla 273
                posy -= 50
                posx += 15
        elif ev.type == pygame.KEYUP:#que pasa cuando se levanta la tecla
            key = ev.dict["key"]
            if key == 273:#define la tecla 273
                posx-= 15
                posy+=50
        elif ev.type == pygame.USEREVENT + 1:#movimiento del enemigo


            y1+= 80
            enemigo= (x4,y1,a1,l1)
            enemigo2 = (x5,y1,a2,l2)
          #  enemigo3 = (x6,y1,a3,l3)
            #print(enemigo)#try
            player = (posx,posy,80,80)
            main_surf.blit(carretera,(0,0))
            main_surf.fill(colorenemy,enemigo)
            main_surf.fill(colorenemy2,enemigo2)
         #   main_surf.fill(colorenemy3,enemigo3)
            main_surf.fill(colorplayer,player)
            pygame.display.flip()


        player = (posx,posy,80,80)

        main_surf.blit(carretera,(0,0))
        
        main_surf.fill(colorenemy,enemigo)
        main_surf.fill(colorenemy2,enemigo2)
        #main_surf.fill(colorenemy3,enemigo3)
        main_surf.fill(colorplayer,player)
        if enemigo[0] == player[0]:
            if enemigo[1] == player[1]: 
                
                main_surf.fill((0,0,0))
                main_surf.blit(gameover,(0,0))
                del enemigo
        if enemigo2[0] == player[0]:
            if enemigo2[1] == player[1]: 
                
                main_surf.fill((0,0,0))
                main_surf.blit(gameover,(0,0))
                del enemigo2
#        if enemigo3[0] == player[0]:
#            if enemigo3[1] == player[1]: 
#                
#                main_surf.fill((0,0,0))
#                main_surf.blit(gameover,(0,0))
#                del enemigo3


        pygame.display.flip()

    pygame.quit()

main()#ejecucion