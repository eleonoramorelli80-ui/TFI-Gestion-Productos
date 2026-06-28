import base_de_datos
import usuario
from colorama import init, Fore

init(autoreset=True)

# Creamos la base de datos al iniciar
base_de_datos.crear_base_de_datos()

while True:
    print(Fore.YELLOW + "\n╔══════════════════════════════╗")
    print(Fore.YELLOW + "║    GESTIÓN DE PRODUCTOS      ║")
    print(Fore.YELLOW + "╠══════════════════════════════╣")
    print(Fore.YELLOW + "║  1. Agregar producto         ║")
    print(Fore.YELLOW + "║  2. Ver productos            ║")
    print(Fore.YELLOW + "║  3. Actualizar producto      ║")
    print(Fore.YELLOW + "║  4. Eliminar producto        ║")
    print(Fore.YELLOW + "║  5. Salir                    ║")
    print(Fore.YELLOW + "╚══════════════════════════════╝")

    opcion = input(Fore.YELLOW + "  Elegí una opción: ")

    if opcion == "1":
        datos = usuario.pedir_producto()
        base_de_datos.agregar_producto(*datos)

    elif opcion == "2":
        productos = base_de_datos.listar_productos()
        usuario.mostrar_productos(productos)

    elif opcion == "3":
        productos = base_de_datos.listar_productos()
        usuario.mostrar_productos(productos)
        id = usuario.pedir_id()
        datos = usuario.pedir_producto()
        base_de_datos.actualizar_producto(id, *datos)

    elif opcion == "4":
        productos = base_de_datos.listar_productos()
        usuario.mostrar_productos(productos)
        id = usuario.pedir_id()
        base_de_datos.eliminar_producto(id)

    elif opcion == "5":
        print(Fore.GREEN + "👋 ¡Hasta luego!")
        break

    else:
        print(Fore.RED + "❌ Opción inválida. Elegí un número del 1 al 5.")