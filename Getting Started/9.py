# python code to find if a number is prime or not

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num): #its not num+1 because You don’t need to check up to num because a number is always divisible by itself.
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number") # 0 and 1 are not prime numbers
