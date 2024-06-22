import requests
import sys
import json

def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        amount = float(sys.argv[1])
        jayson = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        jayson = jayson.json()
        jayson = jayson['bpi']['USD']['rate']
        jayson = jayson.split(",")

        jayson = jayson[0] + jayson[1]
        price = amount * float(jayson)

        print(f"${price:,}")

    except requests.RequestException:
        sys.exit(1)

    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)





if __name__ == "__main__":
    main()