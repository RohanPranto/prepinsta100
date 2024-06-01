# python code to find Sum of First N Natural numbers, take input from user

num = int(input("Enter a number: "))
sum = 0
for i in range(1, num+1): #starts from 1, ends just before hiting num+1
    sum += i
print("Sum of First", num, "Natural numbers is:", sum)
