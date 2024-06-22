import sys
import csv


def main():
    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if ".csv" not in sys.argv[2]:
        sys.exit("Not a csv file")
    try:
        first = []
        last = []
        house = []
        with open(sys.argv[1], 'r') as before:
            reader = csv.DictReader(before)
            for i in reader:
                l, f = i['name'].split(",")
                first.append(f.strip())
                last.append(l.strip())
                house.append(i['house'])

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    except Exception as arg:
        sys.exit(arg)

    with open(sys.argv[2], 'w') as update:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(update, fieldnames = fieldnames)
            writer.writeheader()
            for i in range(len(first)):
                writer.writerow({"first":first[i], "last":last[i], "house": house[i]})


if __name__ == "__main__":
    main()
