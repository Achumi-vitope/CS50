def main():
    amount_due = 50
    coins = insert_coins(amount_due)
    change_owed = 0
    paid = 0
    while True:
        amount_due  -= coins
        paid += coins
        if paid < 50:
            print("Amount Due:", amount_due)
            coins = insert_coins(amount_due)
        elif paid > 50:
            change_owed = paid - 50
            print("Change Owed:", change_owed)
            break
        elif paid == 50:
            print("Change Owed:", change_owed)
            break


def insert_coins(amount_due):
    coins = 0
    while True:
        coins = int(input("Insert Coin: "))
        if coins == 25 or coins == 10 or coins == 5:
            return coins
        else:
            print("Amount Due:", amount_due)






if __name__ == "__main__":
    main()