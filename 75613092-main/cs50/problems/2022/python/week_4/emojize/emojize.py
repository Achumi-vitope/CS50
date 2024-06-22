from emoji import emojize, is_emoji

def main():
    to_emoji = input()
    to_emoji = emojize(to_emoji, language = 'alias')

    if not is_emoji(to_emoji):
        print("Not an emoji.")
    else:
        print(to_emoji)

if __name__ == "__main__":
    main()