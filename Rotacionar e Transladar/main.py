# Gabriel Maia Alves Araújo - 2022005689
# Caio Teodoro Portela - 2020004501
# CMCO05 - INTRODUÇÃO À COMPUTAÇÃO VISUAL - Questão 1 da P1

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (-4, 0),
    (-1, 1),
    (0, 4),
    (1, 1),
    (4, 0),
    (1, -1),
    (0, -4),
    (-1, -1)
    )

arestas = (
    (0,1),
    (1,2),
    (2,3),
    (3,4),
    (4,5),
    (5,6),
    (6,7),
    (7,0)
    )

def Forma():
    glBegin(GL_LINES)
    for aresta in arestas:
        for vertice in aresta:
            glColor3f(1.0, 0.0, 0.0)
            glVertex2iv(vertices[vertice])
    glEnd()

def Grid():
    glBegin(GL_LINES)
    glColor3f(0.5, 0.5, 0.5)
    for i in range(-10, 11):
        glVertex2f(i, -10)
        glVertex2f(i, 10)
        glVertex2f(-10, i)
        glVertex2f(10, i)
    glEnd()

def Cor():
    glBegin(GL_LINES)
    glColor3f(0, 0, 1)
    glVertex2f(0, -10)
    glVertex2f(0, 10)
    glVertex2f(-10, 0)
    glVertex2f(10, 0)
    glEnd()

def Ponto(x, y, angulo):
    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluOrtho2D(-10, 10, -10, 10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 

        Grid()
        Cor()
        glPushMatrix()
        glTranslatef(x, y, 0)
        glRotatef(angulo, 0, 0, 1)
        Forma()
        glPopMatrix()
        
        pygame.display.flip()
        pygame.time.wait(10)

print('Deseja rotacionar e transladar o cubo [Y/N]? ')
condicao = input()

if condicao == 'N' or condicao == 'n':
    x = 0
    y = 0
    angulo = 0
    Ponto(x, y, angulo)

if condicao == 'Y' or condicao == 'y':
    x = 5
    y = 5
    angulo = 45
    Ponto(x, y, angulo)