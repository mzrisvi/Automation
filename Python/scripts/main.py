import HelloPython
tempvar = 10
# Main function
def main():
    tempvar = 20
    print("Hello from main.py!")
    name = input("Enter your name: ")
    print("Welcome",name)
    age = int(input("Enter your age: "))
    print("You are",age,"years old.")
    if (age<60):
        print("You are young!")
    else:
        print("You are wise!")
    age = age + 1
    Age = age + 5
    print("Next year, you will be",age,"years old.")
    print("In 5 years, you will be",Age,"years old.")
    print("The local variable tempvar is:", tempvar)
    
main()
print("The Global variable tempvar is:", tempvar)