#Comandos para librerías
#pip install pyopengl
#pip install glfw

#Importar librerias

from cmath import cos, pi, sin
import dis
from OpenGL.GL import *
from glew_wish import *
import glfw
import math

#unidades por segundo
velocidad = 0.5
posicion_nave = [0.0,-0.8,0.0]
window = None
angulo_nave = 0.0
velocidad_rotacion_nave = 90.0
fase = 90.0

posicion_limite1 = [0.0, 0.0, 0.0]

##Bala
posiciones_bala = [
               [0.0,0.0,0.0],
               [0.0,0.0,0.0],
               [0.0,0.0,0.0]
                ]
disparando = [False,False,False]
angulo_bala = [0.0, 0.0, 0.0]
velocidad_bala= 1.75

##Enemigos
posiciones_enemigos = [
    [-0.4, 0.75, 0.0], 
    [0.0, 0.75, 0.0], 
    [0.4, 0.75, 0.0]
    ]
velocidades_enemigos = [0.1,0.1,0.1]
#direcciones 0 abajo 1 arriba
direcciones_enemigos = [0,0,0]
activos_enemigos = [1,0,0]

posiciones_enemigos2 = [
    [-0.4, 0.55, 0.0], 
    [0.0, 0.55, 0.0], 
    [0.4, 0.55, 0.0]
    ]
velocidades_enemigos2 = [0.1,0.1,0.1]
direcciones_enemigos2 = [0,0,0]
activos_enemigos2 = [1,0,0]

posiciones_enemigos3 = [
    [-0.4, 0.35, 0.0], 
    [0.0, 0.35, 0.0], 
    [0.4, 0.35, 0.0]
    ]
velocidades_enemigos3 = [0.1,0.1,0.1]
direcciones_enemigos3 = [0,0,0]
activos_enemigos3 = [1,0,0]

posiciones_enemigos4 = [
    [-0.4, 0.15, 0.0], 
    [0.0, 0.15, 0.0], 
    [0.4, 0.15, 0.0]
    ]
velocidades_enemigos4 = [0.1,0.1,0.1]
direcciones_enemigos4 = [0,0,0]
activos_enemigos4 = [1,0,0]

posiciones_enemigos5 = [
    [-0.4, -0.05, 0.0], 
    [0.0, -0.05, 0.0], 
    [0.4, -0.05, 0.0]
    ]
velocidades_enemigos5 = [0.1,0.1,0.1]
direcciones_enemigos5 = [0,0,0]
activos_enemigos5 = [1,0,0]

vivos_enemigos = [True, True, True]


contador_tiempo = 0.0
tiempo_anterior = 0.0

def actualizar_enemigos(tiempo_delta):
    global contador_tiempo

    if glfw.get_time() > 3.0:
        activos_enemigos[2] = 1
    if glfw.get_time() > 7.0:
        activos_enemigos[1] = 1

    contador_tiempo = contador_tiempo + tiempo_delta
    if contador_tiempo >= 1.0:
        contador_tiempo = contador_tiempo - 1.0
        for i in range(3):
            velocidades_enemigos[i] = velocidades_enemigos[i] + 0.01
    for i in range(3):
        if activos_enemigos[i]:
            cantidad_movimiento = velocidades_enemigos[i] * tiempo_delta
            if direcciones_enemigos[i] == 0:
                posiciones_enemigos[i][0] = posiciones_enemigos[i][0] - cantidad_movimiento
                if posiciones_enemigos[i][0] <= -0.75:
                    direcciones_enemigos[i] = 1
            else:
                posiciones_enemigos[i][0] = posiciones_enemigos[i][0] + cantidad_movimiento
                posiciones_enemigos[i][1] = posiciones_enemigos[i][1] - (cantidad_movimiento/20)
                if posiciones_enemigos[i][0] >= 0.75:
                    direcciones_enemigos[i] = 0

