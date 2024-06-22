import random


def main():
    Level = user_input("Level: ")
    Guess: int = -1
    answer = random.randint(0, Level + 1)

    while Guess != answer:
        Guess = user_guess(Level)
        if Guess < answer:
            print("Too small!")
        elif Guess > answer:
            print("Too Large!")
        else:
            print("Just right!")
            break


def user_guess(x):
    while True:
        try:
            Guess = int(input("Guess: "))
            if Guess >= 0 and Guess <= x:
                break
        except:
            pass
    return Guess


def user_input(p):
    while True:
        try:
            Level = int(input(p))
            if Level >= 0:
                break
        except:
            pass
    return Level


if __name__ == "__main__":
    main()
