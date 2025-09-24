def main():
    print(shorten(input("WORD: ")))



def shorten(word="Hello, world"):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letter in word:
        if letter in vowels:
            word = word.replace(letter, "")
    return word


if __name__ == "__main__":
    main()