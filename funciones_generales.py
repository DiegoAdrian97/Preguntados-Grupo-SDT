from preguntas import *
from file_system import *
from manejo_de_usuarios import *
import random
import time


    
def iniciar_juego(datos: dict, vidas_del_usuario: int, puntos: int, puntos_por_correcta: int) -> None:
    '''
        ¿Que hace?: Comienza el juego, se elige aleatoriamente una pregunta y se muestra en pantalla.
        ¿Que recibe?: Los datos del usuario que juega, la cantidad de vidas y la cantidad de puntos y la configuracion del juego.
        ¿Que retorna?: La pregunta elegida aleatoriamente dentro de la categoría, que incluye el texto de la pregunta, las opciones y la respuesta correcta.'''
    
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
    def elegir_pregunta_aleatoria() -> str:
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
    
    
    
    
    def mostrar_pregunta(pregunta: str,vidas_del_usuario: int, puntos: int, datos: dict)-> str:
        
        '''
        ¿Que hace?: Muestra en pantalla el texto de la pregunta, sus opciones (A, B o C) y define si es correcta o no lo es.
        ¿Que recibe?:      
                - pregunta (dict): Un diccionario con: pregunta["pregunta"] El texto de la pregunta (str), pregunta["opciones"]: Una lista de opciones de respuesta (list de str), pregunta["respuesta"]: La respuesta correcta (str).
        ¿Que retorna?: 
                - respuesta_correcta (bool): True si la respuesta es correcta, False si no lo es.
        '''
        
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
            
            puntos += puntos_por_correcta
            print(f'''
                  Tu respuesta es... ¡CORRECTA!
                  Tu puntuacion: {puntos} puntos!
                  ''')
            categoria, pregunta_aleatoria = elegir_pregunta_aleatoria()
            mostrar_pregunta(pregunta_aleatoria, vidas_del_usuario, puntos, datos)
            
        else:
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
                    print(f"Tu puntuacion final es de {puntos} puntos.")
                    partida = {
                    "usuario": datos.get("usuarios")[-1]["nombre"],
                    "puntuacion": puntos}
                    datos["top_puntuaciones"].append(partida)
                    return guardar_datos(datos)
            else:
                print("Te quedan", vidas_del_usuario, "vidas restantes.")
                categoria, pregunta_aleatoria = elegir_pregunta_aleatoria()
                mostrar_pregunta(pregunta_aleatoria, vidas_del_usuario, puntos, datos)        
        
    
    
    categoria, pregunta_aleatoria = elegir_pregunta_aleatoria()
    mostrar_pregunta(pregunta_aleatoria, vidas_del_usuario, puntos, datos)
    
def ver_top10(datos: dict) -> dict:
    '''
    ¿Qué hace?: Muestra el top 10 de puntuaciones de los usuarios.
    ¿Qué recibe?: El diccionario con los datos de los usuarios y sus puntuaciones.
    ¿Qué retorna?: Una lista con las 10 mejores puntuaciones y sus usuarios.
    '''
    top_puntuaciones = datos.get("top_puntuaciones")

    if not top_puntuaciones:
        print("No hay puntuaciones registradas.")
        return []
    
    top_puntuaciones_ordenado = sorted(top_puntuaciones, reverse=True, key=lambda puntuacion: puntuacion["puntuacion"])

    top = top_puntuaciones_ordenado[:10]

    print("Top 10 puntuaciones:")
    for i in range(len(top)):
        top10 = print(f"{i + 1}. Usuario: {top[i]['usuario']}, Puntuación: {top[i]['puntuacion']}")

    return top10

def configuracion_del_juego(configuracion_del_juego: dict) -> dict :
    '''
    ¿Que hace?: Modifica la configuracion default del juego
    ¿Que recibe?: El diccionario con la configuracion del juego
    ¿Que retorna?: La configuracion del juego actualizada
    '''
    
    
    while True:
        print("\nConfiguración del juego:")
        print("A. Cambiar la cantidad de vidas")
        print("B. Cambiar la cantidad de puntos por respuesta correcta")
        print("C. Salir")
        
        
        opcion = str(input("Seleccione una opcion (A-C): ")).upper()
        
        if opcion == "A":
            vidas_del_usuario = int(input("Ingrese la cantidad de vidas deseadas: "))
            configuracion_del_juego.update({"vidas": vidas_del_usuario})
        elif opcion == "B":
            puntos_por_correcta = int(input("Ingrese la cantidad de puntos por respuesta correcta: "))
            configuracion_del_juego.update({"puntos_por_correcta": puntos_por_correcta})
        elif opcion == "C":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    
    return vidas_del_usuario, puntos_por_correcta

def menu_agregar_pregunta(preguntas: dict) -> dict:
    '''
    ¿Que hace?: Muestra el menu de agregar preguntas
    ¿Que recibe?: El diccionario con las preguntas
    ¿Que retorna?: El diccionario con las preguntas actualizado
    '''
    def agregar_pregunta(preguntas:dict) -> dict:
        '''
        ¿Que hace?: Agrega preguntas al diccionario de preguntas
        ¿Que recibe?: El diccionario con las preguntas
        ¿Que retorna?: El diccionario con las preguntas actualizado
        '''
    
        categoria = input("Ingrese la categoria de la pregunta: ")
        while categoria not in preguntas.keys():
            categoria = input("Categoría Inexistente. Por favor, ingrese una categoría existente: ")
        
        pregunta = input("Ingrese la pregunta: ")
        opcionA = input("Ingrese la respuesta: ")
        opcionB = input("Ingrese la respuesta: ")
        opcionC = input("Ingrese la respuesta: ")
        respuesta_correcta = input("Ingrese la respuesta correcta(A, B o C): ").upper()
        while respuesta_correcta != "A" and respuesta_correcta != "B" and respuesta_correcta != "C":
            respuesta_correcta = input("Respuesta incorrecta. Por favor, ingrese la respuesta correcta(A,B o C): ").upper()
        opciones = [opcionA, opcionB, opcionC]
        
        pregunta = {
            "pregunta": pregunta.title(), 
            "opciones": opciones, 
            "respuesta": respuesta_correcta
        }
        preguntas[categoria].append(pregunta)
        preguntas.update({categoria:pregunta})
        return print(preguntas)
    while True:
        print("\nMenú de opciones:")
        print("A. Agregar pregunta")
        print("B. Salir")
        
        opcion = str(input("Seleccione una opcion (A-B): ")).upper()
        
        if opcion == "A":
            agregar_pregunta(preguntas)
        elif opcion == "B":
            break
        else:
            print("Opción no válida. Intente de nuevo.")