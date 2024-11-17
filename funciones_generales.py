from preguntas import *
import random


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

def mostrar_pregunta(pregunta):
    '''
    ¿Que hace?: Muestra en pantalla el texto de la pregunta, sus opciones (A, B o C) y define si es correcta o no lo es.
    ¿Que recibe?:      
            - pregunta (dict): Un diccionario con: pregunta["pregunta"] El texto de la pregunta (str), pregunta["opciones"]: Una lista de opciones de respuesta (list de str), pregunta["respuesta"]: La respuesta correcta (str).
    ¿Que retorna?: -
    '''
    print("Pregunta:", pregunta["pregunta"])

    # Lista de letras para las opciones
    letras_opciones = ["A", "B", "C"]
    
    # Bucle for para asociar una letra con una opcion
    for i in range(len(pregunta["opciones"])):
        letra = letras_opciones[i]
        opcion = pregunta["opciones"][i]
        print(f"{letra}. {opcion}")
    
    respuesta_usuario = input("Elige una opción (A, B o C): ").upper()
    while respuesta_usuario not in letras_opciones:
        respuesta_usuario = input("Opción inválida. Por favor, elige A, B o C: ").upper()
    
    indice = letras_opciones.index(respuesta_usuario)
    if pregunta["opciones"][indice] == pregunta["opciones"][letras_opciones.index(pregunta["respuesta"])]:
        print("Tu respuesta es... ¡CORRECTA!")
    else:
        print("Tu respuesta es... Incorrecta. La respuesta era la opción", pregunta["respuesta"])
        
