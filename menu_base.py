    "A01": ["Ana López", "Chile", "Programación"],
    "A02": ["Carlos Ruiz", "Argentina", "Matemáticas"]
}

### Funciones a implementar (cada integrante hace UNA)
def buscar_estudiante():  # Integrante 1 (OPCIÓN 1)
    pass  # Reemplazar con código de búsqueda

def agregar_estudiante():  # Integrante 2 (OPCIÓN 2)
    pass  # Reemplazar con código de agregar

### Menú principal (adaptado a tu estructura)
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Buscar estudiante por código")  # Integrante 1
    print("2. Agregar nuevo estudiante")      # Integrante 2
    print("0. Salir")
    
    op = input("Seleccione opción: ")
    if op == "0":
        print("Programa finalizado.")
        break
    elif op == "1":
        buscar_estudiante()  # Función del Integrante 1
    elif op == "2":
        agregar_estudiante()  # Función del Integrante 2
    else:
        print("▲ Opción inválida.")def agregar_estudiante():
    codigo = input("Código nuevo (ej: A03): ")
    if codigo in estudiantes:
        print(" Error: Código ya existe")
    else:
        nombre = input("Nombre completo: ")
        pais = input("País: ")
        curso = input("Curso: ")
        estudiantes[codigo] = [nombre, pais, curso]
        print(f" {nombre} añadido/a exitosamente")
     
while True:
 print("\n--- MENÚ PRINCIPAL ---")
 print("1. Función de integrante 1")
 print("2. Función de integrante 2")
 print("3. Función de integrante 3")
 print("0. Salir")
 op = input("Seleccione opción: ")
 if op == "0":
 print("Programa finalizado.")
 break
 elif op == "1":
 pass # Aquí se llamará a la función del integrante 1
 elif op == "2":
 pass # Aquí se llamará a la función del integrante 2
 elif op == "3":
 pass # Aquí se llamará a la función del integrante 3
 else:
 print(" Opción inválida.")
