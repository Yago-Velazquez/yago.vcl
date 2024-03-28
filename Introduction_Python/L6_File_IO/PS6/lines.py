import sys

if len(sys.argv) != 2:
    sys.exit("Incorrect number of command-line arguments")
else:
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        code_lines = [line.strip() for line in lines if line.strip() and line[0] != "#"]
        print(len(code_lines))