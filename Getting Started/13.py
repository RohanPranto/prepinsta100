##if a number is PALINDROME or not

num = int(input("Enter a number: "))
reversed_num = int(str(num)[::-1])

if num == reversed_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")