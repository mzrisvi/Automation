# This is a simple calculator module
def main(args=None):
    print("This is the calculator module.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero.")
            return
    else:
        print("Invalid operation.")
        return
    print("The result is:", result)
main()

# This is for module testing
print("Module testing:")
def sum():
    x = 5
    y = 10
    return x + y
print("Sum is:", sum())

def multiply(a, b):
    return a * b
print("Multiplication is:", multiply(3, 4))

def divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    return a / b
print("Division is:", divide(10, 2))

def subtract(a, b):
    return a - b
print("Subtraction is:", subtract(10, 5))