import sqlite3
from colorama import init, Fore

init(autoreset=True)

def crear_base_de_datos():
    conn = sqlite3.connect("producto.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre    TEXT    NOT NULL,
            categoria TEXT    NOT NULL,
            precio    REAL    NOT NULL CHECK (precio >= 0),
            stock     INTEGER NOT NULL CHECK (stock >= 0)
        )
    """)
    conn.commit()
    conn.close()
    print(Fore.GREEN + "✅ Base de datos y tabla creadas correctamente.")

def agregar_producto(nombre, categoria, precio, stock):
    conn = sqlite3.connect("producto.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO productos (nombre, categoria, precio, stock)
        VALUES (?, ?, ?, ?)
    """, (nombre, categoria, precio, stock))
    conn.commit()
    conn.close()
    print(Fore.GREEN + "✅ Producto agregado correctamente.")

def listar_productos():
    conn = sqlite3.connect("producto.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return productos

def actualizar_producto(id, nombre, categoria, precio, stock):
    conn = sqlite3.connect("producto.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE productos
        SET nombre=?, categoria=?, precio=?, stock=?
        WHERE id=?
    """, (nombre, categoria, precio, stock, id))
    conn.commit()
    conn.close()
    print(Fore.GREEN + "✅ Producto actualizado correctamente.")

def eliminar_producto(id):
    conn = sqlite3.connect("producto.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id=?", (id,))
    conn.commit()
    conn.close()
    print(Fore.GREEN + "✅ Producto eliminado correctamente.")

# Ejecutamos la función
crear_base_de_datos()