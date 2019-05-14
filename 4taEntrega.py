# -*- coding: utf-8 -*-
"""
Created on Fri May  3 18:53:20 2019

@author: Daniel
"""
import base64
import gzip
import sys
import pygame
#import random
from pygame.locals import *
import json
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
""" variables globales"""
ancho = 900
alto = 450

class jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenCarro = pygame.image.load("sprites_gold.png")
        self.imagenCarro.set_clip(pygame.Rect(99,26,90,140))
        self.image = self.imagenCarro.subsurface(self.imagenCarro.get_clip())
        self.inv_imagencarro = pygame.transform.flip(self.imagenCarro,True,False)
        self.inv_imagencarro.set_clip(pygame.Rect(50,26,90,70))
        self.Rimage = self.inv_imagencarro.subsurface(self.inv_imagencarro.get_clip())



        self.rect = self.image.get_rect()
        self.rect.centerx = ancho-830
        self.rect.centery = alto-65

        self.vida = True
        self.velocidad = 50

        self.frame = 0
        """ animacion """
        self.right_states = {0: (41,26,90,134),1:(200,26,80,140),2:(140,26,70,138)}
        self.Rright_states = {0: (41,26,90,134),1:(500,26,200,140),2:(140,26,70,138)}

        self.direct = True
        self.salto = True
        self.salto_par = True
        self.contadorfun = 0



        """ mover a la derecha """


    def movimientoDerecha(self):
        """ que se pueda mover a la derecha en el eje x """

        self.rect.right += self.velocidad
        self.movimiento()


    def movimientoIzquierda(self):
        """ que se pueda mover a la izquierda """
        self.rect.left -= self.velocidad
        self.movimiento()


    def movimiento(self):
        if self.vida == True:
            """ crear hasta donde se puede mover"""
            if self.rect.left <= 10 :
                self.rect.left = 11



    """ animacion"""

    def get_frame(self,frame_set):
        self.frame += 1
        if self.frame > (len(frame_set)-1):
            self.frame = 0

        return frame_set[self.frame]

    def clip(self,clipped_rect):
        if type(clipped_rect) is dict:
            self.imagenCarro.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.imagenCarro.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def Rclip (self, Rclipped_rect):
        if type (Rclipped_rect) is dict:
            self.inv_imagencarro.set_clip(pygame.Rect(self.get_frame(Rclipped_rect)))
        else:
            self.inv_imagencarro.set_clip(pygame.Rect(Rclipped_rect))
        return Rclipped_rect

    def update(self,direction):
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.centerx += 5

        elif direction == "left":
            self.Rclip(self.Rright_states)
            self.rect.centerx -= 5


        self.Rimage = self.inv_imagencarro.subsurface(self.inv_imagencarro.get_clip())
        self.image = self.imagenCarro.subsurface(self.imagenCarro.get_clip())

    def dibujar(self,superficie):
        superficie.blit(self.image,self.rect)
    def rdibujar(self,superficie):
        superficie.blit(self.Rimage,self.rect)




class Enemigos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenEnemigo = pygame.image.load("veneno.png")
        self.imagenEnemigo = pygame.transform.scale(self.imagenEnemigo,(50,50))


        """ atributos del enemigo"""
        self.imagenPos = 0 # la posicion por defecto que se va a ir graduando manualmente

        self.rect = self.imagenEnemigo.get_rect()


        self.velocidad = 1 # velocidad con la que va a bajar
        #self.MaxVel = self.rect.top + 40
        """ define donde va a empezar el enemigo"""

        self.rect.centerx = ancho-670
        self.rect.centery = alto-47
        
        self.derecha = True
        self.rect.left = self.rect.centerx
        self.vidaEnemigo = True
        
        
    
    def moverse(self):
        if self.vidaEnemigo == True:
            
            if self.derecha == True:
                self.rect.left -= self.velocidad
                if self.rect.left <  10:
                    self.derecha = False
        
            else:
                self.rect.left += self.velocidad
                if self.rect.left > ancho-680:
                    self.derecha =True
            









    def dibujar(self,superficie):

        superficie.blit(self.imagenEnemigo,self.rect)

