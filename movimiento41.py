import pygame
import random



def main():
    pygame.init()
    main_surf = pygame.display.set_mode((500, 500), 0, 32)#crea la pantalla
    pygame.display.set_caption("Gold Traveler")#le da nombre al juego


    posx = 210#posicion jugador en x
    posy = 420#posicion jugador en y
    player = (posx,posy,80,80)#crea el jugador
    colorplayer = (200,10,30)#color de jugador
    a= random.randint(25,50)#da ancho del jugador
    l= random.randint(25,50)#da largo de jugador
    x1 = 130 #x1,x2,x3 son los carriles
    x2 = 230
    x3= 340
    xsuper = [x1,x2,x3]
    x4 = random.choice(xsuper) #el enemigo sale en un carril aleatorio
    y1= 0
    enemigo = (x4,y1,a,l)
    pygame.time.set_timer(pygame.USEREVENT + 1, 500)#se usa despues para el movimiento del enemigo
    carretera = pygame.image.load("carretera.png").convert_alpha()#carretera es el fondo
    carretera = pygame.transform.scale(carretera, (500,500))
    gameover = pygame.image.load("game over.png").convert_alpha()
    gameover = pygame.transform.scale(gameover, (500,500))
    
    #enemigo2 = (x4,y1,a,l)

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


            y1+= l
            enemigo= (x4,y1,a,l)
            #enemigo2= (x4+100,y1,a,l)
            #print(enemigo)#try
            player = (posx,posy,90,90)
            main_surf.blit(carretera,(0,0))
            main_surf.fill(colorplayer,enemigo)
            #main_surf.fill(colorplayer,enemigo2)
            main_surf.fill(colorplayer,player)
            
            #







            pygame.display.flip()


        player = (posx,posy,90,90)

        main_surf.blit(carretera,(0,0))
        main_surf.fill(colorplayer,enemigo)
        #main_surf.fill(colorplayer,enemigo2)
        main_surf.fill(colorplayer,player)
        #main_surf.blit(carretera,(0,0))
        if enemigo[0] >= player[0]: 
            if enemigo[1] >= player[1]:
                main_surf.fill((0,0,0))
                main_surf.blit(gameover,(0,0))
                

                
                #del enemigo2
        
                
                #print("hola")#try
                
                
        enemigo = (x4,y1,a,l)
        main_surf.fill(colorplayer,player)

        pygame.display.flip()



    pygame.quit()

main()#ejecucion