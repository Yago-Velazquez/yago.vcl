def main():
    word = str(input("camelCase: "))
    convert(word)

# Transform to snake case
def convert(what):
    for letter in what:
        if letter.isupper():
            what = what.replace(letter, str("_" + letter.lower()))

    print("snake_case", what, sep=": ")

main()
