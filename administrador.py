from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table

console = Console()

# Función para cargar los datos del administrador desde el archivo CSV
def cargar_datos_administrador():
    try:
        with open("administrador.csv", "r") as archivo:
            nombre, contrasena = archivo.readline().strip().split(",")
            return {"nombre": nombre, "contrasena": contrasena}
    except FileNotFoundError:
        console.print("[bold red]Archivo de administrador no encontrado, se cargarán valores por defecto.[/bold red]")
        return {"nombre": "admin", "contrasena": "admin123"}  # Valores por defecto
    except Exception as e:
        console.print(f"[bold red]Error al leer el archivo del administrador: {str(e)}[/bold red]")
        return {"nombre": "admin", "contrasena": "admin123"}

# Función para guardar los datos del administrador en el archivo CSV
def guardar_datos_administrador(administrador):
    with open("administrador.csv", "w") as archivo:
        archivo.write(f"{administrador['nombre']},{administrador['contrasena']}\n")
    console.print(f"[bold green]Datos del administrador actualizados correctamente.[/bold green]")

# Inicializar el archivo del administrador si no existe
def inicializar_administrador():
    administrador = cargar_datos_administrador()
    if administrador['nombre'] == 'admin' and administrador['contrasena'] == 'admin123':
        guardar_datos_administrador(administrador)
        console.print("[bold green]Archivo del administrador creado con valores por defecto.[/bold green]")

# Función para modificar datos del administrador
def modificar_datos_administrador():
    administrador = cargar_datos_administrador()
    console.print(Panel("[bold cyan]--- Modificar Datos del Administrador ---[/bold cyan]", expand=False))

    nuevo_nombre = input("Ingrese el nuevo nombre (o presione Enter para no cambiar): ")
    nuevo_contrasena = input("Ingrese la nueva contraseña (o presione Enter para no cambiar): ")

    if nuevo_nombre:
        administrador["nombre"] = nuevo_nombre
    if nuevo_contrasena:
        administrador["contrasena"] = nuevo_contrasena

    guardar_datos_administrador(administrador)
