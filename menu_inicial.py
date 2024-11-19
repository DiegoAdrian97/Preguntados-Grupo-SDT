from funciones_generales import *
from manejo_de_usuarios import *
from file_system import *


datos = {"usuarios": [], "top_puntuaciones": []}
configuracion = {"vidas":3, "puntos_por_correcta":25}

'''
Configuración del juego:
a. Dentro del menú principal, el usuario podrá acceder a un submenú que le permita modificar
la cantidad de puntos por respuesta correcta, la cantidad de vidas
'''


def menu():

    while True:
        print("\nMenú de opciones:")
        print("A. Registrarse")
        print("B. Iniciar partida")
        print("C. Ver top 10")
        print("D. Eliminar datos previos")
        print("E. Configuración del juego")
        print ("F. Salir")
        
        opcion = str(input("Seleccione una opción (A-E): ")).upper()
        
        if opcion == "A":
            crear_usuario(leer_datos())
        elif opcion == "B":
            #Iniciar partida
            iniciar_juego(iniciar_sesion(leer_datos()),puntos=0, vidas_del_usuario = configuracion["vidas"], puntos_por_correcta = configuracion["puntos_por_correcta"])
        elif opcion == "C":
            ver_top10(leer_datos())
            pass
        elif opcion == "D":
            eliminar_datos_previos("./Parcial/Preguntados-Grupo-SDT/usuarios.json", datos)
        elif opcion == "E":
            configuracion_del_juego(configuracion)
        elif opcion == "F":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
