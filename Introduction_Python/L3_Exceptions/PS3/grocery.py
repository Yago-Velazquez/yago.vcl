def main():
    grocery_list = {}
    
    while True:
        try:
            item = input("")
            if item not in grocery_list:
                grocery_list[item] = 1
            else:
                grocery_list[item] += 1
        except EOFError:
            break

    for i in sorted(grocery_list):
        print(f"{grocery_list[i]} {i.upper()}")

if __name__ == "__main__":
    main()

