from funciones_generales import *
from manejo_de_usuarios import *

lista_usuarios = []

def menu():

    while True:
        print("\nMenú de opciones:")
        print("1. Registrarse")
        print("2. Iniciar partida")
        print("3. Ver top 10")
        print("4. Ver respuesta")
        print ("5. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            crear_usuario(lista_usuarios)
            resultado = iniciar_sesion(lista_usuarios)
            print(resultado)
            
        elif opcion == 2:
            #Iniciar partida
            if iniciar_sesion(lista_usuarios):
                categoria, pregunta = elegir_pregunta_aleatoria()
                print("Categoria: ", categoria)
                mostrar_pregunta(pregunta)
            else:
                print("No se pudo iniciar la partida. Registrese primero")
            pass
        elif opcion == 3:
            #Ver top10
            pass
        elif opcion == 4:
            #Ver respuesta
            pass
        elif opcion == 5:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
