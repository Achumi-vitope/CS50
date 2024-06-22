def main():
    ask = input("What is the Answer to the Great Question Of Life, the Universe and Everything? ").lower().strip()

    if ask == "42" or ask == "forty-two" or ask =="forty two":
        print("Yes")
    else:
        print("No")

main()