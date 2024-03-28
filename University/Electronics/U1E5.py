# Base de datos:
datos = {}

while True:
    eleccion = int(input("Elige una opción\n" "1. Añadir cliente\n" "2. Eliminar cliente\n"
                         "3. Mostrar cliente\n" "4. Mostrar clientes\n" "5. Mostrar clientes preferentes\n"
                         "6. Terminar\n"))

    if eleccion == 1:
        nif = str(input("NIF: "))
        nombre = str(input("Nombre: "))
        tlf = str(input("Teléfono: "))
        correo = str(input("Correo: "))
        dire = str(input("Dirección: "))
        vip = str(input("Preferente (S/N): "))
        if vip == "S":
            vip = True
        else:
            vip = False
        datos[nif] = {"NIF": nif, "Nombre": nombre, "Teléfono": tlf, "Correo": correo, "Dirección": dire, "Preferente": vip}
        print("Cliente agregado exitosamente\n")

    elif eleccion == 2:
        nif = str(input("NIF: "))
        if nif in datos:
            del datos[nif]
        else:
            print("Cliente no encontradon\n")

    elif eleccion == 3:
        nif = str(input("NIF: "))
        if nif in datos:
            print(datos[nif])
        else:
            print("Cliente no encontrado\n")

    elif eleccion == 4:
        print(datos, sep= "\n",end="\n\n")

    elif eleccion == 5:
        for nif, pref in datos.items():
            if pref["Preferente"]:
                print(nif, pref["Nombre"], end= "\n\n")

    elif eleccion == 6:
        break

    else:
        print("Valor no válido\n")