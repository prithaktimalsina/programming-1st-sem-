import random 
symbols = ['cherry', 'orange', 'banana', 'bar', 'seven', 'grape', 'bell']
print("Welcome to the slot machine simulator!")
print("It costs $1.00 to spin the reel.")
print("Jackpot payout for all five reels matching: $1,000.00\n")
total_spins = 0
while True:
    input("Press Enter to spin...")
    total_spins += 1
    reels = [random.choice(symbols) for _ in range(5)]
    print('|'.join(reels))
    if all(symbol == reels[0] for symbol in reels):
        print(f"\nCongratulations! You hit the jackpot in {total_spins} spins.")
        print(f"You've won $1,000.00!\n")
        play_again = input("Would you like to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break
print(f"\nTotal spins: {total_spins}")
print("Thank you for playing!")