name = input("Please enter your name: ")
student_id = input("Please enter your Student ID: ")

number1 = int(input("Please enter a whole number: "))
number2 = int(input("Please enter a different second whole number: "))

# Perform three calculations.
multiplication = number1 * number2
division = number1 / number2
addition = number1 + number2

# Display each result with two decimal places.
print(f"The result of {number1} times {number2} is: {multiplication:.2f}")
print(f"The result of {number1} divided by {number2} is: {division:.2f}")
print(f"The result of {number1} plus {number2} is: {addition:.2f}")

# Compare the two numbers.
if number1 > number2:
    print("Number 1 is larger than Number 2")
elif number1 < number2:
    print("Number 1 is smaller than Number 2")
else:
    print("Number 1 is equal to Number 2")

# Display your name and student ID.
print(name)
print(student_id)