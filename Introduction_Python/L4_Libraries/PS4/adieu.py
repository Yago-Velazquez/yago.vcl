# https://pypi.org/project/inflect/
import inflect

names = []

while True:
    try:
        name = str(input("Name: "))
    except EOFError:
        print(f"Adieu, adieu, to {inflect.engine().join(names)}")
        break
    else:
        names.append(name)