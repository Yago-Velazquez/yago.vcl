import re

email = input("EMAIL: ").strip()

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(edu|com)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

#Real regular expression: ^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$