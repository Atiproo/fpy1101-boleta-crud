import os

# Estructura de datos original
boleta = []

def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = int(input("Precio: "))
    boleta.append({"nombre": nombre, "precio": precio})
    print(f"Producto '{nombre}' agregado.")

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
    nuevo_precio = int(input("Nuevo precio: "))
    for p in boleta:
        if p['nombre'] == nombre:
            p['precio'] = nuevo_precio
            print("Precio actualizado.")
            return
    print("Producto no encontrado.")

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    for p in boleta:
        if p['nombre'] == nombre:
            boleta.remove(p)
            print("Producto eliminado.")
            return
    print("Producto no encontrado.")

# Menú interactivo
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
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")