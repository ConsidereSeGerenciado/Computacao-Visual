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

# print('Deseja rotacionar o cubo [Y/N]? ')
# condicao = input()

def Forma():
    glBegin(GL_LINES)
    for aresta in arestas:
        for vertice in aresta:
            glVertex2iv(vertices[vertice])
    glEnd()

def PontoInicial():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -25)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Forma()
        pygame.display.flip()
        pygame.time.wait(10)

def PontoMudado(x, y, angulo):
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glTranslatef(x, y, -25)
        glRotatef(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Forma()
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