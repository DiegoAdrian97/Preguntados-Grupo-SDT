from funciones_generales import *
from file_system import *


datos = {"top_puntuaciones": []}
configuracion = {    
    "vidas": 3,
    "puntos_por_correcta": 25
}

def menu():
    while True:
        print("\n")
        print("*" * 60)
        print("*" + " " * 15 + "Bienvenidos a Descerebrados" + " " * 15 + "*")
        print("*" * 60)
        print("\n" + " " * 22 + "Menú de opciones: \n")
        print("A. Iniciar Partida".center(60))
        print("B. Ver top 10".center(60))
        print("C. Eliminar datos previos".center(60))
        print("D. Configuración del juego".center(60))
        print("E. Agregar pregunta nueva".center(60))
        print("F. Salir".center(60))
        
        opcion = str(input("\nSeleccione una opción (A-G): ")).upper()
        
        if opcion == "A":
            print("\n")
            iniciar_juego(leer_datos(), cargar_preguntas(), puntos=0, vidas_del_usuario = configuracion["vidas"], puntos_por_correcta = configuracion["puntos_por_correcta"])
        elif opcion == "B":
            print("\n")
            ver_top10(leer_datos())
        elif opcion == "C":
            print("\n")
            print("*" * 60)            
            print("LEA ATENTAMENTE. NO HAY VUELTA ATRAS".center(60))
            print("*" * 60)
            
            print("\n" + "Está a punto de eliminar las puntuaciones guardadas.".center(60))
            decision_borrar = input("\n" + " " * 14 + "Desea continuar: (SI / NO) ").upper()
            while decision_borrar != "SI" and decision_borrar != "NO":
                print("\n" + "Está a punto de eliminar las puntuaciones guardadas.".center(60))
                decision_borrar = input("\n" + " " * 11 + "Elija una de estas opciones: (SI / NO) ").upper()
            
            if decision_borrar == "SI":
                eliminar_datos_previos(datos)
            else:
                print("\n" + "Menos mal que pregunte!".center(60))
    
        elif opcion == "D":
             print("\n")
             configuracion_del_juego(configuracion)
        elif opcion == "E":
           print("\n")
           menu_agregar_pregunta(cargar_preguntas())
        elif opcion == "F":
            print("\n")
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
menu()