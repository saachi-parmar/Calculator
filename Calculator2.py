import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def square(a):
    return a ** 2

def exponent(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def square_root(a):
    if a < 0:
        return "Error: Square root of negative number"
    return math.sqrt(a)

def calculator():
    print("=== ADVANCED PYTHON CALCULATOR ===")
    print("Available operations:")
    print(" 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n 5. Square\n 6. Exponent\n 7. Modulus\n 8. Square Root\n 9. Exit")

    while True:
        operation = input("\nEnter operation name or number (e.g., Add or 1): ").strip().lower()

        if operation in ["9", "exit"]:
            print("Exiting calculator. Goodbye!")
            break

        if operation in ["5", "square", "8", "square root"]:
            try:
                a = float(input("Enter number: "))
                if operation in ["5", "square"]:
                    print(f"Result: {a}² = {square(a)}")
                elif operation in ["8", "square root"]:
                    print(f"Result: √{a} = {square_root(a)}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        if operation in ["1", "add"]:
            print(f"Result: {a} + {b} = {add(a, b)}")
        elif operation in ["2", "subtract"]:
            print(f"Result: {a} - {b} = {subtract(a, b)}")
        elif operation in ["3", "multiply"]:
            print(f"Result: {a} * {b} = {multiply(a, b)}")
        elif operation in ["4", "divide"]:
            print(f"Result: {a} / {b} = {divide(a, b)}")
        elif operation in ["6", "exponent"]:
            print(f"Result: {a}^{b} = {exponent(a, b)}")
        elif operation in ["7", "modulus"]:
            print(f"Result: {a} % {b} = {modulus(a, b)}")
        else:
            print("Invalid operation. Please try again.")

if __name__ == "__main__":
    calculator()
