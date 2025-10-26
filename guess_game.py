import random

jackpot = random.randint(1, 300)
guess = int(input("Guess the number: "))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("Guess Higher:")
    else:
        print("Guess Lower:")
    guess = int(input("Try again: "))
    counter += 1

print("🎉 Right Answer!")
print("You took", counter, "attempts!")