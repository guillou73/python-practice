with open("example.txt", "w") as file:

    file.write("Hello, class!")
    
with open("example.txt" , "r") as file:
    file.read()
    print("content")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
    import math
    print(math.sqrt(16))
    numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

# Writing to the file using a loop
with open("example.txt", "w") as file:
    for i in range(1):  # Loop to write a single line (not necessary, but for demonstration)
        file.write("Hello, class!\n")

        # Reading from the file using a loop
with open("example.txt", "r") as file:
    content = ""
    for line in file:
        content += line
    print("Content:", content)
# Handling an exception
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
     # Using a loop for the math operation
    import math
    values = [16]
    for value in values:
        print(math.sqrt(value))
# Using a for loop to square numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for i in numbers:
    squared_numbers.append(i** 2)

print(squared_numbers)