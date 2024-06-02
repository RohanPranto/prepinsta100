#Check if a String is a Substring of Another

string = input("Enter a string: ")
substring = input("Enter a substring: ")

if substring in string:
    print(substring, "is a substring of", string)
else:
    print(substring, "is not a substring of", string)