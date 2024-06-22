def main():
    Greetings = input("Greetings: ").lower()
    splited_text = Greetings.split()

    if "hello" in splited_text[0]:
        print("$0")
    elif Greetings[0] == 'h':
        print("$20")
    else:
        print("$100")
main()
