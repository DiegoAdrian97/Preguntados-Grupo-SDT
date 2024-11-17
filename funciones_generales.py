from preguntas import *
import random
import time
    
def iniciar_juego():
    
    #region temporizador SOLO EN PYGAME
    # def contador_regresivo(segundos):
    #     '''
    #     ¿Que hace?: Genera el contador de tiempo, si llega a 0 el usuario pierde.
    #     ¿Que recibe?: Recibe la cantidad de segundos a configurar
    #     ¿Que retorna?: El tiempo corriendo
    #     '''
    #     while segundos > 0:
    #         print(f"Tiempo restante: {segundos} segundos", end="\r")
    #         time.sleep(1)
    #         segundos -= 1
    #         tiempo_corriendo = True
    #     print("¡Se acabó el tiempo!")
    #     tiempo_corriendo = False 
    
    #endregion
    def elegir_pregunta_aleatoria():
        '''
        ¿Que hace?: Selecciona aleatoriamente una categoría de preguntas y luego elige aleatoriamente una pregunta dentro de esa categoría.
        ¿Que recibe?: No recibe nada, pero utiliza el diccionario de preguntas, opciones y respuestas.
        ¿Que retorna?:
            - categoria (str): El nombre de la categoría seleccionada aleatoriamente.
            - pregunta_aleatoria (dict) La pregunta elegida aleatoriamente dentro de la categoría, que incluye el texto de la pregunta, las opciones y la respuesta correcta.
        '''
        categoria = random.choice(list(preguntas.keys()))
        pregunta_aleatoria = random.choice(preguntas[categoria])
        return categoria, pregunta_aleatoria
    
    
    
    
    def mostrar_pregunta(pregunta,vidas_del_usuario, puntos):
        
        '''
        ¿Que hace?: Muestra en pantalla el texto de la pregunta, sus opciones (A, B o C) y define si es correcta o no lo es.
        ¿Que recibe?:      
                - pregunta (dict): Un diccionario con: pregunta["pregunta"] El texto de la pregunta (str), pregunta["opciones"]: Una lista de opciones de respuesta (list de str), pregunta["respuesta"]: La respuesta correcta (str).
        ¿Que retorna?: 
                - respuesta_correcta (bool): True si la respuesta es correcta, False si no lo es.
        '''
        respuesta_correcta = False
        
        print("Pregunta:", pregunta["pregunta"])

        letras_opciones = ["A", "B", "C"]
        
        for i in range(len(pregunta["opciones"])):
            letra = letras_opciones[i]
            opcion = pregunta["opciones"][i]
            print(f"{letra}. {opcion}")
        
        respuesta_usuario = input("Elige una opción (A, B o C): ").upper()
        
        while respuesta_usuario not in letras_opciones:
            respuesta_usuario = input("Opción inválida. Por favor, elige A, B o C: ").upper()
        
        indice = letras_opciones.index(respuesta_usuario)
        if pregunta["opciones"][indice] == pregunta["opciones"][letras_opciones.index(pregunta["respuesta"])]:
            respuesta_correcta = True
            puntos += 25
            print(f'''
                  Tu respuesta es... ¡CORRECTA!
                  Tu puntuacion: {puntos} puntos!
                  ''')
            categoria, pregunta_aleatoria = elegir_pregunta_aleatoria()
            mostrar_pregunta(pregunta_aleatoria, vidas_del_usuario, puntos)
            
        else:
            respuesta_correcta = False
            if puntos > 10:
                puntos -= 10
            else:
                puntos = 0
            print(f'''
                  Tu respuesta es... Incorrecta. La respuesta era la opción {pregunta["respuesta"]}
                  Tu puntuacion: {puntos} puntos!
                  ''', )
            vidas_del_usuario -= 1
            if vidas_del_usuario == 0:
                    print("Te quedaste sin vidas. Has perdido la partida.")
                    return puntos
            else:
                print("Te quedan", vidas_del_usuario, "vidas restantes.")
                categoria, pregunta_aleatoria = elegir_pregunta_aleatoria()
                mostrar_pregunta(pregunta_aleatoria, vidas_del_usuario, puntos)        
        
    vidas_del_usuario = 3
    puntos = 0
    
    categoria, pregunta_aleatoria = elegir_pregunta_aleatoria()
    mostrar_pregunta(pregunta_aleatoria, vidas_del_usuario, puntos)
    