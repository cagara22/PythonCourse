def show_balance(balance: float):
    print(f"Your current balance is ${balance:.2f}")


def deposit():
    while True:
        amount = input("Enter an amount to be deposited: ")
        if not amount.isalpha():
            amount = float(amount)
            if amount > 0:
                return amount
        print("That is not a valid amount!")


def withdraw(balance: float):
    while True:
        amount = input("Enter an amount to be withdrawn: ")
        if not amount.isalpha():
            amount = float(amount)
            if 0 < amount <= balance:
                return amount
            else:
                print(f"The amount is not within the withdrawing range ($1.00 - ${balance})")
        else:
            print("That is not a valid amount")


def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program!")
        print("1 - Show Balance")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - EXIT")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                show_balance(balance)
            case "2":
                deposit_amount = deposit()
                balance += deposit_amount
                print(f"Successfully deposited ${deposit_amount}!")
            case "3":
                withdraw_amount = withdraw(balance)
                balance -= withdraw_amount
                print(f"Successfully withdrawn ${withdraw_amount}!")
            case "4":
                is_running = False
            case _:
                print("Invalid Option")

    print("Thank you! Have a nice day!")


if __name__ == "__main__":
    main()
