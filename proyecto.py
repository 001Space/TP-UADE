usuarios={}
administrador = {"nombre": "admin", "contrasena": "admin123"}
usuarios[administrador["nombre"]] = administrador["contrasena"]

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
            
            if usuario_actual == administrador["nombre"]:
                print("4. Modificar datos del administrador")
                print("5. Agregar/Modificar datos de productos")
                print("6. Registrar/modificar usuarios")
                
            print("7. Cerrar sesión")

            opcion = input("Seleccione una opción (1-7): ")



# Ejecutar el menú
menu()


def Registrar_usuario():
    pass

def Modificar_usuario():
    pass
    
def Registrar_producto():
    pass
    
def Modificar_producto():
    pass

def Factura():
    pass
    
def Cierre_contable():
    pass

def Buscador_usuarios():
    pass

def Buscador_productos():
    pass

def Modificacion_pago():
    pass

def datos_usuario():
    pass
    
#funciones lambda para descuentos y recargos en la factura
descuento = lambda x, y: x * y
recargo = lambda x, z: x * z


