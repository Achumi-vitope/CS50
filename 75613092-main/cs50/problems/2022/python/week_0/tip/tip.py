def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #d = d.translate({ord('$') : None})
    d = d.replace("$", "")
    new_d = d
    new_d = float(new_d)
    return new_d



def percent_to_float(p):
    #p = p.translate({ord('%') : None})
    p = p.replace("%", "")
    new_P = p
    new_p = float(new_P)
    new_p = new_p/100
    return new_p











main()