def main():
    time = input("What time is it? ")
    convert(time)

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    hours = (hours * 60) + minutes
    hours = hours / 60

    if hours >= 7 and hours <= 8:
        print('Breakfast time')
    elif hours >= 12 and hours <= 13:
        print("Lunch time")
    elif hours >= 18 and hours <= 19:
        print("Dinner time")
    return hours
if __name__ == "__main__":
    main()