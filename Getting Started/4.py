num1= int(input("Enter a number: "))
num2= int(input("Enter another number: "))
sum=0
for i in range(num1, num2+1):
    sum+=i
print("Sum from", num1, "to", num2 , "is: " ,sum)