def main():
    camelCase = input("camelCase: ")
    to_replace =""
    foundCamelCase = ""
    for i in camelCase:
        if i.isupper():
            foundCamelCase = i
            to_replace = "_" + i.lower()
            camelCase = camelCase.replace(foundCamelCase, to_replace)
    print(camelCase)
if __name__ == "__main__":
    main()