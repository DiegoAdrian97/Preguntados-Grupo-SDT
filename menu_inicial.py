from funciones import *


def menu():

    while True:
        print("\nMenú de opciones:")
        print("1. Iniciar partida")
        print("2. Ver top 10 puntuaciones")
        print("3. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            #iniciar partida
            pass
        elif opcion == 2:
            #Ver top10
            pass
        elif opcion == 3:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
