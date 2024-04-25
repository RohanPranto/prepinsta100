import math

num1=int(input("Enter the first number: "))
num2=int(input("enter the seccond number: "))

lcm= (num1*num2) // math.gcd(num1,num2)

print("LCM IS", lcm)