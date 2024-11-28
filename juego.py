import pygame
from funciones_generales import *
from funciones_pygame import *
from file_system import *

import time



# Configuración del juego
pygame.init()
ALTURA_PANTALLA = 600
ANCHO_PANTALLA = 800
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTURA_PANTALLA))
pygame.display.set_caption("Preguntados SDT")
fuente_pregunta = pygame.font.SysFont(None, 36)
fuente_opciones = pygame.font.SysFont(None, 32)
fuente_mensaje = pygame.font.SysFont(None, 42)
imagen_juego = pygame.image.load("./pygame/fondo_preguntados.jpg")
imagen_inicio = pygame.image.load("./pygame/fondo_estrellas_dos.png")
fuente_pequena = pygame.font.SysFont(None, 24) 


preguntas = cargar_preguntas()

# Variables del juego
input_activo = None
vidas_input = ""
puntos_input = ""
tiempo_input = ""

estado = "inicio"
bandera_juego = True
vidas_del_usuario = 3
puntos = 0
puntos_por_correcta = 25
correctas = 0
mensaje = None
mostrar_boton_siguiente = False
mostrar_texto = False
tiempo_inicio = None
nombre_usuario = ""
tiempo_total_partida = 60
tiempo_inicio_partida = None
tiempo_restante = tiempo_total_partida

