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

def get_payout(row, bet , pool):

    if row[0] == row[1] == row[2] :
        match row[0]:
            case "🍒":
                return bet*3
            case "🍋":
                return bet*4
            case "⭐" :
                return bet*10
            case "7️⃣":
                return 10*pool


    else :
        return 0

def main():
    balance = 100
    spin = 0
    win = 0
    lose = 0
    pool = 1
    print("****************************")
    print(f"Your symbols: {symbols[0]} , {symbols[1]} , {symbols[2]} , {symbols[3]}")
    print("Welcome to the Slot Machine!")
    print("****************************")
    print("This is how your payout works: ")
    print("🍒 -- 3X \n 🍋 -- 4X \n ⭐ -- 10X")
    print("Every time you lose a Bet you again 1 point in the jackpot pool. ")

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

        payout = get_payout(row , bet , pool)

        if payout > 0:
            print(f"You earned ${payout}")
            win += 1
            spin += 1

        else :
            print ("You Lost")
            pool += 1
            lose += 1
            spin += 1

        balance += payout

        print(f"Your current balance is ${balance}")
        print("****************************")
        print(f"Total spins : {spin} \n Losses : {lose}  \n Wins : {win}")
        print("****************************")
        play_again = input("Do you want to play again? (y/n): ").upper()

        if play_again != "Y":
            break

    print("******************************")
    print(f"Your final balance is ${balance}")
    print("******************************")


if __name__ == "__main__":
    main()

