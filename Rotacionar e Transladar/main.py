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

def PontoInicial():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluOrtho2D(-10, 10, -10, 10)
    
    glTranslatef(0.0, 0.0, 0)
    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        Grid()
        Forma()

        pygame.display.flip()
        pygame.time.wait(10)

def PontoMudado(x, y, angulo):
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluOrtho2D(-10, 10, -10, 10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)     

        Grid()
        
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
    PontoInicial()

if condicao == 'Y' or condicao == 'y':
    print('Qual a coordenada do ponto x? ')
    x = int(input())
    print('Qual a coordenada do ponto y? ')
    y = int(input())
    print('Qual o ângulo de rotação? ')
    angulo = int(input())
    PontoMudado(x, y, angulo)