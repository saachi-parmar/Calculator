#---------------------------------------------------------------------------------------
# CALCULATOR
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
def square(num1, num2):
    return num1**2, num2**2

print("SELECT OPERATION TO PERFORM: \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n 5.Square \n")

operation = str(input("ENTER THE OPERATION TO BE PERFORMED: "))

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the first number: "))

if operation=="Add":
    print(n1, "+", n2, "=", add(n1, n2))
elif operation=="Suntract":
    print(n1, "-", n2, "=", subtract(n1, n2))
elif operation=="Multiply":
    print(n1, "x", n2, "=", multiply(n1, n2))
elif operation=="Divide":
    print(n1, "+", n2, "=", divide(n1, n2))
elif operation=="Square":
    print(n1, "^2=", square(n1), n2, "^2=", square(n2))
else:
    print("Invalid Input")
    
print("\n")