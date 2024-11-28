
from file_system import *
import random

def elegir_pregunta_aleatoria(preguntas) -> str:
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
    
def iniciar_juego(datos: dict, preguntas:dict, vidas_del_usuario: int, puntos: int, puntos_por_correcta: int) -> None:
    '''
        ¿Que hace?: Comienza el juego, se elige aleatoriamente una pregunta y se muestra en pantalla.
        ¿Que recibe?: Los datos del usuario que juega, la cantidad de vidas y la cantidad de puntos y la configuracion del juego.
        ¿Que retorna?: La pregunta elegida aleatoriamente dentro de la categoría, que incluye el texto de la pregunta, las opciones y la respuesta correcta.'''
    while datos == "Volver":
        return
    
    #endregion
    
    def mostrar_pregunta(pregunta: str,vidas_del_usuario: int, puntos: int, datos: dict)-> str:
        
        '''
        ¿Que hace?: Muestra en pantalla el texto de la pregunta, sus opciones (A, B o C) y define si es correcta o no lo es.
        ¿Que recibe?:      
                - pregunta (dict): Un diccionario con: pregunta["pregunta"] El texto de la pregunta (str), pregunta["opciones"]: Una lista de opciones de respuesta (list de str), pregunta["respuesta"]: La respuesta correcta (str).
        ¿Que retorna?: 
                - respuesta_correcta (bool): True si la respuesta es correcta, False si no lo es.
        '''
        
        print("*" * 60)
        print("¡Es hora de la pregunta!".center(60))
        print("*" * 60)
        print(f"\n{pregunta["pregunta"].center(60)}\n")

        letras_opciones = ["A", "B", "C"]
        
        for i in range(len(pregunta["opciones"])):
            letra = letras_opciones[i]
            opcion = pregunta["opciones"][i]
            texto = f"{letra}. {opcion}"
            print(f"{texto.center(58)}")

        respuesta_usuario = input("\n" + " " * 16 + "Elige una opción (A, B o C): ").upper()
        
        while respuesta_usuario not in letras_opciones:
            respuesta_usuario = input("\n" + " " * 10 +"Opción inválida. Por favor, elige A, B o C: ").upper()
        
        if respuesta_usuario == pregunta["respuesta"]:
            puntos += puntos_por_correcta
            print("\n")
            print("|" + f"Tu respuesta es... ¡CORRECTA!. ".center(58) + "|")
            print("|" + f"Tu puntuacion: {puntos} puntos!".center(58) + "|")
            print("\n")
            categoria, pregunta_aleatoria = elegir_pregunta_aleatoria(preguntas)
            mostrar_pregunta(pregunta_aleatoria, vidas_del_usuario, puntos, datos)
            
        else:
            print("\n")
            print("|" + f"Tu respuesta es... Incorrecta. La respuesta era la {pregunta['respuesta']}".center(58) + "|")
            print("|" + f"Tu puntuacion: {puntos} puntos!".center(58) + "|")
                
            vidas_del_usuario -= 1
            if vidas_del_usuario == 0:
                    print("\n")
                    print("|" + "Te quedaste sin vidas. Has perdido la partida.".center(58) + "|")
                    print("|" + f"Tu puntuacion final es de {puntos} puntos.".center(58) + "|")
                    nombre_jugador = input(" " * 15 +"\nIngrese su nombre de usuario: ")
                    partida = {
                    "usuario": nombre_jugador,
                    "puntuacion": puntos
                    }
                    datos["top_puntuaciones"].append(partida)
                    print("Partida guardada exitosamente.")
                    return guardar_datos(datos)
            else:
                print("|" + f"Te quedan {vidas_del_usuario} vidas restantes.".center(58) + "|")
                print("\n")
                categoria, pregunta_aleatoria = elegir_pregunta_aleatoria(preguntas)
                mostrar_pregunta(pregunta_aleatoria, vidas_del_usuario, puntos, datos)        
        
    
    
    categoria, pregunta_aleatoria = elegir_pregunta_aleatoria(preguntas)
    mostrar_pregunta(pregunta_aleatoria, vidas_del_usuario, puntos, datos)
    
def ver_top10(datos: dict) -> dict:
    '''
    ¿Qué hace?: Muestra el top 10 de puntuaciones de los usuarios.
    ¿Qué recibe?: El diccionario con los datos de los usuarios y sus puntuaciones.
    ¿Qué retorna?: Una lista con las 10 mejores puntuaciones y sus usuarios.
    '''
    top_puntuaciones = datos.get("top_puntuaciones")

    if not top_puntuaciones:
        print("No hay puntuaciones registradas.".center(60))
        print("Aprovecha y sé el primero en jugar. ¡ADELANTE!".center(60))
        return []
    
    top_puntuaciones_ordenado = sorted(top_puntuaciones, reverse=True, key=lambda puntuacion: puntuacion["puntuacion"])

    top = top_puntuaciones_ordenado[:10]

    print("\n" + "*" * 50)
    print("Top 10 Puntuaciones".center(50))
    print("*" * 50 + "\n")
    print("Posición".ljust(20) + "Usuario".ljust(20) + "Puntuación".ljust(10))
    for i in range(len(top)):
        print(f"{str(i + 1).ljust(20)}{top[i]['usuario'].ljust(20)}{str(top[i]['puntuacion']).ljust(10)}")

    return top

