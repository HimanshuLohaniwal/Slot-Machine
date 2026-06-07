import random
symbols = ["🍒", "🍋", "⭐", "7️⃣"]

def spin_row():
    symbols = ["🍒", "🍋", "⭐", "7️⃣"]
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results

def print_row(row):
    print(" ".join(row))

def get_payout():
    pass

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

main()

