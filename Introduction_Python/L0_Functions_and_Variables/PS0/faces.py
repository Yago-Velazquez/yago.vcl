# Define main
def main():
    sentence = str(input())
    print(convert(sentence))

# Define convert
def convert(words):
    first = words.replace(":)", "🙂")
    return first.replace(":(", "🙁")

# Call main
main()