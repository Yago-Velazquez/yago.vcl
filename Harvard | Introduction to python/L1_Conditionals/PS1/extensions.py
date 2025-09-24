file = str(input("File name: "))

file = file.partition(".")

match file[2]:
    case "gif" | "jpeg" | "jpg" | "png":
        print(f"image/{file[2]}")
    case "pdf" | "zip":
        print(f"application/{file[2]}")
    case "txt":
        print(f"text/plain")
    case _:
        print("application/octetstream")