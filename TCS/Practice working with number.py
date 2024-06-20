# Highest Common Factor (HCF)
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
if number1 > number2:
    smaller = number2
else:
    smaller = number1
for i in range(1, smaller + 1):
    if (number1 % i == 0) and (number2 % i == 0):
        hcf = i
print("The H.C.F. of", number1, "and", number2, "is", hcf)


# Lowest Common Multiple (LCM)
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
if number1 > number2:
    greater = number1
else:
    greater = number2
while True:
    if (greater % number1 == 0) and (greater % number2 == 0):
        lcm = greater
        break
    greater += 1
print("The L.C.M. of", number1, "and", number2, "is", lcm)


# Prime Number
number = int(input("Enter a number: "))
if number > 1:
    for i in range(2, int(number**0.5) + 1):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")


# Prime Numbers in an Interval
lower = int(input("Enter the lower number: "))
upper = int(input("Enter the upper number: "))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)


# GCD
import math
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print("The GCD of", number1, "and", number2, "is", math.gcd(number1, number2))


# LCM
import math
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print("The LCM of", number1, "and", number2, "is", math.lcm(number1, number2))


# Binary to Decimal
binary = input("Enter a binary number: ")
decimal = int(binary, 2)
print("The decimal value is:", decimal)


# Decimal to Binary
decimal = int(input("Enter a decimal number: "))
binary = bin(decimal).replace("0b", "")
print("The binary value is:", binary)


# Decimal to Octal
decimal = int(input("Enter a decimal number: "))
octal = oct(decimal).replace("0o", "")
print("The octal value is:", octal)


# Octal to Decimal
octal = input("Enter an octal number: ")
decimal = int(octal, 8)
print("The decimal value is:", decimal)


# Decimal to Hexadecimal
decimal = int(input("Enter a decimal number: "))
hexadecimal = hex(decimal).replace("0x", "")
print("The hexadecimal value is:", hexadecimal)


# Hexadecimal to Decimal
hexadecimal = input("Enter a hexadecimal number: ")
decimal = int(hexadecimal, 16)
print("The decimal value is:", decimal)


# Octal to Binary
octal = input("Enter an octal number: ")
decimal = int(octal, 8)
binary = bin(decimal).replace("0b", "")
print("The binary value is:", binary)


# Binary to Octal
binary = input("Enter a binary number: ")
decimal = int(binary, 2)
octal = oct(decimal).replace("0o", "")
print("The octal value is:", octal)


# Quadrant in Which the Coordinate Point Lies
x = int(input("Enter the x-coordinate: "))
y = int(input("Enter the y-coordinate: "))
if x > 0 and y > 0:
    print("The coordinate point (", x, ",", y, ") lies in the First quadrant")
elif x < 0 and y > 0:
    print("The coordinate point (", x, ",", y, ") lies in the Second quadrant")
elif x < 0 and y < 0:
    print("The coordinate point (", x, ",", y, ") lies in the Third quadrant")
elif x > 0 and y < 0:
    print("The coordinate point (", x, ",", y, ") lies in the Fourth quadrant")
elif x == 0 and y == 0:
    print("The coordinate point (", x, ",", y, ") lies at the origin")
elif x == 0:
    print("The coordinate point (", x, ",", y, ") lies on the y-axis")
else:  # y == 0
    print("The coordinate point (", x, ",", y, ") lies on the x-axis")


# Permutations of n People Occupying r Seats in a Classroom
import math
n = int(input("Enter the number of people: "))
r = int(input("Enter the number of seats: "))
permutations = math.perm(n, r)
print("The number of permutations is:", permutations)


# Combinations of n People Occupying r Seats in a Classroom
import math
n = int(input("Enter the number of people: "))
r = int(input("Enter the number of seats: "))
combinations = math.comb(n, r)
print("The number of combinations is:", combinations)


# Calculate the Area of a Circle
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius * radius
print("The area of the circle is:", area)


# Convert Digit/Number to Words
number = int(input("Enter a number: "))
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
result = ""
for digit in str(number):
    result += words[int(digit)] + " "
print(result.strip())
