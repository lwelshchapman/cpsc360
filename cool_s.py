from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                                                  # glut window number
width, height = 500, 500                                                    # window size

########################################### The Cool S ####################################################
def cool_s():
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(100, 100, 0.0)
    glVertex3f(100, 150, 0.0)
    glVertex3f(50, 175, 0.0)
    glVertex3f(50, 225, 0.0)
    glVertex3f(100, 275, 0.0)
    glVertex3f(150, 225, 0.0)
    glVertex3f(150, 175, 0.0)
    glVertex3f(125, 162.5, 0.0)
    glEnd()

    glBegin(GL_LINE_STRIP)
    glVertex3f(100, 225, 0.0)
    glVertex3f(100, 175, 0.0)
    glVertex3f(150, 150, 0.0)
    glVertex3f(150, 100, 0.0)
    glVertex3f(100, 50, 0.0)
    glVertex3f(50, 100, 0.0)
    glVertex3f(50, 150, 0.0)
    glVertex3f(75, 162.5, 0.0)
    glEnd()


########################################### OpenGL Program ####################################################
def refresh(width, height):
    glViewport(0, 0, width, height)                                         # specify viewport parameters
    glMatrixMode(GL_PROJECTION)                                             # set mode to projection transformation
    glLoadIdentity()                                                        # reset transf matrix to an identity
    glOrtho(0, 500, 0, 500, 0.0, 1.0)                                       # specify orthogonal projection view volume
    glMatrixMode(GL_MODELVIEW)                                              # set mode to modelview (geometric+view transf)
    glLoadIdentity()                                                        # reset transf matrix to an identity
    
def draw():                                                                 # This is the drawing function defined by you and called all the time
    glClearColor(1.0, 1.0, 0.0, 1.0)                                        # set background RGBA color 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                      # clear display mode of display-window
    glLoadIdentity()                                                        # load an identity matrix
    refresh(width, height)                                                  # reset viweing and projection transforms for every iteration

    cool_s()

    glutSwapBuffers()                                                       # import for double-buffering

def main():
    glutInit()                                                              # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)  # set display mode of display-window
    glutInitWindowPosition(0, 0)                                            # set top-left display-window position
    glutInitWindowSize(width, height)                                       # set display-window size
    window = glutCreateWindow("cpsc 360")                                   # create window with title
    glutDisplayFunc(draw)                                                   # display graphic content and wait
    glutMainLoop()                                                          # must be called at last; display graphics and put program into infinite loop

main()