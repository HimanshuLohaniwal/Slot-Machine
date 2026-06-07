import random
symbols = ["🍒", "🍋", "⭐", "7️⃣"]

def spin_row():
    symbols = ["🍒", "🍋", "⭐", "7️⃣"]
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results

def print_row(row):
    # print(" ".join(row)) -- this joins the item of list row with a space giving it a clean look while displaying
    print(" ! ".join(row))

def get_payout(row, bet):

    if row[0] == row[1] == row[2] :
        match row[0]:
            case "🍒":
                return bet*3
            case "🍋":
                return bet*4
            case "⭐" :
                return bet*10
            case "7️⃣":
                return bet*7

    else :
        return 0

def main():
    balance = 100
    print("****************************")
    print(f"Your symbols: {symbols[0]} , {symbols[1]} , {symbols[2]} , {symbols[3]}")
    print("Welcome to the Slot Machine!")

    while balance > 0:
        print(f"Your balance is ${balance}")

        bet = input("Enter your bet amount: ")
        if not bet.isdigit():
            print("Invalid bet amount. Please try again.")
            continue

        bet = int(bet)

        if bet > balance:
            print("You don't have enough balance to make that bet. Please try again.")
            continue

        if bet <= 0:
            print("Bet amount must be greater than zero. Please try again.")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning.... ")
        print_row(row)

        payout = get_payout(row , bet)

        if payout > 0:
            print(f"You earned ${payout}")

        else :
            print ("You Lost")

        balance += payout

        print(f"Your current balance is ${balance}")

        play_again = input("Do you want to play again? (y/n): ").upper()

        if play_again != "Y":
            break

    print("******************************")
    print(f"Your final balance is ${balance}")
    print("******************************")


if __name__ == "__main__":
    main()

