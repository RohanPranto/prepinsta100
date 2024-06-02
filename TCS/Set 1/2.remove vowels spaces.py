##python program to Remove Vowels and Spaces from a String

string=input("Enter a string: ")
vowels = "AEIOUaeiou"
new_string = ""
for i in string:
    if i not in vowels and i != " ":
        new_string += i
print("New string: ", new_string)
