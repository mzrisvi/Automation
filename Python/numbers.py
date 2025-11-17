import random
# This is a simple numbers module

random_number = random.randint(1, 100)
print("Here is a random number for you:", random_number)

print(10>8)
def is_even(num):
    return num % 2 == 0
x = 4
y = 20

print(x, y)
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Is x greater than y?", x > y)
print("Is x less than or equal to y?", x <= y)
print("Is x equal to y?", x == y)
print("Modulus of x and y:", x % y)
print("Exponentiation of x to the power of 2:", x ** 2)
print("Add 5 to x:", x + 5)
print("Is x even?", is_even(x))
print("Is y even? AND x greater than y?", is_even(y) and (x > y))
print("is x equal y", x is y)

