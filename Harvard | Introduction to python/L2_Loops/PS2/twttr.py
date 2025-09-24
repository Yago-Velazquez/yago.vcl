def main():
    phrase = str(input("Input: "))
    no_vowels(convert(phrase))

def convert(word):
    return word.lower()

def no_vowels(word):
    for i in word:
        if i in ["a", "e", "i", "o", "u"]:
            word = word.replace(i, "")
    print(f"Output: {word}")

main()
