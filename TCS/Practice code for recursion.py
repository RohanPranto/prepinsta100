# 1. Power of a Number
# 2. Prime Number
# 3. Largest element in an array
# 4. Smallest element in an array
# 5. Reversing a Number
# 6. HCF of two numbers
# 7. LCM of two numbers
# 8. Program to calculate length of the string using recursion
# 9. Print All Permutations of a String
# 10. Given an integer N the task to print the F(N)th term.
# 11. Given a list arr of N integers, print sums of all subsets in it
# 12. Last non-zero digit in factorial
# 13. Given a positive integer N, return the Nth row of pascal’s triangle 
# 14. Given an integer N representing the number of pairs of parentheses, the task is to generate all combinations of well-formed(balanced) parentheses
# 15. Find the Factorial of a number using recursion
# 16. Find all possible Palindromic partitions of the given String
# 17. Find all the N bit binary numbers having more than or equal 1’s than 0’s
# 18. Given a set of positive integers, find all its subsets
# 19. Given a string s, remove all its adjacent duplicate characters recursively

# 1. Power of a Number
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power(base, exponent - 1)

base = int(input("Enter a base number: "))
exponent = int(input("Enter an exponent: "))

result = power(base, exponent)

print(f"{base} raised to the power of {exponent} is: {result}")

################################################################

# 2. Prime Number
import math

def isPrime(number, divisor=None):
    if divisor is None:
        divisor = int(math.sqrt(number)) + 1
    
    if number <= 1:
        return False
    if divisor == 1:
        return True
    if number % divisor == 0:
        return False
    
    return isPrime(number, divisor - 1)

number = int(input("Enter a number: "))

if isPrime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

################################################################

# 3. Largest element in an array
input_string = input("Enter the array elements separated by space: ")
arr = list(map(int, input_string.split()))
max_element = arr[0]
for num in arr[1:]:
    if num > max_element:
        max_element = num
print("The largest element in the array is:", max_element)

################################################################

#4. Smallest element in an array
input_string = input("Enter the array elements separated by space: ")
arr = list(map(int, input_string.split()))
max_element = arr[0]
for num in arr[1:]:
    if num < max_element:
        max_element = num
print("The largest element in the array is:", max_element)

################################################################

# 6. HCF of two numbers
def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is: {result}")

################################################################

# 7. LCM of two numbers
import math
def lcm(a, b):
    product = a * b
    gcd_value = math.gcd(a, b)
    lcm_value = abs(product) // gcd_value
    return lcm_value
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result}")

################################################################




