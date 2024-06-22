def main():
    menus = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    menu = {}
    for k, v in menus.items():
        menu[k.lower()] = v

    take_order(menu)


def take_order(menu):
    Total = 0
    while True:
        try:
            items = input("Item: ").lower()
            if items in menu:
                Total += menu[items]
            print(f"Total: ${Total:.2f}")
        except EOFError:
            print()
            break

if __name__ == "__main__" :
    main()