def main():
    fraction = get_input("Fraction: ")
    fraction = round(fraction, 2) * 100

    fraction = int(fraction)
    if fraction <= 1:
        print("E")
    elif fraction >= 99:
        print("F")
    else:
        print(f"{fraction}%")

def get_input(prompt):
    while True:
        try:
            fraction = input(prompt)
            x, y = fraction.split("/")
            if "." in x or "." in y:
                get_input("Fraction: ")
            x = float(x)
            y = float(y)

            if x > y:
                get_input("Fraction: ")

            return x / y

        except ValueError:
            pass
        except ZeroDivisionError:
            pass

if __name__ == "__main__":
    main()