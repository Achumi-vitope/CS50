import sys
import pyfiglet


def main():
    has_arg: bool = False
    if len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            check_font(sys.argv)
            has_arg = True
            take_input(has_arg, sys.argv)
        else:
            abort()
    elif len(sys.argv) == 1:
        has_arg = False
        take_input(has_arg, sys.argv)
    else:
        abort()


def take_input(x, y):
    if x:
        text = input("Text: ")
        f = pyfiglet.Figlet(font=y[2])
        print(f.renderText(text))
    else:
        text = input("Text: ")
        print(pyfiglet.figlet_format(text))


def check_font(x):
    try:
        if pyfiglet.Figlet(font=x[2]):
            return True
    except:
        abort()


def abort():
    print("Invalid usage")
    sys.exit(1)


if __name__ == "__main__":
    main()
