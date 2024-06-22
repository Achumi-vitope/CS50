def main():
    word = input("Input: ")
    result = shorten(word)
    print("Output:", result)

def shorten(word):
    vowels = 'aeiou'
    result = ''
    for i in word:
        if i in vowels:
            continue
        result = result + i
    return result
if __name__ == "__main__":
    main()