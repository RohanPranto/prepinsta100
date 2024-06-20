# Write a program to find the factorial of a number using recursion.

number = int(input("Enter a number: "))
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print(f"The factorial of {number} is {factorial(number)}")
