import json

def leer_datos() -> dict:  
    '''
        ¿Que hace?: Lee los datos de los usuarios, y sus puntuaciones
        ¿Que recibe?: El JSON con los datos de los usuarios
        ¿Que retorna?: Diccionario con los usuarios leidos
    '''
    with open("./Parcial/Preguntados-Grupo-SDT/usuarios.json", "r") as archivo:
        users_data = json.load(archivo)
    return users_data
    
def guardar_datos(datos: dict) -> str:
    '''
        ¿Que hace?: Guarda los datos del nuevo usuario creado
        ¿Que recibe?: El JSON con los datos de los usuarios, los datos del nuevo usuario
        ¿Que retorna?: Nada.
    '''
    with open("./Parcial/Preguntados-Grupo-SDT/usuarios.json", "w") as archivo:
        json.dump(datos, archivo)

def eliminar_datos_previos(archivo_json: str, datos: dict) -> str:
    '''
        ¿Que hace?: Elimina los usuarios creados previamente
        ¿Que recibe?: El JSON de los usuarios y el diccionario datos vacío.
        ¿Que retorna?: Mensaje de OK
    '''
    with open(archivo_json, "w") as archivo:
        json.dump(datos, archivo)
        
    mensaje = print("Usuarios eliminados con exito")
    
    return mensaje