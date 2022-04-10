# Logan Welsh
# lwelsh@chapman.edu
# CPSC-360-01 Assignment 13.A
# assignment13a.py

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                                                  # glut window number
width, height = 500, 500                                                    # window size

########################################### OpenGL Program ####################################################
def refresh(width, height):
    glViewport(0, 0, width, height)                                         # specify viewport parameters
    glMatrixMode(GL_PROJECTION)                                             # set mode to projection transformation
    glLoadIdentity()                                                        # reset transf matrix to an identity
    glOrtho(0, 500, 0, 500, 0.0, 1.0)                                       # specify orthogonal projection view volume
    glMatrixMode(GL_MODELVIEW)                                              # set mode to modelview (geometric+view transf)
    glLoadIdentity()                                                        # reset transf matrix to an identity

def question1():
    # Draw line strip
    glColor3f(0.0, 0.0, 1.0)
    glLineWidth(7.5)
    glBegin(GL_LINE_STRIP)
    glVertex3f(50.0, 50.0, 0.0)
    glVertex3f(150.0, 350.0, 0.0)
    glVertex3f(250.0, 50.0, 0.0)
    glVertex3f(350.0, 350.0, 0.0)
    glVertex3f(450.0, 50.0, 0.0)
    glEnd()

    # Draw points
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(15.0)
    glBegin(GL_POINTS)
    glVertex3f(50.0, 50.0, 0.0)
    glVertex3f(150.0, 350.0, 0.0)
    glVertex3f(250.0, 50.0, 0.0)
    glVertex3f(350.0, 350.0, 0.0)
    glVertex3f(450.0, 50.0, 0.0)
    glEnd()

    print("assignment 13.A-1")

def question2():
    # Draw line strip
    glColor3f(0.0, 0.0, 1.0)
    glLineWidth(7.5)
    glBegin(GL_LINES)
    glVertex3f(50.0, 50.0, 0.0)
    glVertex3f(150.0, 350.0, 0.0)
    glVertex3f(150.0, 350.0, 0.0)
    glVertex3f(250.0, 50.0, 0.0)
    glVertex3f(250.0, 50.0, 0.0)
    glVertex3f(350.0, 350.0, 0.0)
    glVertex3f(350.0, 350.0, 0.0)
    glVertex3f(450.0, 50.0, 0.0)
    glEnd()

    # Draw points
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(15.0)
    glBegin(GL_POINTS)
    glVertex3f(50.0, 50.0, 0.0)
    glVertex3f(150.0, 350.0, 0.0)
    glVertex3f(250.0, 50.0, 0.0)
    glVertex3f(350.0, 350.0, 0.0)
    glVertex3f(450.0, 50.0, 0.0)
    glEnd()

    print("assignment 13.A-2")
    
def draw():                                                                 # This is the drawing function defined by you and called all the time
    glClearColor(1.0, 1.0, 0.0, 1.0)                                        # set background RGBA color 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                      # clear display mode of display-window
    glLoadIdentity()                                                        # load an identity matrix
    refresh(width, height)                                                  # reset viweing and projection transforms for every iteration

    # To show the result for one quesiton at a time, 
    #    comment out the function of the other question

    # assignment 13.A-1
    # TODO write your code in the function below
    question1()

    # assignment 13.A-2
    # TODO write your code in the function below
    #question2()

    glutSwapBuffers()                                                       # import for double-buffering

def main():
    glutInit()                                                              # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)  # set display mode of display-window
    glutInitWindowPosition(0, 0)                                            # set top-left display-window position
    glutInitWindowSize(width, height)                                       # set display-window size
    window = glutCreateWindow("cpsc360:A13.A - Logan Welsh")        # create window with title
    glutDisplayFunc(draw)                                                   # display graphic content and wait
    glutMainLoop()                                                          # must be called at last; display graphics and put program into infinite loop

main()