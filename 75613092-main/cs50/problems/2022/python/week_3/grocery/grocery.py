def main():
    get_input()


def get_input():
    count = 1
    basket = {}
    duplicates = []
    x = ""
    while True:
        try:
            Grocery = input().upper()
            count = 1
            if Grocery in duplicates:
                count += 1
            duplicates.append(Grocery)
            basket[Grocery] = count

        except (EOFError, KeyError):
            print()
            break
    basket = sorted(basket.items())
    for k, v in basket:
        print(v, k)


if __name__ == "__main__":
    main()
