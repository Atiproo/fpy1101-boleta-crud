import os

# Estructura de datos original
boleta = []

def agregar_producto():
    nombre = input("Nombre del producto: ")
    
    # V1: Validar que el nombre no esté vacío
    if not nombre.strip():
        print("Error: El nombre del producto no puede estar vacío.")
        return

    # V4: Validar que no se agregue un producto duplicado (ignorando mayúsculas/minúsculas)
    for p in boleta:
        if p['nombre'].lower() == nombre.lower():
            print("Error: El producto ya existe en la boleta.")
            return

    # V3: Validar que el precio tenga formato numérico válido (try/except)
    try:
        precio = int(input("Precio: "))
        
        # V2: Validar que el precio sea mayor que cero
        if precio <= 0:
            print("Error: El precio debe ser mayor que cero.")
            return
            
        boleta.append({"nombre": nombre, "precio": precio})
        print(f"Producto '{nombre}' agregado correctamente.")
        
    except ValueError:
        print("Error: El precio debe ser un número entero.")

def mostrar_boleta():
    if not boleta:
        print("La boleta está vacía.")
    else:
        print("\n--- BOLETA ---")
        total = 0
        for p in boleta:
            print(f"{p['nombre']} - ${p['precio']}")
            total += p['precio']
        print(f"TOTAL: ${total}")

def actualizar_precio():
    nombre = input("Nombre del producto a actualizar: ")
    
    try:
        nuevo_precio = int(input("Nuevo precio: "))
        
        # V2: Validar precio mayor a cero al actualizar
        if nuevo_precio <= 0:
            print("Error: El precio debe ser mayor que cero.")
            return
            
        for p in boleta:
            if p['nombre'].lower() == nombre.lower():
                p['precio'] = nuevo_precio
                print("Precio actualizado correctamente.")
                return
        print("Producto no encontrado.")
        
    except ValueError:
        print("Error: El precio debe ser un número entero.")

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    for p in boleta:
        if p['nombre'].lower() == nombre.lower():
            boleta.remove(p)
            print("Producto eliminado correctamente.")
            return
    print("Producto no encontrado.")

# Menú principal
while True:
    print("\n--- MENÚ ---")
    print("1) Agregar producto")
    print("2) Mostrar boleta")
    print("3) Actualizar precio")
    print("4) Eliminar producto")
    print("5) Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_boleta()
    elif opcion == "3":
        actualizar_precio()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción inválida.")