def actualizar_enemigos2(tiempo_delta):
    global contador_tiempo

    if glfw.get_time() > 3.0:
        activos_enemigos2[2] = 1
    if glfw.get_time() > 7.0:
        activos_enemigos2[1] = 1

    contador_tiempo = contador_tiempo + tiempo_delta
    if contador_tiempo >= 1.0:
        contador_tiempo = contador_tiempo - 1.0
        for i in range(3):
            velocidades_enemigos2[i] = velocidades_enemigos2[i] + 0.011
    for i in range(3):
        if activos_enemigos2[i]:
            cantidad_movimiento = velocidades_enemigos2[i] * tiempo_delta
            if direcciones_enemigos2[i] == 0:
                posiciones_enemigos2[i][0] = posiciones_enemigos2[i][0] - cantidad_movimiento
                if posiciones_enemigos2[i][0] <= -0.75:
                    direcciones_enemigos2[i] = 1
            else:
                posiciones_enemigos2[i][0] = posiciones_enemigos2[i][0] + cantidad_movimiento
                posiciones_enemigos2[i][1] = posiciones_enemigos2[i][1] - (cantidad_movimiento/20)
                if posiciones_enemigos2[i][0] >= 0.75:
                    direcciones_enemigos2[i] = 0

def actualizar_enemigos3(tiempo_delta):
    global contador_tiempo

    if glfw.get_time() > 3.0:
        activos_enemigos3[2] = 1
    if glfw.get_time() > 7.0:
        activos_enemigos3[1] = 1

    contador_tiempo = contador_tiempo + tiempo_delta
    if contador_tiempo >= 1.0:
        contador_tiempo = contador_tiempo - 1.0
        for i in range(3):
            velocidades_enemigos3[i] = velocidades_enemigos3[i] + 0.011
    for i in range(3):
        if activos_enemigos3[i]:
            cantidad_movimiento = velocidades_enemigos3[i] * tiempo_delta
            if direcciones_enemigos3[i] == 0:
                posiciones_enemigos3[i][0] = posiciones_enemigos3[i][0] - cantidad_movimiento
                if posiciones_enemigos3[i][0] <= -0.75:
                    direcciones_enemigos3[i] = 1
            else:
                posiciones_enemigos3[i][0] = posiciones_enemigos3[i][0] + cantidad_movimiento
                posiciones_enemigos3[i][1] = posiciones_enemigos3[i][1] - (cantidad_movimiento/20)
                if posiciones_enemigos3[i][0] >= 0.75:
                    direcciones_enemigos3[i] = 0
                
def actualizar_enemigos4(tiempo_delta):
    global contador_tiempo

    if glfw.get_time() > 3.0:
        activos_enemigos4[2] = 1
    if glfw.get_time() > 7.0:
        activos_enemigos4[1] = 1

    contador_tiempo = contador_tiempo + tiempo_delta
    if contador_tiempo >= 1.0:
        contador_tiempo = contador_tiempo - 1.0
        for i in range(3):
            velocidades_enemigos4[i] = velocidades_enemigos4[i] + 0.011
    for i in range(3):
        if activos_enemigos4[i]:
            cantidad_movimiento = velocidades_enemigos4[i] * tiempo_delta
            if direcciones_enemigos4[i] == 0:
                posiciones_enemigos4[i][0] = posiciones_enemigos4[i][0] - cantidad_movimiento
                if posiciones_enemigos4[i][0] <= -0.75:
                    direcciones_enemigos4[i] = 1
            else:
                posiciones_enemigos4[i][0] = posiciones_enemigos4[i][0] + cantidad_movimiento
                posiciones_enemigos4[i][1] = posiciones_enemigos4[i][1] - (cantidad_movimiento/20)
                if posiciones_enemigos4[i][0] >= 0.75:
                    direcciones_enemigos4[i] = 0
            
