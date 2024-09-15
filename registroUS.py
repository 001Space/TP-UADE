usuarios = []

#Registro de nuevo usuario
def registrarusuario():
    idusuario = input("Ingrese un ID de usuario: ")
    nombre = input("Ingrese el nombre del usuario: ")
    contraseña = input("Ingrese una contraseña: ")

    #Diccioanrio con los datos
    usuario = {
        'id': idusuario,
        'nombre': nombre,
        'contraseña': contraseña
    }

    usuarios.append(usuario)
    print("Usuario registrado con éxito.")


def mostrarusuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    #Muestra  los usuarios registrados
    print("Usuarios registrados:")
    for usuario in usuarios:
        print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}")
