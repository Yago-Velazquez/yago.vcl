# Crear un diccionario para almacenar los datos de las personas
personas = {}

# Función para agregar una nueva persona
def agregar_persona():
    nombre = input("Ingrese el nombre de la persona: ")
    identificacion = input("Ingrese la identificación de la persona: ")

    # Almacenar la información en el diccionario
    personas[identificacion] = nombre
    print("Persona agregada exitosamente.")

# Función para mostrar todas las personas almacenadas
def mostrar_personas():
    print("\nLista de personas:")
    for identificacion, nombre in personas.items():
        print(f"Identificación: {identificacion}, Nombre: {nombre}")

# Menú principal
while True:
    print("\n1. Agregar persona")
    print("2. Mostrar personas")
    print("3. Salir")

    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == '1':
        agregar_persona()
    elif opcion == '2':
        mostrar_personas()
    elif opcion == '3':
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")