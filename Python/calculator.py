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

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero."
        return a / b

    def subtract(self, a, b):
        return a - b
    
calc = Calculator()
print("Addition is:", calc.add(5, 3))
print("Multiplication is:", calc.multiply(4, 2))
print("Division is:", calc.divide(8, 2))
print("Subtraction is:", calc.subtract(10, 4))