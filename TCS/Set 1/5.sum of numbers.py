##Sum of Numbers in a String

string = input("Enter a string: ")
sum = 0
for i in string:
    if i.isdigit():
        sum += int(i)

print("Sum of numbers in the string: ", sum)