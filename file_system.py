import json

with open("./Parcial/Preguntados-Grupo-SDT/usuarios.json", "r") as archivo:
    users_data = json.load(archivo)
    
def guardar_datos(archivo_json, datos):
    with open(archivo_json, "w") as archivo:
        json.dump(datos, archivo)

def eliminar_datos_previos(archivo_json, datos):
    with open(archivo_json, "w") as archivo:
        json.dump(datos, archivo)