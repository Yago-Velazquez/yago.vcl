datos = [
    {"Mes": "Enero", "Ventas": "30500", "Gastos": "22000"},
    {"Mes": "Febrero", "Ventas": "35600", "Gastos": "23400"},
    {"Mes": "Marzo", "Ventas": "28300", "Gastos": "18100"},
    {"Mes": "Abril", "Ventas": "33900", "Gastos": "20700"},
]
for name in datos:
    print(name["Mes"]+ ": " + name["Ventas"], name["Gastos"])