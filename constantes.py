import pygame

FPS = 60
ANCHO_VENTANA = 1000
ALTO_VENTANA = 1000
CASILLA_TAMANO = 50
COLOR_BLANCO = (255,255,255)
COLOR_VERDE = (0,255,0)
COLOR_NARANJA = (230, 97, 29)
COLOR_ROJO = (255,0,0)
COLOR_GRIS = (128,128,128)
COLOR_AMARILLO = (255,255,0)
COLOR_CELESTE = (0,0,255)
COLOR_AZUL = (0,0,128)
TAMANO_FUENTE_ENCABEZADO = 60
TAMANO_FUENTE = 40
TEXTO_IZQUIERDO = 230
TEXTO_SUPERIOR = 100

COORDENADAS_MUNDO_1 = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 0, 0, 7, 7, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 2, 2, 0, 0, 1], 
[1, 0, 0, 0, 7, 7, 7, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 2, 7, 7, 7, 7, 0, 0, 7, 0, 0, 0, 0, 0, 7, 0, 0, 0, 1], 
[1, 0, 1, 2, 2, 2, 2, 0, 0, 7, 0, 0, 3, 0, 0, 7, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 2, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 2, 2, 0, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 2, 1, 1, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
[1, 8, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

COORDENADAS_MUNDO_2 = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 7, 0, 0, 0, 0, 7, 0, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 7, 0, 2, 0, 0, 7, 0, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1], 
[1, 7, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 7, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 7, 0, 0, 0, 1], 
[1, 0, 2, 7, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 0, 7, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 2, 0, 0, 7, 0, 0, 3, 0, 0, 7, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 2, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 8, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

COORDENADAS_MUNDO_3 = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 7, 0, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 1], 
[1, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 7, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1], 
[1, 0, 7, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 0, 1], 
[1, 0, 2, 7, 0, 0, 7, 0, 7, 0, 7, 0, 0, 0, 7, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 2, 0, 2, 0, 7, 0, 3, 0, 7, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 7, 0, 7, 0, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 1], 
[1, 8, 0, 0, 2, 2, 2, 2, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1], 
[1, 2, 0, 0, 0, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
