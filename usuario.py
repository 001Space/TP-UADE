from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table

console = Console()

def cargar_usuarios():
    usuarios = []
    try:
        with open("usuarios.csv", "rt") as archivo_usuarios:
            for linea in archivo_usuarios:
                campos = linea.strip().split(",")
                if len(campos) == 3:
                    nombre, contrasena, legajo = campos
                    usuarios.append([nombre, contrasena, int(legajo)])
                else:
                    console.print(f"[bold red]Línea ignorada por formato incorrecto: {linea.strip()}[/bold red]")
    except FileNotFoundError:
        console.print("[bold red]Archivo de usuarios no encontrado.[/bold red]")
    return usuarios

# Función para guardar usuarios en el archivo CSV
def guardar_usuarios(usuarios):
    with open("usuarios.csv", "w") as archivo_usuarios:
        for usuario in usuarios:
            archivo_usuarios.write(f"{usuario[0]},{usuario[1]},{usuario[2]}\n")

# Función para mostrar todos los usuarios registrados
def mostrar_usuarios():
    usuarios = cargar_usuarios()
    if not usuarios:
        console.print("[bold red]No hay usuarios registrados.[/bold red]")
        return

    tabla = Table(title="Usuarios Registrados")
    tabla.add_column("Nombre", style="cyan", justify="center")
    tabla.add_column("Legajo", style="magenta", justify="center")

    for usuario in usuarios:
        tabla.add_row(usuario[0], str(usuario[2]))

    console.print(tabla)


# Función para registrar un usuario
def registrarusuario():
    usuarios = cargar_usuarios()
    nombre = input("Ingrese el nombre del usuario: ")
    contraseña = input("Ingrese una contraseña: ")
    legajo = int(input("Ingrese el número de legajo del usuario: "))

    for usuario in usuarios:
        if usuario[0] == nombre:
            console.print("[bold red]El usuario ya existe.[/bold red]")
            return

    nuevo_usuario = [nombre, contraseña, legajo]
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)
    console.print("[bold green]Usuario registrado con éxito.[/bold green]")

# Función para eliminar un usuario
def eliminar_usuario():
    usuarios = cargar_usuarios()
    nombre_usuario = input("Ingrese el nombre del usuario a eliminar: ")

    for usuario in usuarios:
        if usuario[0] == nombre_usuario:
            usuarios.remove(usuario)
            guardar_usuarios(usuarios)
            console.print(f"[bold green]Usuario {nombre_usuario} eliminado con éxito.[/bold green]")
            return

    console.print("[bold red]Usuario no encontrado.[/bold red]")