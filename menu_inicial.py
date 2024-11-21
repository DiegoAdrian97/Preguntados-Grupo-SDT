from funciones_generales import *
from manejo_de_usuarios import *
from file_system import *


datos = {"usuarios": [], "top_puntuaciones": []}
configuracion = {    
    "vidas": 3,
    "puntos_por_correcta": 2
}

def menu():
    while True:
        print("\nMenú de opciones:")
        print("A. Iniciar Partida")
        print("B. Ver top 10")
        print("C. Eliminar datos previos")
        print("D. Configuración del juego")
        print("E. Agregar pregunta nueva")
        print("F. Salir")
        
        opcion = str(input("Seleccione una opción (A-G): ")).upper()
        
        if opcion == "A":
            iniciar_juego(leer_datos(), puntos=0, vidas_del_usuario = configuracion["vidas"], puntos_por_correcta = configuracion["puntos_por_correcta"])
        elif opcion == "B":
            ver_top10(leer_datos())
        elif opcion == "C":
            eliminar_datos_previos("./Parcial/Preguntados-Grupo-SDT/usuarios.json", datos)
        elif opcion == "D":
             configuracion_del_juego(configuracion)
        elif opcion == "E":
           menu_agregar_pregunta(cargar_preguntas())
        elif opcion == "F":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
menu()