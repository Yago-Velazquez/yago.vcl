def main():
    hello("Yago")
    hello()
    goodbye("Yago")
    goodbye()


def hello(to="World"):
    print(f"Hello, {to}")


def goodbye(to="World"):
    print(f"Goodbye {to}")
    

if __name__ == "__main__":
    main()
