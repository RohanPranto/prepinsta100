##Find Duplicates in the Input String using

string = input("Enter a string: ")
duplicate_string = ''

for i in string:
    if string.count(i) > 1 and i not in duplicate_string: # Check if the character is repeated more than once and not already in the duplicate_string
        duplicate_string += i

print("Duplicate characters in the string:", duplicate_string)