class mundo:
    def __init__(self):
        self.tilewidth = 0
        self.widthmapa = 0
        self.heightmapa = 0
        self.tileheight = 0

    def cargarMapa(self, nivel):
        self.matrizMapa = []
        self.salida = []
        self.abrir = (open("map/"+ nivel +".json","r"))
        self.data = json.load(self.abrir)
        self.abrir.close()
        self.tilewidth = self.data["tilewidth"]
        self.tileheight =  self.data["tileheight"]
        self.heightmapa = self.data["height"]
        self.widthmapa = self.data["width"]
        for item in self.data["layers"]:
            self.mapa = item["data"]
        #print(self.mapa)

        self.mapa = base64.decodestring(self.mapa.encode())
        #print(self.mapa)
        self.cadena = gzip.zlib.decompress(self.mapa)
        #print(self.cadena)
        #int.from_bytes
        for idx in range(0, len(self.cadena), 4):
            #print(self.cadena[idx])
#            self.val = ord((str(self.cadena[idx]))) | (ord(str(self.cadena[idx + 1])) << 8) | \
#            (ord(str(self.cadena[idx + 2])) << 16) | (ord(str(self.cadena[idx + 3])) << 24)
            self.salida.append(self.cadena[idx])

        #print(self.salida)


        for a1 in range (0, len(self.salida),self.widthmapa):
            self.matrizMapa.append(self.salida[a1:a1 + self.widthmapa])

        for k in range(self.heightmapa):
            #print (self.matrizMapa[k])

            return

    def array_tileset(self,img):
        self.x = 0
        self.y = 0
        self.hojatiles = []
        for i in range (29):
            for h in range (27):
                self.imagen = self.cortar(mundo, img, (self.x,self.y,16,16))
                self.hojatiles.append(self.imagen)
                self.x+= 18
            self.x = 0
            self.y += 18
        return self.hojatiles

    def cortar(self, img, rectangulo):
        self.rect = pygame.Rect(rectangulo)
        self.image = pygame.Surface(self.rect.size).convert()
        self.image.blit(img, (0,0), self.rect)
        return self.image




def goldTraver():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Gold Traver")
    #imagenFondo = pygame.image.load("desierto.png").convert_alpha()
    """ me permite configurar la imagen el ancho y el alto de la imagen"""
    #imagenFondo = pygame.transform.scale(imagenFondo, (900, 500))



    """ creacion del jugador"""
    player = jugador()

    enJuego = True

    """ creacion del enemigo"""
    enemigo = Enemigos()



    while True:
        #global matrizMapa
        img = pygame.image.load("conejo_tileset.png")

        imagenEnemigo = pygame.image.load("veneno.png")

        mundo.cargarMapa(mundo,"primerMapa")
        hoja = mundo.array_tileset(mundo, img)
        
        for m in range(mundo.heightmapa):
            for l in range(mundo.widthmapa):
                minum = mundo.matrizMapa[m][l]
                tileimg = hoja[minum - 1]
                tileimg = pygame.transform.scale(tileimg,(mundo.tilewidth*2, mundo.tileheight*2))
                ventana.blit(tileimg,(l*mundo.tilewidth*2,m*mundo.tileheight*2 + 10))
                
       # pygame.display.update()
        
        enemigo.moverse()

        """ si el jugador da a la x de la venta se cierra la pantalla"""

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            """ crear eventos cuando se oprime una telca"""

            if enJuego == True:# se usa para saber si el jugador no ha perdido


                """ hacer mover al enemigo mientras que el jugador no alla perdido"""
                


                if evento.type == pygame.KEYDOWN:
                    key = evento.dict["key"]
                    print(key)

                    if evento.key == 276:#izquierda
                        player.movimientoIzquierda()
                        player.update("left")

                        player.direct = False


                    if evento.key == 275:#derecha
                        player.movimientoDerecha()
                        player.update('right')

                        player.direct = True
                    if evento.key == 273:
                        player.salto = True
                        if player.contadorfun == 0:
                            player.rect.y -= 80
                            player.contadorfun += 1

                if evento.type ==pygame.KEYUP:
                    if evento.key == 273:
                        player.contadorfun -= 1
                        player.rect.y += 80
                    
        """creando las colisiones """         
        if player.rect.colliderect(enemigo.rect):
            enemigo.vidaEnemigo = False
            enJuego = False
            print(enemigo.rect,player.rect)
        
















        #ventana.blit(imagenFondo,(0,0))
        """ pinta el jugador en la ventana y la dibuja """
        if player.direct == True:
            player.dibujar(ventana)
        elif player.direct == False:
            player.rdibujar(ventana)

        enemigo.dibujar(ventana)
        
            
















        pygame.display.update()

goldTraver()
