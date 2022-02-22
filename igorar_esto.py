def actualizar_nave(tiempo_delta):
    global angulo_triangulo
    global posicion_nave
    global disparando
    global angulo_bala
    global estado_anterior_espacio

    #################33
    global tiempo_anterior  ####
    global window           ####
    #######
    tiempo_actual = glfw.get_time() ##
    tiempo_delta = tiempo_actual - tiempo_anterior###

    estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)
    estado_tecla_espacio = glfw.get_key(window, glfw.KEY_SPACE)

    if estado_tecla_espacio == glfw.PRESS and estado_anterior_espacio == glfw.RELEASE:
        for i in range(3):
            if not disparando[i]:
                disparando[i] = True
                posiciones_bala[i][0] = posicion_nave[0]
                posiciones_bala[i][1] = posicion_nave[1]
                angulo_bala[i] = angulo_triangulo + fase
                break

    cantidad_movimiento = velocidad * tiempo_delta ####
    if estado_tecla_derecha == glfw.PRESS:
        for i in range(3):
         if not colisionando(
            posicion_nave[0] ,posicion_nave[1],
            0.05,0.05,0.05,0.05,
            posiciones_enemigos[i][0] , posiciones_enemigos[i][1] ,
            0.05,0.05,0.2,0.2):
            posicion_nave[0] = posicion_nave[0] + cantidad_movimiento


    ###########################################3
    if estado_tecla_izquierda == glfw.PRESS:
        for i in range(3):
            if not colisionando(
                posicion_nave[0] ,posicion_nave[1],
                0.05,0.05,0.05,0.05,
                posiciones_enemigos[i][0] , posiciones_enemigos[i][1] ,
                0.05,0.05,0.2,0.2):
                posicion_nave[0] = posicion_nave[0] - cantidad_movimiento


    actualizar_bala(tiempo_delta)  
    actualizar_enemigos(tiempo_delta) 
    actualizar_enemigos2(tiempo_delta) 
    actualizar_enemigos3(tiempo_delta)  
    actualizar_enemigos4(tiempo_delta)  
    actualizar_enemigos5(tiempo_delta) 
    tiempo_anterior = tiempo_actual    
    



def actualizar():
    global tiempo_anterior
    global window
    global posicion_nave
    
    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior
    cantidad_movimiento = velocidad * tiempo_delta
    