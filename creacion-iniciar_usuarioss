lista_usuario = []

def crear_usuario(lista: list) -> dict:
    """
    ¿Qué hace?: permite al usuario crear un usuario y contraseña para ingresar al sistema.
    ¿Qué recibe?: Recibe una lista que contendrá los datos del usuario en modo diccionario.
    ¿Qué retorna?: Retorna el diccionario con los datos de los usuarios.
    """
    print("Debes tener en cuenta que tu nuevo usuario y contraseña deben contener mínimo 8 caracteres y no caracteres especiales.")
    
    nombre = input("Ingrese el nombre de usuario: ")
    while not nombre.isalnum() or len(nombre) < 8:  
        if len(nombre) < 8:
            nombre = input("Debe contener más de 8 caracteres, intente nuevamente: ")
        else:
            nombre = input("Intente nuevamente, el nombre debe ser alfanumérico: ")

    contraseña = input("Ingresa la contraseña del usuario: ")
    while not contraseña.isalnum() or len(contraseña) < 8: 
        if len(contraseña) < 8:
            contraseña = input("La contraseña debe contener más de 8 caracteres, intente nuevamente: ")
        else:
            contraseña = input("No se permiten caracteres especiales, intente nuevamente: ")
    
    usuario = {
        "nombre": nombre,
        "contraseña": contraseña
    }
    
    lista.append(usuario)

    
def iniciar_sesion(lista: list) -> str:
    """
    ¿Qué hace?: Permite al usuario intentar iniciar sesión con su nombre de usuario y contraseña.
    ¿Qué recibe?: Recibe la lista de usuarios creada por la función crear_usuario.
    ¿Qué retorna?: Retorna un mensaje dependiendo si el inicio de sesión fue exitoso o no.
    """
    nombre = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    for usuario in lista:
        while usuario["nombre"] != nombre:
            nombre = input("Usuario incorrecto, intente nuevamente: ")
            while usuario["contraseña"] != contraseña:
                contraseña = input("Contraseña incorrecta, intente nuevamente: ")
        print("se inicio sesion correctamente")

        


crear_usuario(lista_usuario)
resultado = iniciar_sesion(lista_usuario)
print(resultado)
