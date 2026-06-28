# 🛒 Sistema de Gestión de Productos

Trabajo Final Integrador — Curso Iniciación a la Programación con Python  
**Talento Tech** | Buenos Aires Ciudad · Ministerio de Educación GCBA

---

## 📋 Descripción

Sistema de gestión de productos desarrollado en Python con base de datos SQLite. Permite registrar, consultar, modificar y eliminar productos desde una interfaz de menú en consola, con salidas en color mediante Colorama.

---

## ⚙️ Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python 3 | Lenguaje principal |
| SQLite3 | Base de datos local |
| Colorama | Colores en consola |
| VS Code | Entorno de desarrollo |

---

## 📁 Estructura de archivos

```
TFI/
│
├── base_de_datos.py   # Conexión a SQLite y operaciones CRUD
├── usuario.py         # Interacción con el usuario (inputs y validaciones)
├── main.py            # Menú principal y flujo del programa
└── producto.db        # Base de datos (se genera automáticamente)
```

---

## 🗄️ Estructura de la base de datos

**Tabla:** `productos`

| Campo | Tipo | Restricción |
|---|---|---|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| nombre | TEXT | NOT NULL |
| categoria | TEXT | NOT NULL |
| precio | INTEGER | NOT NULL, mayor a 0 |
| stock | INTEGER | NOT NULL, mayor a 0 |

---

## ▶️ Cómo ejecutarlo

### 1. Requisitos previos

Tener instalado Python 3 y Colorama. Si no tenés Colorama:

```bash
pip install colorama
```

### 2. Clonar o descargar el proyecto

Copiá los tres archivos `.py` en una misma carpeta.

### 3. Ejecutar el programa

Abrí la terminal, posicionarte en la carpeta del proyecto y ejecutar:

```bash
cd C:\Users\ELEO\Desktop\26101_Python\TFI
python main.py
```

La base de datos `producto.db` se crea automáticamente en la primera ejecución.

---

## 🧭 Cómo usarlo

Al ejecutar `main.py` aparece el siguiente menú:

```
╔══════════════════════════════╗
║    GESTIÓN DE PRODUCTOS      ║
╠══════════════════════════════╣
║  1. Agregar producto         ║
║  2. Ver productos            ║
║  3. Actualizar producto      ║
║  4. Eliminar producto        ║
║  5. Salir                    ║
╚══════════════════════════════╝
```

### Opciones disponibles

**1. Agregar producto** — Solicita nombre, categoría, precio y stock. Valida que los datos sean correctos antes de guardar.

**2. Ver productos** — Muestra todos los productos registrados en formato tabla.

**3. Actualizar producto** — Muestra el listado, solicita el ID del producto a modificar y permite editar todos sus campos.

**4. Eliminar producto** — Muestra el listado y solicita el ID del producto a eliminar.

**5. Salir** — Cierra el programa.

---

## ✅ Validaciones implementadas

- El nombre y la categoría se guardan automáticamente con la primera letra en mayúscula, sin importar cómo los escriba el usuario
- El precio debe ser un número entero mayor a cero (no acepta decimales)
- El stock debe ser un número entero mayor a cero
- Si el dato ingresado es incorrecto, el programa lo vuelve a pedir

---

## 🎨 Código de colores en consola

| Color | Significado |
|---|---|
| 🟢 Verde | Operación exitosa |
| 🟡 Amarillo | Menú, información y listados |
| 🔴 Rojo | Errores y datos inválidos |

---

## 👩‍💻 Autora

**Eleonora Morelli**  
Talento Tech · 2026