def actualizar_enemigos5(tiempo_delta):
    global contador_tiempo

    if glfw.get_time() > 3.0:
        activos_enemigos5[2] = 1
    if glfw.get_time() > 7.0:
        activos_enemigos5[1] = 1

    contador_tiempo = contador_tiempo + tiempo_delta
    if contador_tiempo >= 1.0:
        contador_tiempo = contador_tiempo - 1.0
        for i in range(3):
            velocidades_enemigos5[i] = velocidades_enemigos5[i] + 0.011
    for i in range(3):
        if activos_enemigos5[i]:
            cantidad_movimiento = velocidades_enemigos5[i] * tiempo_delta
            if direcciones_enemigos5[i] == 0:
                posiciones_enemigos5[i][0] = posiciones_enemigos5[i][0] - cantidad_movimiento
                if posiciones_enemigos5[i][0] <= -0.75:
                    direcciones_enemigos5[i] = 1
            else:
                posiciones_enemigos5[i][0] = posiciones_enemigos5[i][0] + cantidad_movimiento
                posiciones_enemigos5[i][1] = posiciones_enemigos5[i][1] - (cantidad_movimiento/20)
                if posiciones_enemigos5[i][0] >= 0.75:
                    direcciones_enemigos5[i] = 0

def actualizar_bala(tiempo_delta):
    global disparando
    for i in range(3):
        if disparando[i]:
            cantidad_movimiento = velocidad_bala* tiempo_delta
            posiciones_bala[i][0] = posiciones_bala[i][0] + (
                math.cos(angulo_bala[i] * pi / 180.0) * cantidad_movimiento
            )
            posiciones_bala[i][1] = posiciones_bala[i][1] + (
                math.sin(angulo_bala[i] * pi / 180.0) * cantidad_movimiento
            )
            #checar si está chocando contra enemigos
            #(Eso hay que hacerlo, no está hecho)
            #Checar si se salió de los límites:
            if (posiciones_bala[i][0] > 1 or posiciones_bala[i][0] < -1 or 
                posiciones_bala[i][1] > 1 or posiciones_bala[i][1] < -1):
                disparando[i] = False

tiempo_anterior = 0.0
estado_anterior_espacio = glfw.RELEASE

def actualizar():
    global tiempo_anterior
    global window
    global posicion_nave
    global disparando
    global angulo_bala
    global angulo_nave
    global estado_anterior_espacio
    global posicion_limite1
    #global posiciones_enemigos ##cuadrado

    tiempo_actual = glfw.get_time()
    #Cuanto tiempo paso entre la ejecucion actual
    #y la inmediata anterior de esta funcion
    tiempo_delta = tiempo_actual - tiempo_anterior

    #Leer los estados de las teclas que queremos
    estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)
    estado_tecla_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)
    estado_tecla_espacio = glfw.get_key(window, glfw.KEY_SPACE) 

    #if estado_tecla_espacio == glfw.PRESS and not disparando:
     #   disparando = True
      #  posicion_bala[0] = posicion_nave[0]
       # posicion_bala[1] = posicion_nave[1]
        #angulo_bala = angulo_nave + fase
    colision_limite1 = colisionando(
        posicion_nave[0],posicion_nave[1],
        0.05,0.05,0.05,0.05,
        posicion_limite1[0], posicion_limite1[1],
        1.00,1.00,0.6,0.6)

    cantidad_movimiento = velocidad * tiempo_delta
    if estado_tecla_arriba == glfw.PRESS:
        posicion_nave[0] = posicion_nave[0] + (math.cos((angulo_nave + fase) * pi / 180.0) * cantidad_movimiento)

    if estado_tecla_abajo == glfw.PRESS:
        posicion_nave[0] = posicion_nave[0] - (math.cos((angulo_nave + fase) * pi / 180.0) * cantidad_movimiento)

    cantidad_rotacion = velocidad_rotacion_nave * tiempo_delta
    if estado_tecla_derecha == glfw.PRESS:
        angulo_nave = angulo_nave - cantidad_rotacion
        if angulo_nave < 0.0:
            angulo_nave = angulo_nave + 360.0

    if estado_tecla_izquierda == glfw.PRESS:
        angulo_nave = angulo_nave + cantidad_rotacion
        if angulo_nave > 360.0:
            angulo_nave = angulo_nave - 360.0 

    if estado_tecla_espacio == glfw.PRESS and estado_anterior_espacio == glfw.RELEASE:
        for i in range(3):
            if not disparando[i]:
                disparando[i] = True
                posiciones_bala[i][0] = posicion_nave[0]
                posiciones_bala[i][1] = posicion_nave[1]
                angulo_bala[i] = angulo_nave + fase
                break



    actualizar_bala(tiempo_delta)
    actualizar_enemigos(tiempo_delta)
    actualizar_enemigos2(tiempo_delta)
    actualizar_enemigos3(tiempo_delta)
    actualizar_enemigos4(tiempo_delta)
    actualizar_enemigos5(tiempo_delta)
    tiempo_anterior = tiempo_actual
    estado_anterior_espacio = estado_tecla_espacio
    
