def main():
    user_input("Date: ")

def user_input(prompt):
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
    ]
    while True:
        status = 0
        bad_date_format = input(prompt).title()
        try:
            dd, yyyy = bad_date_format.split(",")
            yyyy = yyyy.strip()
            mm, dd= dd.split(" ")
            if mm not in months:
                user_input("Date: ")
            break
        except:
            pass
        try:
            mm, dd, yyyy = bad_date_format.split("/")
            if mm in months:
                user_input("Date: ")
            status = 1
            break
        except:
            pass

    if status != 1:
        mm = months.index(mm) + 1
    mm = int(mm)
    dd = int(dd)
    yyyy = int(yyyy)

    if mm > 12 or dd > 31:
        user_input("Date: ")

    print(f"{yyyy}-{mm:02}-{dd:02}")



if __name__ == "__main__":
    main()