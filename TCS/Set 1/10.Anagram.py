##Check if Strings are Anagrams of Each Other
## Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. for example 'listen' and 'silent' are anagrams of each other.

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if sorted(string1) == sorted(string2):
    print("The strings are anagrams of each other.")
else:
    print("The strings are not anagrams of each other.")