def colisionando(x1,y1,wl1,wr1,hu1,hd1,x2,y2,wl2,wr2,hu2,hd2):
    colisionando = False
    if (x1 + wr1 >= x2 - wl2 
        and x1 - wl1 <= x2 + wr2 
        and y1 + hu1 >= y2 - hd2 
        and y1 - hd1 <= y2 + hu2):
        
        colisionando = True 
    return colisionando

def draw_nave():
    global posiciones_enemigos
    global posiciones_enemigos3
    global posiciones_enemigos4
    global posiciones_enemigos5
    global posicion_nave
    global window
    glPushMatrix()
    glTranslatef(posicion_nave[0], posicion_nave[1],0.0)
    glRotatef(angulo_nave, 0.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    for i in range(3):
        if colisionando(posicion_nave[0],posicion_nave[1],
            0.05,0.05,0.05,0.05,
            posiciones_enemigos[i][0], posiciones_enemigos[i][1],
            0.05,0.05,0.05,0.05):
            glColor3f(0,0,1)
            glfw.set_window_should_close(window,True)
            break
        elif colisionando(posicion_nave[0],posicion_nave[1],
            0.05,0.05,0.05,0.05,
            posiciones_enemigos2[i][0], posiciones_enemigos2[i][1],
            0.05,0.05,0.05,0.05):
            glColor3f(0,0,1)
            glfw.set_window_should_close(window,True)
            break
        elif colisionando(posicion_nave[0],posicion_nave[1],
            0.05,0.05,0.05,0.05,
            posiciones_enemigos3[i][0], posiciones_enemigos3[i][1],
            0.05,0.05,0.05,0.05):
            glColor3f(0,0,1)
            glfw.set_window_should_close(window,True)
            break
        elif colisionando(posicion_nave[0],posicion_nave[1],
            0.05,0.05,0.05,0.05,
            posiciones_enemigos4[i][0], posiciones_enemigos4[i][1],
            0.05,0.05,0.05,0.05):
            glColor3f(0,0,1)
            glfw.set_window_should_close(window,True)
            break
        elif colisionando(posicion_nave[0],posicion_nave[1],
            0.05,0.05,0.05,0.05,
            posiciones_enemigos5[i][0], posiciones_enemigos5[i][1],
            0.05,0.05,0.05,0.05):
            glColor3f(0,0,1)
            glfw.set_window_should_close(window,True)
        elif colisionando(posiciones_bala[i][0],posiciones_bala[i][1],
            0.01,0.01,0.01,0.01,
            posiciones_enemigos[i][0], posiciones_enemigos[i][1],
            0.05,0.05,0.05,0.05):
            glColor3f(0,0,0)
            vivos_enemigos[i] = False
            break

        else:
            glColor3f(1,0,0)
        

    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0.0,0.05,0)
    glVertex3f(0.05,-0.05,0)

    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-0.05, -0.05, 0)
    glVertex3f(-0.05,0.05,0.0)
    glVertex3f(0.05, 0.05,0.0)
    glVertex3f(0.05,-0.05,0.0)
    glEnd()

    glPopMatrix()

def draw_enemigos(): ##verde
    global posiciones_enemigos
    for i in range(3):
        if vivos_enemigos[i]:
            glPushMatrix()
            glTranslatef(posiciones_enemigos[i][0], posiciones_enemigos[i][1], 0.0)
            glBegin(GL_QUADS)
            glColor3f(0.3, 0.72, 0.37)
            glVertex3f(-0.05,0.05,0.0)
            glVertex3f(0.05,0.05,0.0)
            glVertex3f(0.05,-0.05,0.0)
            glVertex3f(-0.05,-0.05,0.0)
            glEnd()
        
            glBegin(GL_LINE_LOOP)
            glColor3f(0.0, 0.0, 0.0)
            glVertex3f(-0.05,0.05,0.0)
            glVertex3f(0.05,0.05,0.0)
            glVertex3f(0.05,-0.05,0.0)
            glVertex3f(-0.05,-0.05,0.0)
            glEnd()

            glPopMatrix()