def configuracion_del_juego(configuracion_del_juego: dict) -> dict :
    '''
    ¿Que hace?: Modifica la configuracion default del juego
    ¿Que recibe?: El diccionario con la configuracion del juego
    ¿Que retorna?: La configuracion del juego actualizada
    '''

    while True:
        print("*" * 50)
        print("Configuración del juego".center(50))
        print("*" * 50 + "\n")
        print("A. Cambiar la cantidad de vidas")
        print("B. Cambiar la cantidad de puntos por respuesta correcta")
        print("C. Salir\n")
        
        
        opcion = str(input("Seleccione una opcion (A-C): ")).upper()
        
        if opcion == "A":
            while True:
                vidas_del_usuario = input("Ingrese la cantidad de puntos por respuesta correcta (1 o más): ")
                if vidas_del_usuario.isdigit():
                    vidas_del_usuario = int(vidas_del_usuario)
                    if vidas_del_usuario >= 1: 
                        configuracion_del_juego.update({"vidas": vidas_del_usuario})
                        break
                print("Entrada inválida. Por favor, ingrese un número entero mayor o igual a 1.")
               
        elif opcion == "B":
            while True:
                puntos_por_correcta = input("Ingrese la cantidad de puntos por respuesta correcta (1 o más): ")
                if puntos_por_correcta.isdigit():
                    puntos_por_correcta = int(puntos_por_correcta)
                    if puntos_por_correcta >= 1: 
                        configuracion_del_juego.update({"puntos_por_correcta": puntos_por_correcta})
                        break
                print("Entrada inválida. Por favor, ingrese un número entero mayor o igual a 1.")

            
        elif opcion == "C":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    
    return configuracion_del_juego

def menu_agregar_pregunta(preguntas: dict) -> dict:
    '''
    ¿Que hace?: Muestra el menu de agregar preguntas
    ¿Que recibe?: El diccionario con las preguntas
    ¿Que retorna?: El diccionario con las preguntas actualizado
    '''
    def cargar_preguntas():
            with open("./Parcial/Preguntados-Grupo-SDT/preguntas.json", "r") as archivo:
                return json.load(archivo).get("preguntas", {})
            
    def agregar_pregunta(preguntas:dict) -> dict:
        '''
        ¿Qué hace?: Solicita datos para agregar una nueva pregunta.
        ¿Qué recibe?: El diccionario con las preguntas actuales.
        ¿Qué retorna?: El diccionario con las preguntas actualizado.
        '''
        
        categoria = input("\nIngrese la categoría de la pregunta: ").strip()
        
        while categoria not in preguntas:
            print(f"La categoría '{categoria}' no existe. Intente nuevamente.")
            categoria = input("Ingrese la categoría de la pregunta: ").strip()

        
        pregunta_a_agregar = input("Ingrese la pregunta: ").strip()
        opcionA = input("Ingrese la opción A: ").strip()
        opcionB = input("Ingrese la opción B: ").strip()
        opcionC = input("Ingrese la opción C: ").strip()

        respuesta_correcta = input("Ingrese la respuesta correcta (A, B o C): ").strip().upper()
        while respuesta_correcta not in ["A", "B", "C"]:
            respuesta_correcta = input("Respuesta incorrecta. Por favor, ingrese la respuesta correcta (A, B o C): ").strip().upper()

        nueva_pregunta = {
            "pregunta": pregunta_a_agregar.title(),
            "opciones": [opcionA, opcionB, opcionC],
            "respuesta": respuesta_correcta
        }
        
        agregar_pregunta_a_archivo(categoria, nueva_pregunta)

    while True:
        print("*" * 60)
        print("Configuración de preguntas".center(60))
        print("*" * 60)
        print("\nA. Agregar nueva pregunta")
        print("B. Salir")
        
        opcion = str(input("\n" + " " * 16 + "Seleccione una opcion (A-B): ")).upper()
        
        if opcion == "A":
            preguntas = cargar_preguntas()
            agregar_pregunta(preguntas)
        elif opcion == "B":
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def dibujar_texto_multilinea(texto, x, y, max_ancho, fuente, pantalla, color_texto=(255, 255, 255)):
    """
    que hace: dibuja un texto con las espeficiaciones dadas
    que recibe:reciba las especificaciones de nuestro texto, como fuente, altura, ancho, etc
    que retorna:el texto como lo quiere el usuario
    """
    palabras = texto.split(' ')
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        if fuente.size(linea_actual + palabra)[0] < max_ancho:
            linea_actual += " " + palabra
        else:
            lineas.append(linea_actual)
            linea_actual = palabra

    if linea_actual:
        lineas.append(linea_actual)

    for i, linea in enumerate(lineas):
        texto_renderizado = fuente.render(linea, True, color_texto)
        pantalla.blit(texto_renderizado, (x, y + i * fuente.get_height()))


def agregar_top_diez(partida:dict) -> dict:
    """
    que hace: agregaria las partidas a un top 10 para guardar la puntuacion de cada usuario en un  json
    que recibe: recibe un cada partida como un dict 
    que retorna: retorna un diccionario (dict) con las partidas guardadas
    """
    import json

    archivo = './pygame/usuarios.json'
    with open(archivo, 'r') as arch:
        data = json.load(arch)
    
    top_puntuaciones = data["top_puntuaciones"]
    
    top_puntuaciones.append(partida)

    data["top_puntuaciones"] = top_puntuaciones
    with open(archivo, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)