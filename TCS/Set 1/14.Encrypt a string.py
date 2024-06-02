##Encrypt the String in python

string = input("Enter a string: ")
encrypted_string = ''
for i in string:
    encrypted_string += chr(ord(i) + 2) ##chr() converts the ASCII value to character

print("Encrypted string:", encrypted_string)