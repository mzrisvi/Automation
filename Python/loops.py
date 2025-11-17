# For loop example
for i in range(1,5):
    print("Iteration:", i)

# While loop example
count = 1
while count <= 5: # condition checked BEFORE running
    print("Count is:", count)
    count += 1
print("Loop finished!")

# Do-while loop example
count = 1
while True:
    print("Count is:", count)
    count += 1
    if count > 5:   # condition checked AFTER running once
        break