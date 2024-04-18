import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (-4, 0, 0),
    (-1, 1, 0),
    (0, 4, 0),
    (1, 1, 0),
    (4, 0, 0),
    (1, -1, 0),
    (0, -4, 0),
    (-1, -1, 0)
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

def Cubo():
    glBegin(GL_LINES)
    for aresta in arestas:
        for vertice in aresta:
            glVertex3fv(vertices[vertice])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(1.0,1.0, -10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cubo()
        pygame.display.flip()
        pygame.time.wait(10)


main()