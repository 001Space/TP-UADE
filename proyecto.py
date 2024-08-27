#Hacer un login usurarios/administradores
#Buscador de mercaderia
#Dentro del administrador, modificar y agregar productos, stock, stock en sucursarles
#Vendedores, sumar restar stock, carrito de compras, ejecutar carrito (suma de costo, resta de stock)
#Comision vendedores

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
            print("1. Registrar usuario")
            print("2. Eliminar usuario")
            print("3. Mostrar usuarios registrados")
            if usuario_actual == administrador["nombre"]:
                print("4. Modificar credenciales del administrador")
            print("5. Cerrar sesión")
            print("6. Salir")

            opcion = input("Seleccione una opción (1-6): ")

            if opcion == "1":
                registrar_usuario(usuario_actual)
            elif opcion == "2":
                eliminar_usuario(usuario_actual)
            elif opcion == "3":
                mostrar_usuarios(usuario_actual)
            elif opcion == "4" and usuario_actual == administrador["nombre"]:
                modificar_admin()
            elif opcion == "5":
                usuario_actual = None
                print("Sesión cerrada.")
            elif opcion == "6":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida, intente de nuevo.")

# Ejecutar el menú
menu()
