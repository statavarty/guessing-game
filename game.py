"""A number-guessing game."""

# Put your code here
from random import randint

name = input("Howdy, what's your name? ")
print(f"\n{name}, I'm thinking of a number between 1 and 100")
print("Try to guess my number")

# set system generated number
guess_num = randint(1, 101)
count = 0
round = 1
player_stats = []

while True:
    guessed_num = int(input("Your Guess? "))
    count += 1
    if guessed_num == guess_num:
        print(f"\nWell done, {name}! You found my number in {count} tries!")
        print()
        player_stats.append(count)
        print("Do you want to play again?")
        check_multiple_rounds=input("Press [Enter] to Quit ")
        if check_multiple_rounds:
            guess_num = randint(1, 101)
            round += 1
            continue
        else:
            break
        break
    elif guessed_num > guess_num:
        print("Your guess is too high, try again.")
    else:
        print("Your guess is too low, try again.")

# At the end print player statistics
print(f'\n List of rounds(tries) {name} played')
print(40 * '-')
for index, value in enumerate(player_stats, 1):
    print(f'{index :<1}. {value:>2}(tries)')