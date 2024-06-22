import inflect


def main():
    p = inflect.engine()
    names = take_input("Name: ")
    names = p.join(names)
    print("Adieu, adieu, to", names)


def take_input(prompt):
    x: list = []
    while True:
        try:
            names = input(prompt)
            x.append(names)
        except EOFError:
            print()
            break
    return x


if __name__ == "__main__":
    main()
