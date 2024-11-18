from funciones_generales import *
from manejo_de_usuarios import *
from file_system import *


datos = {"usuarios": [], "top_puntuaciones": []}




def menu():

    while True:
        print("\nMenú de opciones:")
        print("1. Registrarse")
        print("2. Iniciar partida")
        print("3. Ver top 10")
        print("4. Eliminar datos previos")
        print ("5. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            nuevo_user = crear_usuario()
            datos["usuarios"].append(nuevo_user)
            
            guardar_datos("./Parcial/Preguntados-Grupo-SDT/usuarios.json", datos)
            
        elif opcion == 2:
            #Iniciar partida
            if iniciar_sesion(datos["usuarios"]):
                iniciar_juego()
            else:
                print("No se pudo iniciar la partida. Registrese primero")
            pass
        elif opcion == 3:
            #Ver top10
            pass
        elif opcion == 4:
            eliminar_datos_previos("./Parcial/Preguntados-Grupo-SDT/usuarios.json", datos)
        elif opcion == 5:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
