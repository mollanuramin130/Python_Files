# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    return x / y

while True:
    # Display the menu
    print()
    print("Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("Enter 'quit' to end the program")

    # Prompt the user for their choice
    user_input = input(": ")

    if user_input == "quit":
        break

    if user_input in ("+", "-", "*", "/"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "+":
            print("Result:", add(num1, num2))
        elif user_input == "-":
            print("Result:", subtract(num1, num2))
        elif user_input == "*":
            print("Result:", multiply(num1, num2))
        elif user_input == "/":
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")
