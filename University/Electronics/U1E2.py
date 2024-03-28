# Pedimos una palabra:
palabra = str(input("Palabra: "))
vocales = ("a", "e", "i", "o", "u")
contadores = []

for vocal in vocales:
    contador = 0
    for letra in palabra:
        if vocal == letra:
            contador += 1
    contadores.append(contador)

print(f"En la palabra `{palabra}´, hay {contadores[0]} a, {contadores[1]} e, {contadores[2]} i, {contadores[3]} o, {contadores[4]} u.")