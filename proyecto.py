#Trabajo practico GRUPO 8


#Variables externas
usuarios = {
    "admin": "admin123",
    "juan": "juan123",
}
administrador = {"nombre": "admin", "contrasena": "admin123"}
productos = []

#Inicio de sesion, verifica usuarios
def iniciar_sesion():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if nombre_usuario in usuarios and usuarios[nombre_usuario] == contrasena:
        print(f"Inicio de sesión exitoso. Bienvenido, {nombre_usuario}.")
        return nombre_usuario
    else:
        print("Nombre de usuario o contraseña incorrectos.")
        return None

# Menú principal
def menu():
    usuario_actual = None
#While verifica que el usuario actual y la contraseña coinciden 

    while True:
        if usuario_actual is None:
            print("\n--- Menú de inicio de sesión ---")
            print("1. Iniciar sesión")
            print("2. Salir")
            opcion = input("Seleccione una opción (1-2): ")

            if opcion == "1":
                usuario_actual = iniciar_sesion()
            elif opcion == "2":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida, intente de nuevo.")
        else:
            print(f"\n--- Menú principal (Usuario actual: {usuario_actual}) ---")
            print("1. Mostrar usuarios registrados")
            print("2. Buscar productos")
            print("3. Cargar venta")
#Si el usuario es el administrador podra ver mas opciones            
            if usuario_actual == administrador["nombre"]:
                print("4. Modificar datos del administrador")
                print("5. Agregar/Modificar datos de productos")
                print("6. Registrar/Modificar usuarios")
                
            print("7. Cerrar sesión")

            opcion = input("Seleccione una opción (1-7): ")
#Seleccion de opciones del menu
            if opcion == "1":
                mostrar_usuarios()
            elif opcion == "2":
                nombre_producto = input("Ingrese el nombre del producto a buscar: ")
                buscadorProductos(productos, nombre_producto)
            elif opcion == "3":
                pass
            elif opcion == "4" and usuario_actual == administrador["nombre"]:
                pass
            elif opcion == "5" and usuario_actual == administrador["nombre"]:
                Registrar_producto(productos)
            elif opcion == "6" and usuario_actual == administrador["nombre"]:
                registrarusuario()
            elif opcion == "7":
                usuario_actual = None
                print("Sesión cerrada.")
            else:
                print("Opción no válida.")
#Definimos mostrar usuarios
def mostrar_usuarios():
    print("\n--- Usuarios registrados ---")
    for usuario in usuarios:
        print(f"Usuario: {usuario}")
#Definimos como registrar usuarios
def registrarusuario():
    nombre = input("Ingrese el nombre del usuario: ")
    contraseña = input("Ingrese una contraseña: ")

    if nombre in usuarios:
        print("El usuario ya existe.")
    else:
        usuarios[nombre] = contraseña
        print("Usuario registrado con éxito.")
#Definimos como registrar productos
def Registrar_producto(productos):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    codigo = input("Ingrese el código del producto: ")
    
    nuevo_producto = {
        "nombreProducto": nombre,
        "precio": precio,
        "cantidadStock": cantidad,
        "ID": codigo
    }
    
    productos.append(nuevo_producto)
    print(f"Producto {nombre} registrado correctamente.")
#Definimos como buscar productos
def buscadorProductos(productos, nombre):
    nombre = nombre.upper()
    encontrado = False

    for producto in productos:
        if nombre in producto["nombreProducto"].upper():
            print(f"Producto encontrado: {producto}")
            encontrado = True
    
    if not encontrado:
        print(f"Producto {nombre} no encontrado.")
        
#Funciones a desarrollar en la siguiente entrega

def modificarProducto():
    pass

def modifcarUsuario():
    pass

def facturacion():
    pass

def modAdmin():
    pass

def modDescuentos():
    pass

#Funcion descuentos a desarrolar en lambda
descuento = lambda x, y: x * y
recargo = lambda x, z: x * z
# Ejecutar el menú
menu()
