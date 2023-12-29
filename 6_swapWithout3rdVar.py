# Take the values of the two numbers from the user.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Print the current values of num1 and num2.
print("Current values of num1 and num2 are:", num1, num2)

# Swap the values of num1 and num2 using arithmetic operations.
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

# Print the swapped values of num1 and num2.
print("Swapped values of num1 and num2 are:", num1, num2)
