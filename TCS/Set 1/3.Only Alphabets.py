##Remove All Characters Other Than Alphabets

string=input("Enter a string: ")
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
new_string = ""
for i in string:
    if i in alphabets:
        new_string += i

print("New string: ", new_string)