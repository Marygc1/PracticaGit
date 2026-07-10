diccionario = {
    "A": "Amor",
    "B": "Bondad",
    "C": "Confianza"
}

def obtener_significado(letra):
    """Accede al valor asociado a una letra"""
    return diccionaro[letra]

def agregar_letra(letra, significado):
    diccionario[letra] = significado
    return f"Agregada: {letra} -> {significado}"

def eliminar_letra(letra):
    """Elimina una letra si existe"""
    return diccionario.remove(letra)

def mostrar_diccionario():
    return diccionario

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Acceder a un valor")
        print("2. Agregar una letra")
        print("3. Eliminar una letra")
        print("4. Mostrar diccionario completo")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            letra = input("Ingresa la letra: ").upper()
            print(obtener_significado(letra))  # ❌ NameError por diccionaro

        elif opcion == "2":
            letra = input("Ingresa la letra: ").upper()
            significado = input("Ingresa el significado: ")
            print(agregar_letra(letra, significado))

        elif opcion == "3":
            letra = input("Ingresa la letra a eliminar: ").upper()
            print(eliminar_letra(letra))  # ❌ AttributeError por remove()

        elif opcion == "4":
            print("Diccionario actual:", mostrar_diccionario())

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida, intenta de nuevo.")

menu()
