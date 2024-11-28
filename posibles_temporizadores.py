#dos opciones para temporizador: 
#primera opcion
import time

def temporizador(duracion):
    print(f"El temporizador comenzó, durará {duracion} segundos.")
    tiempo_inicial = time.time()
    while True:
        tiempo_transcurrido = time.time() - tiempo_inicial
        if tiempo_transcurrido >= duracion:
            print(f"¡Tiempo cumplido! Han pasado {int(tiempo_transcurrido)} segundos.")
            break
        time.sleep(1)

temporizador(10)

#segunda opcion

import time


def contador_regresivo(segundos):
    while segundos > 0:
        print(f"Tiempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos -= 1
    print("¡Se acabó el tiempo!")
