#python code to find factorial of a number 

number = int(input("Enter the number: "))

if number < 0:
    print("Factorial of negative numbers does not exist")
elif number == 0:
    print("Factorial of 0 is 1")
else:
    fact = 1
    for i in range(1,number+1):
        fact = fact*i
    print("Factorial of",number,"is",fact)

