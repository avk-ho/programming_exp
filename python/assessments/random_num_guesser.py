# https://www.programmingexpert.io/programming-fundamentals/assessment/1

# Make sure to use `random.randint` to pick your random number.

import random

while True:
    range_start = input("Enter the start of the range: ") # code given, will always be > 0

    if range_start.isdigit():
        range_start = int(range_start)
        break

    print("Please enter a valid number.")

while True:
    range_end = input("Enter the end of the range: ") # code given

    if range_end.isdigit():
        range_end = int(range_end)

        if range_end > range_start:
            break
    
    print("Please enter a valid number.")

rand_num = random.randint(range_start, range_end)
guess_count = 0
guess_hit = False

while not guess_hit:
    guess = input("Guess a number: ")
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess_count += 1
    guess = int(guess)
    
    if guess == rand_num:
        guess_hit = True

if guess_count == 1:
    print(f"You guessed the number in 1 attempt")
else:
    print(f"You guessed the number in {guess_count} attempts")