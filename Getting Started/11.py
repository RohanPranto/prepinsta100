# python code to get the sum of digits of a number

num = int(input("Enter a number: "))
sum = 0
while num > 0:
    sum += num % 10
    num //= 10 # floor division operator, which returns the integer value of the quotient. It dumps the digits after the decimal. and assigns the result to num. we can also use num = num // 10. 
print(f"Sum of digits: {sum}")
