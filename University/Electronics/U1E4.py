# Diccionario con asignaturas y créditos:
uni = {
    "Matemáticas": "6",
    "Física": "4",
    "Química": "5",
}
# Mostrar por pantalla los creditos de cada asignatura
for name in uni:
    print(f"{name}: Tiene {uni[name]} créditos")