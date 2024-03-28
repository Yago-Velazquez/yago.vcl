import re

name = input("Name: ").strip()

if matches := re.search(r"^(.+), *(.+)$" , name):
    name = f"{matches.group(2)} {matches.group(1)}".title()
print(f"Hello, {name}")