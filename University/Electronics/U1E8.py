import csv
import sys
import pandas as pd

def main():
    """
    Apartado 2
    """
    with open("titanic.csv") as file1:
        parametros_titanic(file1)
    """
    Apartado 3 y 4
    """
    with open("titanic.csv") as file2:
        pasajeros(file2)
    """
    Apartado 5
    """
    with open("titanic.csv") as file3:
        VIP(file3)
    """
    Apartado 6
    """
    with open("titanic.csv") as file4:
        porcentaje_total(file4)
    """
    Apartado 7
    """
    with open("titanic.csv") as file5:
        porcentaje(file5, 1)
    with open("titanic.csv") as file6:
        porcentaje(file6, 2)
    with open("titanic.csv") as file7:
        porcentaje(file7, 3)
    """
    Apartado 8
    
    with open("titanic.csv") as file:
        edad(file)
    """

def parametros_titanic(n):
    df = pd.DataFrame(csv.DictReader(n))
    size = df.size
    column_name = df.columns
    return f"Size: {size}, Name of columns: {column_name}", df.head(10), df.tail(10)

def pasajeros(n):
    for row in csv.DictReader(n):
        if row["PassengerId"] == "148" or int(row["PassengerId"])%2 == 0:
            print(row, end= "\n\n\n")

def VIP(n):
    first_class_passengers = []
    for row in csv.DictReader(n):
        if row["Pclass"] == "1":
            first_class_passengers.append(row["Name"])
    print("Los personajes VIP son:")
    for passenger in sorted(first_class_passengers):
        print(passenger, sep="\n")

def porcentaje_total(n):
    vivos = 0
    fallecidos = 0
    for row in csv.DictReader(n):
        if int(row["Survived"]) == 0:
            fallecidos += 1
        else:
            vivos += 1
    porcentaje = round((vivos/(fallecidos + vivos)) * 100)
    print(f"Porcentaje de supervivientes: {porcentaje}%", end= "\n\n\n")

def porcentaje(n, m):
    vivos = 0
    fallecidos = 0
    for row in csv.DictReader(n):
        if int(row["Survived"]) == 0 and int(row["Pclass"]) == m:
            fallecidos += 1
        elif int(row["Survived"]) == 1 and int(row["Pclass"]) == m:
            vivos += 1
    porcentaje = round((vivos/(fallecidos + vivos)) * 100)
    print(f"Porcentaje de supervivientes (Grupo {m}): {porcentaje}%", end= "\n\n\n")

if __name__ == "__main__":
    main()