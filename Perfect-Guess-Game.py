import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

guess = None
guesses = 0

print("Welcome to the Perfect Guess Game!")
print("Guess a number between 1 and 100")

while guess != number:
    guess = int(input("Enter your guess: "))
    guesses += 1

    if guess > number:
        print("Too high! Try again.")
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")

print(f"You guessed the number in {guesses} attempts.")