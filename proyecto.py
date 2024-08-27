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
