from colorama import init, Fore

init(autoreset=True)

def pedir_producto():
    # Nombre — el programa pone la mayúscula solo
    nombre = input(Fore.YELLOW + "  Nombre: ").strip().capitalize()

    # Categoría — el programa pone la mayúscula solo
    categoria = input(Fore.YELLOW + "  Categoría: ").strip().capitalize()

    # Validar precio — sin decimales, mayor a cero
    while True:
        try:
            precio = int(input(Fore.YELLOW + "  Precio (sin decimales): "))
            if precio <= 0:
                print(Fore.RED + "❌ El precio debe ser mayor a cero.")
            else:
                break
        except ValueError:
            print(Fore.RED + "❌ El precio debe ser un número entero. Ejemplo: 1500")

    # Validar stock — sin decimales, mayor a cero
    while True:
        try:
            stock = int(input(Fore.YELLOW + "  Stock: "))
            if stock <= 0:
                print(Fore.RED + "❌ El stock debe ser mayor a cero.")
            else:
                break
        except ValueError:
            print(Fore.RED + "❌ El stock debe ser un número entero.")

    return nombre, categoria, precio, stock

def pedir_id():
    id = int(input(Fore.YELLOW + "  Ingresá el ID del producto: "))
    return id

def mostrar_productos(productos):
    if not productos:
        print(Fore.YELLOW + "⚠️  No hay productos cargados.")
    else:
        print(Fore.YELLOW + "\n📦 Lista de productos:")
        print(Fore.YELLOW + "-" * 55)
        for p in productos:
            print(Fore.YELLOW + f"  ID: {p[0]} | {p[1]} | {p[2]} | ${p[3]} | Stock: {p[4]}")
        print(Fore.YELLOW + "-" * 55)