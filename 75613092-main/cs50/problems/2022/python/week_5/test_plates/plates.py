def main():
    plate = input("Plate: ").lower()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.lower()
    for i in s:
        if i not in 'abcdefghijklmnopqrstuvwxyz1234567890':
            return False
    if len(s) > 6 or len(s) < 2:
        return False
    if s[0] and s[1] > 'a' and s[0] and s[1] < 'z':
        c = 1
        for i in range(len(s)):
            if i > 1:
                if s[i] > 'a' and s[i] < 'z':
                    if c == len(s) - 2:
                        return True
                    c += 1
                    continue
                elif ord(s[i]) != 48:
                    s = s.replace(s[i], "." + s[i])
                    s = s.split(".")
                    for i in s[1]:
                        if i > 'a' and i < 'z':
                            return False
                    return True
                else:
                    return False
    else:
        return False


if __name__ == "__main__":
    main()
