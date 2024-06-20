#Positive or negative
number=int(input("Enter a number: "))
if number>0:
    print("The number is positive")
elif number<0:
    print("The number is negative")
else:
    print("The number is zero")




#number is even or odd
Number = int(input("Enter a number: "))
if Number%2==0:
    print("The number is even")
else:
    print("The number is odd")





#sum of first N natural number
n=int(input("Enter a number: "))
sum=0;
for i in range(1, n+1):
    sum=sum+i
print(sum)





#sum of N natural number between two numbers
number1 = int(input("Enter starting number: "))
number2 = int(input("Enter ending number: "))
sum=0
for i in range(number1, number2+1):
    sum+=i
print(sum)





#leap year or not
yr = int(input("Enter a year: "))
if (yr%400==0) or (yr%4==0 and yr%100 != 0):
    print("Leap year")
else:
    print("Not a leap year")





#prime number or not
number = int(input("Enter a number: "))
if number > 1:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
else:
    print(number, "is not a prime number")

    





#factorial of a number
number=int(input("Enter a number: "))
fact=1;
if number ==0:
    print("factorial: 1")
else:
    for i in range(1, number+1):
        fact=fact*i
print(fact)





#fibonacci series
term=int(input("range up to: "))
count=1
a=0
b=1
for i in range(1,term+1):
    print(a)
    c=a+b
    a=b
    b=c
    count+1





#power of a number
number = int(input("Enter a number: "))
power = int(input("Enter power: "))
result=1
for i in range(1, power+1):
    result=result*number
print(result)





#armstrong number is a number that is equal to the sum of cubes of its digits
number = input("Enter a number: ")
length = len(number)
result = 0

for digit in number:
    result += int(digit) ** 3

if result == int(number):
    print(" is an Armstrong number")
else:
    print(" is not an Armstrong number")





#palindrome
string=input("Enter a word: ")
rev=string[::-1]
if string==rev:
    print("palindrome")
else:
    print("No")





#strong number 
import math
number = int(input("Enter a number: "))
# Calculate the sum of factorials of the digits
sum = sum(math.factorial(int(digit)) for digit in str(number))
if sum == number:
    print(number, "is a strong number")
else:
    print(number, " is not a strong number")





#perfect number is a positive integer that is equal to the sum of its proper divisors. for example, 6 is a perfect number because 1+2+3=6 and 1,2,3 are the proper divisors of 6. for example, 28 is a perfect number because 1+2+4+7+14=28 and 1,2,4,7,14 are the proper divisors of 28.

number = int(input("Enter a number: "))
sum = 0
for i in range(1, number):
    if number % i == 0: # for example,number holo 6. so 1,2,3,4,5 obdi iterate hobe. 6%1=0, 6%2=0, 6%3=0, 6%4!=0, 6%5!=0. so 1+2+3=6. so 6 is a perfect number. 
        sum += i
if sum == number:
    print(number, "is a perfect number")
else:
    print(number, "is not a perfect number")





