# 1) Find Maximum of Three Numbers
def find_max(a, b, c):
    return max(a, b, c)
print(find_max(3, 7, 12))

# 2) Check if a Number is Positive, Negative, or Zero
    
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
print(check_number(0))
print(check_number(-5))
print(check_number(10))

# 3) Find Factorial of a Number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(4))

# 4) Reverse a String
def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))

# 5) Find Fibonacci Series (up to n terms)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
print(fibonacci(6))
# 6) Find the Square of a Number
def square(n):
    return n ** 2
print(square(2))
# 7) Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(n):
    return (n * 9/5) + 32
print(celsius_to_fahrenheit(4))
# 8) Count Vowels in a String
def count_vowels(n):
    vowels = "aeiouAEIOU"
    return sum(1 for char in n if char in vowels)
print(count_vowels("hello world"))