while bandera_juego:
    lista_eventos = pygame.event.get()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    clic_realizado = False

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera_juego = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            clic_realizado = True

    if estado == "inicio":
        #region inicio
        pantalla.blit(imagen_inicio, (0, 0))
        ancho_boton = 300
        alto_boton = 50
        espacio_entre_botones = 20
        espacio_extra_salir = 40

        total_altura_botones = 2 * alto_boton + espacio_entre_botones + espacio_extra_salir + alto_boton
        y_inicial = (ALTURA_PANTALLA - total_altura_botones) // 2 + 50  

        x_centrado = (ANCHO_PANTALLA - ancho_boton) // 2

        rect_iniciar = dibujar_boton("Iniciar Juego", x_centrado, y_inicial, alto_boton, ancho_boton, (0, 0, 255), pantalla)
        rect_ver_puntajes = dibujar_boton("Ver Puntajes", x_centrado, y_inicial + alto_boton + espacio_entre_botones, alto_boton, ancho_boton, (0, 0, 255), pantalla)
        rect_eliminar_partidas_previas = dibujar_boton("Eliminar Partidas Previas",  x_centrado, y_inicial + alto_boton + (espacio_entre_botones + 70), alto_boton, ancho_boton, (0, 0, 255), pantalla)
        rect_configuraciones = dibujar_boton("Configuraciones", x_centrado, y_inicial + alto_boton + (espacio_entre_botones + 140), alto_boton, ancho_boton, (0, 0, 255), pantalla)
        rect_salir = dibujar_boton("Salir del Juego", x_centrado, y_inicial + 2 * (alto_boton + espacio_entre_botones *2 + 30) + espacio_extra_salir, alto_boton, ancho_boton, (0, 0, 255), pantalla)

        if clic_realizado:
            if rect_iniciar.collidepoint(mouse_x, mouse_y):
                estado = "juego"
                categoria, pregunta_actual = elegir_pregunta_aleatoria(preguntas)
                
                vidas_del_usuario = vidas_del_usuario
                puntos = 0
                correctas = 0
                mensaje = None
                mostrar_boton_siguiente = False
                tiempo_total_partida = tiempo_total_partida
                tiempo_restante = tiempo_total_partida
            elif rect_ver_puntajes.collidepoint(mouse_x, mouse_y):
                estado = "puntuaciones"
            elif rect_eliminar_partidas_previas.collidepoint(mouse_x, mouse_y):
                
                datos = {"top_puntuaciones": []}
                eliminar_datos_previos(datos)
                if eliminar_datos_previos(datos):
                    mostrar_texto = True
                    tiempo_inicio = time.time()
                if mostrar_texto:
                    if time.time() - tiempo_inicio <= 3: 
                        texto_ok = fuente_pequena.render("Datos previos eliminados!", True, (0,0,0))
                        pantalla.blit(
                            texto_ok,
                            ((ANCHO_PANTALLA - texto_ok.get_width()) // 2,  
                            ALTURA_PANTALLA - texto_ok.get_height() - 10) 
                        )
                    else:
                        mostrar_texto = False  
            

                
            elif rect_configuraciones.collidepoint(mouse_x, mouse_y):
                estado = "configuraciones"
            elif rect_salir.collidepoint(mouse_x, mouse_y):
                bandera_juego = False
        #endregion
    elif estado == "juego":
        pantalla.blit(imagen_juego, (0, 0))
        
        if tiempo_inicio_partida is None:
            tiempo_inicio_partida = time.time()  

        tiempo_transcurrido_partida = time.time() - tiempo_inicio_partida
        tiempo_restante_partida = max(0, tiempo_total_partida - int(tiempo_transcurrido_partida))

        texto_tiempo = fuente_opciones.render(f"Tiempo: {tiempo_restante_partida}s", True, (255, 0, 0))
        pantalla.blit(texto_tiempo, (ANCHO_PANTALLA - 150, 20))

        if tiempo_restante_partida == 0:
            estado = "fin"
            mensaje = f"Juego terminado. Puntos: {puntos}. Respuestas correctas: {correctas}."

        texto_regreso = fuente_pequena.render("Pulse ESC para salir de la partida!", True, (0, 0, 0))
        texto_pregunta = fuente_pregunta.render(pregunta_actual["pregunta"], True, (0, 0, 0))

        x_pregunta = (ANCHO_PANTALLA - texto_pregunta.get_width()) // 2
        y_pregunta = ALTURA_PANTALLA // 4 - texto_pregunta.get_height() // 2
        pantalla.blit(texto_pregunta, (x_pregunta, y_pregunta))

        altura_respuestas = y_pregunta + texto_pregunta.get_height() + 50
        espacio_entre_botones = 20
        ancho_boton = 300
        alto_boton = 50

        rect_respuesta_a = dibujar_boton(f"A. {pregunta_actual['opciones'][0]}",
                                        (ANCHO_PANTALLA - ancho_boton) // 2,
                                        altura_respuestas,
                                        alto_boton, ancho_boton, (150, 50, 0), pantalla)

        rect_respuesta_b = dibujar_boton(f"B. {pregunta_actual['opciones'][1]}",
                                        (ANCHO_PANTALLA - ancho_boton) // 2,
                                        altura_respuestas + alto_boton + espacio_entre_botones,
                                        alto_boton, ancho_boton, (50, 150, 0), pantalla)

        rect_respuesta_c = dibujar_boton(f"C. {pregunta_actual['opciones'][2]}",
                                        (ANCHO_PANTALLA - ancho_boton) // 2,
                                        altura_respuestas + 2 * (alto_boton + espacio_entre_botones),
                                        alto_boton, ancho_boton, (0, 0, 150), pantalla)

        if clic_realizado and not mostrar_boton_siguiente:
            if rect_respuesta_a.collidepoint(mouse_x, mouse_y):
                respuesta = "A"
            elif rect_respuesta_b.collidepoint(mouse_x, mouse_y):
                respuesta = "B"
            elif rect_respuesta_c.collidepoint(mouse_x, mouse_y):
                respuesta = "C"
            else:
                respuesta = None

            if respuesta:
                if respuesta == pregunta_actual["respuesta"]:
                    puntos += puntos_por_correcta
                    correctas += 1
                    mensaje = "¡Correcto!"
                else:
                    vidas_del_usuario -= 1
                    if puntos > 10:
                        puntos -= 10
                    else:
                        puntos = 0
                    mensaje = "Incorrecto."
                    if vidas_del_usuario == 0:
                        estado = "fin"  
                        mensaje = f"Juego terminado. Puntos: {puntos}. Respuestas correctas: {correctas}."
                        tiempo_restante_partida = 0
                mostrar_boton_siguiente = True

        rect_puntos = pygame.Rect(10, 10, 200, 40)
        rect_vidas = pygame.Rect(10, 60, 200, 40)
        pygame.draw.rect(pantalla, (173, 216, 230), rect_puntos)  
        pygame.draw.rect(pantalla, (173, 216, 230), rect_vidas)  

        pygame.draw.rect(pantalla, (0, 0, 0), rect_puntos, 2)
        pygame.draw.rect(pantalla, (0, 0, 0), rect_vidas, 2)

        texto_puntos = fuente_opciones.render(f"Puntos: {puntos}", True, (0, 0, 0))
        texto_vidas = fuente_opciones.render(f"Vidas: {vidas_del_usuario}", True, (0, 0, 0))
        texto_tiempo = fuente_opciones.render(f"Tiempo: {tiempo_restante_partida}", True, (0, 0, 0))
        
        pantalla.blit(texto_puntos, (rect_puntos.x + 10, rect_puntos.y + 5))
        pantalla.blit(texto_vidas, (rect_vidas.x + 10, rect_vidas.y + 5))

        if mostrar_boton_siguiente:
            rect_siguiente = dibujar_boton("Próxima Pregunta", (ANCHO_PANTALLA - ancho_boton) // 2, 500, 50, 300, (0, 255, 0), pantalla)

            if mensaje:
                y_mensaje = altura_respuestas + 3 * (alto_boton + espacio_entre_botones) + 20

                if mensaje == "¡Correcto!":
                    color_mensaje = (0, 150, 0)
                else:
                    color_mensaje = (255, 0, 0)

                texto_mensaje = fuente_mensaje.render(mensaje, True, color_mensaje)
                x_mensaje = (ANCHO_PANTALLA - texto_mensaje.get_width()) // 2
                pantalla.blit(texto_mensaje, (x_mensaje, y_mensaje))

            if clic_realizado and rect_siguiente.collidepoint(mouse_x, mouse_y):
                categoria, pregunta_actual = elegir_pregunta_aleatoria(preguntas)
                mensaje = None
                mostrar_boton_siguiente = False

        y_posicion_regreso = ALTURA_PANTALLA - 30
        pantalla.blit(texto_regreso, ((ANCHO_PANTALLA - texto_regreso.get_width()) // 2, y_posicion_regreso))

        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    estado = "inicio"
                    

        #endregion
    elif estado == "configuraciones":
    #region configuraciones
        pantalla.blit(imagen_juego, (0, 0))
        titulo_rect = pygame.Rect(0, 0, ANCHO_PANTALLA, 50)
        input_vidas_rect = pygame.Rect(ANCHO_PANTALLA // 2 - 200, ALTURA_PANTALLA // 2 - 100, 400, 50)
        input_tiempo_rect = pygame.Rect(ANCHO_PANTALLA // 2 - 200, ALTURA_PANTALLA // 2 + 100 , 400, 50)
        input_puntos_rect = pygame.Rect(ANCHO_PANTALLA // 2 - 200, ALTURA_PANTALLA // 2, 400, 50)
        boton_aceptar_rect = pygame.Rect(ANCHO_PANTALLA // 2 - 100, ALTURA_PANTALLA // 2 + 170, 200, 50)

        fuente_titulo = pygame.font.Font(None, 60)
        titulo_texto = "Configuraciones"
        superficie_titulo = fuente_titulo.render(titulo_texto, True, (0, 0, 0))
        pantalla.blit(superficie_titulo, (titulo_rect.centerx - superficie_titulo.get_width() // 2, 50))
        texto_regreso = fuente_pequena.render("Pulse ESC para volver!", True, (0, 0, 0))

        
        if input_activo == "vidas":
            color_input_vidas = (0, 0, 255) 
        else:
            color_input_vidas = (0, 0, 0)
        if input_activo == "puntos":
            color_input_puntos = (0, 0, 255) 
        else:
            color_input_puntos = (0, 0, 0)
            
        if input_activo == "tiempo":
            color_input_tiempo = (0, 0, 255) 
        else:
            color_input_tiempo = (0, 0, 0)
            
            

        pygame.draw.rect(pantalla, color_input_vidas, input_vidas_rect, 2)
        pygame.draw.rect(pantalla, color_input_puntos, input_puntos_rect, 2)
        pygame.draw.rect(pantalla, color_input_tiempo, input_tiempo_rect, 2)
        pygame.draw.rect(pantalla, (34, 139, 34), boton_aceptar_rect)

        texto_vidas = f"Vidas por partida: {vidas_del_usuario}"
        texto_puntos = f"Puntos por respuesta correcta: {puntos_por_correcta}"
        texto_tiempo = f"Tiempo por partida: {tiempo_total_partida} segundos"
        
        superficie_vidas = fuente_opciones.render(texto_vidas, True, (0, 0, 0))
        superficie_puntos = fuente_opciones.render(texto_puntos, True, (0, 0, 0))
        superficie_tiempo = fuente_opciones.render(texto_tiempo, True, (0, 0, 0))
        
        texto_aceptar = fuente_opciones.render("Aceptar", True, (255, 255, 255))

        pantalla.blit(superficie_vidas, (input_vidas_rect.x + 5, input_vidas_rect.y - 30))
        pantalla.blit(superficie_puntos, (input_puntos_rect.x + 5, input_puntos_rect.y - 30))
        pantalla.blit(superficie_tiempo, (input_tiempo_rect.x + 5, input_tiempo_rect.y - 30))
        pantalla.blit(texto_aceptar, (boton_aceptar_rect.centerx - texto_aceptar.get_width() // 2, boton_aceptar_rect.centery - texto_aceptar.get_height() // 2))
        color_texto = (255, 0, 0)  
        mensaje_error = ""
        font = pygame.font.Font(None, 36)
        
        error =False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_vidas_rect.collidepoint(event.pos):
                    input_activo = "vidas"
                elif input_puntos_rect.collidepoint(event.pos):
                    input_activo = "puntos"
                elif input_tiempo_rect.collidepoint(event.pos):
                    input_activo = "tiempo"
                elif boton_aceptar_rect.collidepoint(event.pos):
                    estado = "inicio"
                else:
                    input_activo = None

            if event.type == pygame.KEYDOWN:
                if input_activo in ["vidas", "puntos", "tiempo"]:
                    if input_activo == "vidas":
                        input_var = vidas_input
                    elif input_activo == "puntos":
                        input_var = puntos_input
                    elif input_activo == "tiempo":
                        input_var = tiempo_input

                    if event.key == pygame.K_RETURN:
                        input_activo = None
                        mensaje_error = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_var = input_var[:-1]
                    elif event.unicode.isdigit():
                        input_var += event.unicode

                    if input_activo == "vidas":
                        vidas_input = input_var
                        if vidas_input:
                            vidas_del_usuario = int(vidas_input)
                            if not (1 <= vidas_del_usuario <= 99):  
                                mensaje_error = "Las vidas deben estar entre 1 y 99."
                                error = True
                                vidas_del_usuario = 3 
                        else:
                            vidas_del_usuario = 3  

                    elif input_activo == "puntos":
                        puntos_input = input_var
                        if puntos_input:
                            puntos_por_correcta = int(puntos_input)
                            if puntos_por_correcta < 1 or puntos_por_correcta > 101: 
                                mensaje_error = "Los puntos deben ser al menos 1 y menores a 100"
                                error =True
                                puntos_por_correcta = 25 
                        else:
                            puntos_por_correcta = 25  

                    elif input_activo == "tiempo":
                        tiempo_input = input_var
                        if tiempo_input:
                            tiempo_total_partida = int(tiempo_input)
                            if tiempo_total_partida < 1 or tiempo_total_partida > 120:  
                                mensaje_error = "El tiempo debe ser mayor a 0 y menor a 120 segundos"
                                error = True
                                tiempo_total_partida = 60 
                        else:
                            tiempo_total_partida = 60 
                            
                            
            if error:
                texto_renderizado = font.render(mensaje_error, True, color_texto)
                pantalla.blit(texto_renderizado, (50, 50))  



        vidas_text = fuente_opciones.render(vidas_input, True, (0, 0, 0))
        puntos_text = fuente_opciones.render(puntos_input, True, (0, 0, 0))
        tiempo_text = fuente_opciones.render(tiempo_input, True, (0, 0, 0))
        

        pantalla.blit(vidas_text, (input_vidas_rect.x + 10, input_vidas_rect.y + 10))
        pantalla.blit(puntos_text, (input_puntos_rect.x + 10, input_puntos_rect.y + 10))
        pantalla.blit(tiempo_text, (input_tiempo_rect.x + 10, input_tiempo_rect.y + 10))
        
        y_posicion_regreso = ALTURA_PANTALLA - 60 
        pantalla.blit(texto_regreso, ((ANCHO_PANTALLA - texto_regreso.get_width()) // 2, y_posicion_regreso))

        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    estado = "inicio"

            
        #endregion
    elif estado == "fin":
        #region fin
        pantalla.fill((255, 255, 255))
        texto_final = fuente_pregunta.render("Juego Terminado", True, (0, 0, 0))
        texto_puntaje_final = fuente_pregunta.render(f"Puntaje Final: {puntos}", True, (0, 0, 0))
        texto_respuestas_correctas = fuente_pregunta.render(f"Respuestas Correctas: {correctas}", True, (0, 0, 0))
        pantalla.blit(texto_final, ((ANCHO_PANTALLA - texto_final.get_width()) // 2, ALTURA_PANTALLA // 4))
        pantalla.blit(texto_puntaje_final, ((ANCHO_PANTALLA - texto_puntaje_final.get_width()) // 2, ALTURA_PANTALLA // 2))
        pantalla.blit(texto_respuestas_correctas, ((ANCHO_PANTALLA - texto_respuestas_correctas.get_width()) // 2, ALTURA_PANTALLA // 2 + 50))

        input_rect = pygame.Rect(200, 450, 400, 50)
        color_input = (0, 0, 255)
        pygame.draw.rect(pantalla, color_input, input_rect, 2)

        texto_ingresado = fuente_opciones.render(nombre_usuario, True, (0, 0, 0))
        pantalla.blit(texto_ingresado, (input_rect.x + 10, input_rect.y + 10))

        instrucciones = fuente_opciones.render("Ingrese su nombre y presione Enter:", True, (0, 0, 0))
        pantalla.blit(instrucciones, ((ANCHO_PANTALLA - instrucciones.get_width()) // 2, 400))

        partida = {
            "usuario": nombre_usuario,
            "puntuacion": puntos
        }
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  
                    if nombre_usuario.strip():  
                        agregar_top_diez(partida)
                        estado = "puntuaciones"
                        vidas_del_usuario = 3
                        puntos = 0
                        correctas = 0
                        mensaje = None
                        mostrar_boton_siguiente = False
                        nombre_usuario = ""
                        tiempo_inicio_partida = None 
                    else:
                        nombre_usuario = ""
                elif evento.key == pygame.K_BACKSPACE: 
                    nombre_usuario = nombre_usuario[:-1]
                else:
                    if evento.unicode.isalnum() and len(nombre_usuario) < 20:
                        nombre_usuario += evento.unicode

        #endregion
    elif estado == "puntuaciones":
        #region puntuaciones
        
        pantalla.blit(imagen_juego, (0, 0))
        
        texto_puntajes = fuente_pregunta.render("Tabla de Puntajes", True, (0, 0, 0))

        texto_regreso = fuente_pequena.render("Pulse ESC para volver...", True, (0, 0, 0))

        pantalla.blit(texto_puntajes, ((ANCHO_PANTALLA - texto_puntajes.get_width()) // 2, ALTURA_PANTALLA // 10))
        
        y_posicion_regreso = ALTURA_PANTALLA - 60 
        pantalla.blit(texto_regreso, ((ANCHO_PANTALLA - texto_regreso.get_width()) // 2, y_posicion_regreso))

        datos = leer_datos()
        top_puntuaciones = datos.get("top_puntuaciones", [])
        
        if len(top_puntuaciones) == 0:
            mensaje = fuente_pequena.render("No hay puntuaciones registradas", True, (0, 0, 0))
            pantalla.blit(mensaje, ((ANCHO_PANTALLA - mensaje.get_width()) // 2, ALTURA_PANTALLA // 2))
        
        top_puntuaciones_ordenado = sorted(top_puntuaciones, reverse=True, key=lambda puntuacion: puntuacion["puntuacion"])
        
        top = top_puntuaciones_ordenado[:10]
        
        y_posicion = ALTURA_PANTALLA // 5 + 40  
        fuente_pequena_puntajes = pygame.font.SysFont(None, 28)

        for i, puntuacion in enumerate(top):
            texto = fuente_pequena_puntajes.render(f"{i + 1}. {puntuacion['usuario']}: {puntuacion['puntuacion']} puntos", True ,(0, 0, 0))
            pantalla.blit(texto, (ANCHO_PANTALLA // 2 - texto.get_width() // 2, y_posicion))
            y_posicion += 35
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    estado = "inicio"

        #endregion
    
    pygame.display.flip()


pygame.quit()