def draw_enemigos2():#Azulito
    global posiciones_enemigos2
    for i in range(3):
        glPushMatrix()
        glTranslatef(posiciones_enemigos2[i][0], posiciones_enemigos2[i][1], 0.0)
        glBegin(GL_POLYGON)
        glColor3f(0.3, 0.72, 0.72)

        glVertex3f(-0.05,0.025,0.0)
        glVertex3f(-0.02,0.05,0.0)
        glVertex3f(0.02,0.05,0.0)
        glVertex3f(0.05,0.025,0.0)
        glVertex3f(0.05,-0.025,0.0)
        glVertex3f(0.02,-0.05,0.0)
        glVertex3f(-0.02,-0.05,0.0)
        glVertex3f(-0.05,-0.025,0.0)
        glEnd()
    
        glBegin(GL_LINE_LOOP)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(-0.05,0.05,0.0)
        glVertex3f(0.05,0.05,0.0)
        glVertex3f(0.05,-0.05,0.0)
        glVertex3f(-0.05,-0.05,0.0)
        glEnd()

        glPopMatrix()

def draw_enemigos3():#Naranja
    global posiciones_enemigos3
    for i in range(3):
        glPushMatrix()
        glTranslatef(posiciones_enemigos3[i][0], posiciones_enemigos3[i][1], 0.0)
        glBegin(GL_TRIANGLES)
        glColor3f(0.72, 0.53, 0.3)
        glVertex3f(-0.05,0.05,0.0)
        glVertex3f(-0.05,-0.05,0.0)
        glVertex3f(0.05,0.05,0.0)
        glVertex3f(-0.05,-0.05,0.0)
        glEnd()
    
        glBegin(GL_LINE_LOOP)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(-0.05,0.05,0.0)
        glVertex3f(0.05,0.05,0.0)
        glVertex3f(0.05,-0.05,0.0)
        glVertex3f(-0.05,-0.05,0.0)
        glEnd()

        glPopMatrix()

def draw_enemigos4():#rojo
    global posiciones_enemigos4
    for i in range(3):
        glPushMatrix()
        glTranslatef(posiciones_enemigos4[i][0], posiciones_enemigos4[i][1], 0.0)
        glBegin(GL_POLYGON)
        glColor3f(0.72, 0.30, 0.30)
        for angulo in range(0,359,5):                     ##X   ##Tamaño                        ##Altura
            glVertex3f(0.055*math.cos(angulo*math.pi/180) +0.4,0.055*math.sin(angulo*math.pi/180)-0.3, 0)
        glEnd()
        glBegin(GL_LINE_LOOP)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(-0.05,0.05,0.0)
        glVertex3f(0.05,0.05,0.0)
        glVertex3f(0.05,-0.05,0.0)
        glVertex3f(-0.05,-0.05,0.0)
        glEnd()

        glPopMatrix()

def draw_enemigos5(): ##amarillo
    global posiciones_enemigos5
    for i in range(3):
        glPushMatrix()
        glTranslatef(posiciones_enemigos5[i][0], posiciones_enemigos5[i][1], 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.72, 0.7, 0.3)
        glVertex3f(-0.05,0.0,0.0)
        glVertex3f(0.0,0.05,0.0)
        glVertex3f(0.05,0.0,0.0)
        glVertex3f(0.0,-0.05,0.0)
        glEnd()
    
        glBegin(GL_LINE_LOOP)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(-0.05,0.05,0.0)
        glVertex3f(0.05,0.05,0.0)
        glVertex3f(0.05,-0.05,0.0)
        glVertex3f(-0.05,-0.05,0.0)
        glEnd()

        glPopMatrix()


def draw_bala():
    global posiciones_bala
    global disparando
    for i in range(3):
        if disparando:
            if vivos_enemigos[i]:
                glPushMatrix()
                glTranslatef(posiciones_bala[i][0], posiciones_bala[i][1], 0.0)
                glBegin(GL_QUADS)
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(-0.01,0.01,0.0)
                glVertex3f(0.01,0.01,0.0)
                glVertex3f(0.01,-0.01,0.0)
                glVertex3f(-0.01,-0.01,0.0)
                glEnd()
                glPopMatrix()
    
