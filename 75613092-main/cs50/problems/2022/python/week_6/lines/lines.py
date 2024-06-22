import sys


def main():
    line_count = 0
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a python file")
    try:
        file = open(sys.argv[1], "r")
        for line in file:
            if not len(line.strip()) == 0:
                if not line.strip().startswith('#'):
                    line_count += 1

        file.close()
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(line_count)



if __name__ == "__main__":
    main()