from sys import exit, argv
import csv
from tabulate import tabulate

def main():
    if len(argv) > 2:
        exit("Too many command-line arguments")
    elif len(argv) < 2:
        exit("Too few command-line arguments")
    if ".csv" not in argv[1]:
        exit("Not a csv file")

    table = []
    try:
        with open(argv[1]) as file:
            x = csv.reader(file)
            for line in x:
                table.append(line)
            print(tabulate(table, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        exit("File does not exist")



if __name__ == "__main__":
    main()