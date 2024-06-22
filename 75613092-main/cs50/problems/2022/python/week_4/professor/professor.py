import random


def main():
    level = get_level()
    mistakes  = 0
    score = 0
    question = 0
    while True:
        x, y = generate_integer(level)
        question += 1
        mistakes = 0
        while mistakes != 3:
            try:
                ask = int(input(f"{x} + {y} = "))
                if ask ==  (x + y):
                    score += 1
                    break
                else:
                    print("EEE")
                    mistakes += 1
                if mistakes == 3:
                    print(f"{x} + {y} = {x+y}")
            except ValueError or EOFError:
                print("EEE")
                pass
        if question == 10:
            break
    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 4 and level > 0:
                return level
        except ValueError:
            pass



def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y



if __name__ == "__main__":
    main()