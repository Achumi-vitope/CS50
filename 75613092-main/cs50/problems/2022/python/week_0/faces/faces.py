
def main():
    user_input = input("Enter text here: ")
    convert(user_input)

def convert(user_input):
    text = user_input.split(" ")
    emojis = {
        ":)" : "🙂",
        ":(" : "🙁"
    }

    result = " "
    for i in text:
        result += emojis.get(i, i)+ " "
    print(result)






main()