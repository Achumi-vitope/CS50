def main():
    plate = input("Plate: ").lower()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    alphanum = '0123456789'
    combined = 'abcdefghijklmnopqrstuvwxyz0123456789'
    length = len(s)
    caught = ''
    next_step = False
    if length > 6 or length < 2:
        return False
    else:
        for i in range(length):
            if s[i] not in combined:
                return False
        for i in range(length):
            if s[0] and s[1] not in letters:
                return False
            if s[i] in alphanum:
                if s[i] == '0':
                    return False
                caught = s[i]
                s = s.replace(caught, "." + caught)
                s = s.split('.')
                next_step = True
                break
        if next_step:
            for i in s[1]:
                if i in letters:
                    return False
        return True


if __name__ == "__main__":
    main()
    