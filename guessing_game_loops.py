# Name: Replace this with your full name
# Date: October 30, 2026
# Description: Ask the user to guess a number, report the result and tries,
# then demonstrate the same five increments with while and for loops.

userName = input("What is your name? ")
studentId = input("What is your student ID? ")

print(f"Hello, {userName}!")
print(f"Student ID: {studentId}")

correctNumber = 5
guessCount = 0

while True:
    try:
        userGuess = int(input("Please guess a number between 1 and 10..."))
    except ValueError:
        print("Please enter a whole number between 1 and 10.")
        continue

    if userGuess < 1 or userGuess > 10:
        print("Your guess must be between 1 and 10.")
        continue

    guessCount += 1

    if userGuess == correctNumber:
        print(
            f"Congratulations, {userName}! You guessed the number "
            f"in {guessCount} tries!"
        )
        break
    elif userGuess > correctNumber:
        print("You guessed too high")
    else:
        print("You guessed too low")

print("\nOutput from the 'while' loop:")
increment = 1
while increment <= 5:
    incrementedValue = correctNumber + increment
    print(f"{correctNumber} incremented by {increment} is {incrementedValue}")
    increment += 1

print("\nOutput from the 'for' loop:")
for increment in range(1, 6):
    incrementedValue = correctNumber + increment
    print(f"{correctNumber} incremented by {increment} is {incrementedValue}")
