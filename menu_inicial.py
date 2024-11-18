from funciones_generales import *
from manejo_de_usuarios import *
from file_system import *


datos = {"usuarios": [], "top_puntuaciones": []}




def menu():

    while True:
        print("\nMenú de opciones:")
        print("A. Registrarse")
        print("B. Iniciar partida")
        print("C. Ver top 10")
        print("D. Eliminar datos previos")
        print ("E. Salir")
        
        opcion = str(input("Seleccione una opción (A-E): ")).upper()
        
        if opcion == "A":
            crear_usuario("./Parcial/Preguntados-Grupo-SDT/usuarios.json", leer_datos())
            
        elif opcion == "B":
            #Iniciar partida
            iniciar_juego(iniciar_sesion(leer_datos()))
        elif opcion == "C":
            #Ver top10
            pass
        elif opcion == "D":
            eliminar_datos_previos("./Parcial/Preguntados-Grupo-SDT/usuarios.json", datos)
        elif opcion == "E":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
