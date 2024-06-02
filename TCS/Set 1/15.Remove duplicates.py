##Remove Duplicates from a Given String

string = input("Enter a string: ")
unique_string = ''
for i in string:
    if i not in unique_string:
        unique_string += i

print("String after removing duplicates:", unique_string)
