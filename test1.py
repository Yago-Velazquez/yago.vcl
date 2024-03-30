import re
matches = re.findall(r"0-1(?:-[1-9])*0", "0-100-10")
print(len(matches))