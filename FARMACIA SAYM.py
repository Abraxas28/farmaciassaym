import tkinter as tk
from tkinter import messagebox

# Colores para la app
COLOR_FONDO = "#e3f2fd"        # Azul claro
COLOR_BOTON = "#1976d2"        # Azul fuerte
COLOR_BOTON_TEXTO = "#ffffff"  # Blanco
COLOR_ENTRADA = "#bbdefb"      # Azul muy claro
COLOR_LISTA = "#90caf9"        # Azul intermedio
COLOR_TITULO = "#0d47a1"       # Azul oscuro

# Listado de los productos y sus precios
productos = {
    "Paracetamol": 70,
    "Loratadina": 60,
    "Omeprazol": 56,
    "Termisatan": 120,
    "Butilhiosina": 67,
    "Dextametazona": 80,
    "Montelukast": 50,
    "Sterimar": 100,
    "Diclofenaco": 45,
    "Aspirina": 150,
    "Sitaglipina": 45,
    "Naproxeno": 45,
    "Metamizol Sodico": 45,
    "Sal de uvas": 45,
    "Gabapentina": 44,
    "Piroxican": 43,
    "Ketorolaco": 67,
    "Insulina": 55,
    "Cetriaxona": 82,
    "Trimebutina": 90
}

# Variables globales para guardar los datos del usuario
usuario = {}

def abrir_ventana_productos():
    usuario["nombre"] = entry_nombre.get().strip()
    usuario["edad"] = entry_edad.get().strip()
    usuario["fecha_nacimiento"] = entry_fecha.get().strip()
    usuario["direccion"] = entry_direccion.get().strip()

    if not usuario["nombre"] or not usuario["edad"] or not usuario["fecha_nacimiento"] or not usuario["direccion"]:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    ventana_registro.withdraw()
    ventana_productos.deiconify()



def calcular_total():
    productos_ingresados = text_productos.get("1.0", tk.END).strip().split("\n")
    total = 0
    for producto in productos_ingresados:
        producto = producto.strip().lower()
        if producto in map(str.lower, productos.keys()):
            producto_original = next(key for key in productos if key.lower() == producto)
            total += productos[producto_original]
        elif producto:
            messagebox.showwarning("Advertencia", f"El producto '{producto}' no está en la lista.")

    resultado = (
        f"Nombre: {usuario['nombre']}\n"
        f"Edad: {usuario['edad']}\n"
        f"Fecha de nacimiento: {usuario['fecha_nacimiento']}\n"
        f"Dirección de envío: {usuario['direccion']}\n"
        f"Total: ${total}"
    )
    messagebox.showinfo("Resultado", resultado)

# --------- Ventana de Registro ---------
ventana_registro = tk.Tk()
ventana_registro.title("Registro - FARMACIA SAYM")
ventana_registro.geometry("600x370")
ventana_registro.configure(bg=COLOR_FONDO)


titulo = tk.Label(
    ventana_registro, text="FARMACIA SAYM",
    font=("Arial", 28, "bold"),
    fg=COLOR_TITULO, bg=COLOR_FONDO
)
titulo.pack(pady=20)

frame_registro = tk.Frame(ventana_registro, bg=COLOR_FONDO)
frame_registro.pack(pady=10)

tk.Label(frame_registro, text="Nombre:", font=("Arial", 14), bg=COLOR_FONDO).grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nombre = tk.Entry(frame_registro, font=("Arial", 14), bg=COLOR_ENTRADA)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_registro, text="Edad:", font=("Arial", 14), bg=COLOR_FONDO).grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_edad = tk.Entry(frame_registro, font=("Arial", 14), bg=COLOR_ENTRADA)
entry_edad.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_registro, text="Fecha de nacimiento (DD/MM/AAAA):", font=("Arial", 14), bg=COLOR_FONDO).grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_fecha = tk.Entry(frame_registro, font=("Arial", 14), bg=COLOR_ENTRADA)
entry_fecha.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame_registro, text="Dirección de envío:", font=("Arial", 14), bg=COLOR_FONDO).grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_direccion = tk.Entry(frame_registro, font=("Arial", 14), bg=COLOR_ENTRADA)
entry_direccion.grid(row=3, column=1, padx=10, pady=5)

boton_siguiente = tk.Button(
    ventana_registro, text="Siguiente", font=("Arial", 14),
    command=abrir_ventana_productos,
    bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, activebackground=COLOR_TITULO
)
boton_siguiente.pack(pady=20)

# --------- Ventana de Productos ---------
ventana_productos = tk.Toplevel()
ventana_productos.title("Selecciona tus productos - FARMACIA SAYM")
ventana_productos.geometry("900x500")
ventana_productos.configure(bg=COLOR_FONDO)
ventana_productos.withdraw()  # Ocultar hasta que se registre el usuario

# ...existing code...

label_productos = tk.Label(
    ventana_productos, text="Productos (uno por línea):",
    font=("Arial", 14), bg=COLOR_FONDO, fg=COLOR_TITULO
)
label_productos.grid(row=0, column=0, padx=10, pady=5, sticky="w")
text_productos = tk.Text(
    ventana_productos, height=15, width=40, font=("Arial", 12), bg=COLOR_ENTRADA
)
text_productos.grid(row=1, column=0, padx=10, pady=5, rowspan=4)

label_lista = tk.Label(
    ventana_productos, text="Productos disponibles:",
    font=("Arial", 14), bg=COLOR_FONDO, fg=COLOR_TITULO
)
label_lista.grid(row=0, column=1, padx=10, pady=5, sticky="w")
listbox_productos = tk.Listbox(
    ventana_productos, height=20, width=40, font=("Arial", 12), bg=COLOR_LISTA
)
listbox_productos.grid(row=1, column=1, rowspan=4, padx=10, pady=5, sticky="n")

for producto, precio in productos.items():
    listbox_productos.insert(tk.END, f"{producto}: ${precio}")

# Añadir scroll a la lista de productos
scrollbar = tk.Scrollbar(ventana_productos)

def agregar_producto_a_texto(event):
    seleccion = listbox_productos.curselection()
    if seleccion:
        producto = listbox_productos.get(seleccion[0]).split(":")[0]
        # Agrega el producto en una nueva línea
        contenido_actual = text_productos.get("1.0", tk.END).strip()
        if contenido_actual:
            text_productos.insert(tk.END, f"\n{producto}")
        else:
            text_productos.insert(tk.END, producto)

listbox_productos.bind("<Double-Button-1>", agregar_producto_a_texto)

boton_calcular = tk.Button(
    ventana_productos, text="Calcular Total", font=("Arial", 14),
    command=calcular_total,
    bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, activebackground=COLOR_TITULO
)
boton_calcular.grid(row=5, column=0, columnspan=2, pady=20)

ventana_registro.mainloop()