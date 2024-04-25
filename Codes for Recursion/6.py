import math

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = math.gcd(num1, num2) # gcd and hcf same thing

print("The HCF of", num1, "and", num2, "is:", result)
