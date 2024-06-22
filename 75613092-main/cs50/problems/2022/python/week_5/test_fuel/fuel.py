def main():
    fraction = input("Fraction: ")
    convert(fraction)


def convert(fraction):
    while True:
        try:
            if "/" not in fraction:
                main()
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x > y:
                continue
        except ValueError:
            raise
        else:
            try:
                return int(gauge(x/y * 100))
            except ZeroDivisionError:
                raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (percentage) + "%"


if __name__ == "__main__":
    main()
