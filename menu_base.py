estudiantes = {
    "A01": ["Ana López", "Chile", "Programación"],
    "A02": ["Carlos Ruiz", "Argentina", "Matemáticas"]
}

def buscar_estudiante():
    codigo = input("Ingrese código del estudiante (ej: A01): ")
    if codigo in estudiantes:
        nombre, pais, curso = estudiantes[codigo]
        print("\n--- RESULTADO ---")
        print(f" Nombre: {nombre}")
        print(f" País: {pais}")
        print(f" Curso: {curso}")
    else:
        print(" Error: Código no encontrado")

# Menú base del programa
while True:
 print("\n--- MENÚ PRINCIPAL ---")
 print("1. Buscar estudiante por código")
 print("2. Función de integrante 2")
 print("0. Salir")
 op = input("Seleccione opción: ")
 if op == "0":
 print("Programa finalizado.")
 break
 elif op == "1":
      buscar_estudiante()
 elif op == "2":
 pass # Aquí se llamará a la función del integrante 2
 else:
 print(" Opción inválida.")
