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

def main():
    angulo = 0
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(1.0, 1.0, -10)

    while True:
        # if condicao == 'Y':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(angulo, 0, 0, 1)
        angulo += 0.2
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Forma()
        pygame.display.flip()
        pygame.time.wait(10)

            # print('Deseja voltar para a posição inicial [Y/N]? ')
            # condicao = input()
            # if condicao == 'N':
            #     pygame.quit()
            #     quit()


main()