def draw_estrellitas():
    glBegin(GL_LINES)
    glColor3f(1.0,1.0,1.0)
    #####
    glVertex3f(-0.4,0.85,0)
    glVertex3f(-0.4,0.84,0)

    glVertex3f(0.3,0.45,0)
    glVertex3f(0.3,0.46,0)

    glVertex3f(0.2,0.97,0)
    glVertex3f(0.2,0.98,0)

    glVertex3f(0.4,0.17,0)
    glVertex3f(0.4,0.18,0)

    glVertex3f(0.4,-0.47,0)
    glVertex3f(0.4,-0.48,0)

    glVertex3f(0.3,-0.45,0)
    glVertex3f(0.3,-0.46,0)

    glVertex3f(-0.1,-0.55,0)
    glVertex3f(-0.1,-0.54,0)

    glVertex3f(-0.7,-0.15,0)
    glVertex3f(-0.7,-0.14,0)

    glVertex3f(-0.56,-0.98,0)
    glVertex3f(-0.56,-0.96,0)

    glVertex3f(-0.52,-0.62,0)
    glVertex3f(-0.52,-0.6,0)

    glVertex3f(-0.87,-0.93,0)
    glVertex3f(-0.87,-0.95,0)

    glVertex3f(0.82,-0.33,0)
    glVertex3f(0.82,-0.34,0)

    glVertex3f(0.1,-0.23,0)
    glVertex3f(0.1,-0.24,0)
    
    glVertex3f(0.2,-0.53,0)
    glVertex3f(0.2,-0.54,0)

    glVertex3f(0.8,-0.32,0)
    glVertex3f(0.82,-0.34,0)

    glVertex3f(0.86,-0.12,0)
    glVertex3f(0.86,-0.13,0)

    glVertex3f(-0.31,-0.22,0)
    glVertex3f(-0.31,-0.23,0)

    glVertex3f(0.23,-0.26,0)
    glVertex3f(0.23,-0.26,0)

    glVertex3f(0.0,-0.53,0)
    glVertex3f(0.0,-0.54,0)

    glVertex3f(0.1,0.53,0)
    glVertex3f(0.1,0.54,0)

    glVertex3f(-0.23,-0.15,0)
    glVertex3f(-0.23,-0.16,0)

    glVertex3f(-0.42,-0.15,0)
    glVertex3f(-0.42,-0.16,0)
    
    glVertex3f(-0.93,0.43,0)
    glVertex3f(-0.93,0.44,0)

    glVertex3f(-0.46,0.42,0)
    glVertex3f(-0.46,0.43,0)

    glVertex3f(0.23,0.86,0)
    glVertex3f(0.23,0.87,0)

    glVertex3f(0.32,-0.9,0)
    glVertex3f(0.32,-0.91,0)

    glVertex3f(0.23,-0.15,0)
    glVertex3f(0.23,-0.16,0)

    ##Asterisco
    glVertex3f(0.4,0.3,0)
    glVertex3f(0.4,0.33,0)

    ##glVertex3f(0.38,0.3,0)
    ##glVertex3f(0.41,0.33,0)

    ##glVertex3f(0.4,0.3,0)
    ##glVertex3f(0.38,0.28,0)
    
    ##
    glVertex3f(-0.7,0.4,0)
    glVertex3f(-0.7,0.3,0)

    glVertex3f(-0.8,0.35,0)
    glVertex3f(-0.6,0.35,0)

    glVertex3f(-0.75,0.33,0)
    glVertex3f(-0.65,0.37,0)

    glVertex3f(-0.75,0.37,0)
    glVertex3f(-0.65,0.33,0)

    glVertex3f(-0.2,0.05,0)
    glVertex3f(-0.2,0.06,0)

    glVertex3f(-0.26,0.15,0)
    glVertex3f(-0.26,0.15,0)

    glVertex3f(0.3,0.37,0)
    glVertex3f(0.3,0.36,0)

    glVertex3f(-0.35,0.1,0)
    glVertex3f(-0.35,0.1,0)

   ##glVertex3f(0.5,0.23,0)
    ##glVertex3f(0.5,0.24,0)

    ##
    glVertex3f(0.7,-0.4,0)
    glVertex3f(0.7,-0.3,0)

    glVertex3f(0.8,-0.35,0)
    glVertex3f(0.6,-0.35,0)

    glVertex3f(0.75,-0.33,0)
    glVertex3f(0.65,-0.37,0)

    glVertex3f(0.75,-0.37,0)
    glVertex3f(0.65,-0.33,0)

    ##
    glVertex3f(0.9,-0.7,0)
    glVertex3f(0.9,-0.6,0)

    glVertex3f(1.0,-0.65,0)
    glVertex3f(0.8,-0.65,0)

    glVertex3f(0.95,-0.63,0)
    glVertex3f(0.85,-0.67,0)

    glVertex3f(0.95,-0.67,0)
    glVertex3f(0.85,-0.63,0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(.25,0.32,0.65)

    for angulo in range(0,359,5):                     ##X   ##Tamaño                        ##Altura
       glVertex3f(0.005*math.cos(angulo*math.pi/180) +0.4,0.005*math.sin(angulo*math.pi/180)-0.3, 0)
    #for angulo in range(0,359,5):                     
     #   glVertex3f(0.005*math.cos(angulo*math.pi/180) -0.4,0.005*math.sin(angulo*math.pi/180)-0.3, 0)
    #for angulo in range(0,359,5):                     
     #   glVertex3f(0.005*math.cos(angulo*math.pi/180) +0.7,0.005*math.sin(angulo*math.pi/180)+0.3, 0)
    #for angulo in range(0,359,5):                     
     #   glVertex3f(0.005*math.cos(angulo*math.pi/180) +0.6,0.005*math.sin(angulo*math.pi/180)-0.9, 0)
    #for angulo in range(0,359,5):                     
     #   glVertex3f(0.005*math.cos(angulo*math.pi/180) +0.7,0.005*math.sin(angulo*math.pi/180)-0.6, 0)
    #for angulo in range(0,359,5):                     
     #   glVertex3f(0.005*math.cos(angulo*math.pi/180) +0.4,0.005*math.sin(angulo*math.pi/180)+0.3, 0)
    #for angulo in range(0,359,5):                     
     #   glVertex3f(0.005*math.cos(angulo*math.pi/180) -0.52,0.005*math.sin(angulo*math.pi/180)-0.38, 0)

    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.95,1.0,0.0)

    glVertex3f(-0.6,0.7,0)
    glVertex3f(-0.6,0.71,0)

    glVertex3f(-0.7,0.55,0)
    glVertex3f(-0.7,0.54,0)

    glVertex3f(0.8,0.65,0)
    glVertex3f(0.8,0.64,0)

    glVertex3f(-0.1,0.75,0)
    glVertex3f(-0.1,0.74,0)
    
    glEnd()


def draw():
    draw_estrellitas()
    draw_nave()
    draw_enemigos()
    draw_enemigos2()
    draw_enemigos3()
    draw_enemigos4()
    draw_enemigos5()
    draw_bala()
    

def main():
    global window

    width = 700
    height = 700
    #Inicializar GLFW
    if not glfw.init():
        return

    #declarar ventana
    window = glfw.create_window(width, height, "Mi ventana", None, None)

    #Configuraciones de OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Verificamos la creacion de la ventana
    if not window:
        glfw.terminate()
        return

    #Establecer el contexto
    glfw.make_context_current(window)

    #Le dice a GLEW que si usaremos el GPU
    glewExperimental = True

    #Inicializar glew
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #imprimir version
    version = glGetString(GL_VERSION)
    print(version)

    #Draw loop
    while not glfw.window_should_close(window):
        #Establecer el viewport
        #glViewport(0,0,width,height)
        #Establecer color de borrado
        #glClearColor(0.03,0.03,0.08,1)
        glClearColor(0.5,0.5,0.5,1)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        actualizar()
        #Dibujar
        draw()


        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()



    
    