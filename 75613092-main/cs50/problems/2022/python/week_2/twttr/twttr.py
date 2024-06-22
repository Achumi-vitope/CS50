def main():
    Prompt = input("Input: ")
    vowels = 'aeiou'
    result = ''
    for i in Prompt:
        if i in vowels or i in vowels.upper():
            continue
        result = result + i
    print("Output: ", result)
if __name__ == "__main__":
    main()