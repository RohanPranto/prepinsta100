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