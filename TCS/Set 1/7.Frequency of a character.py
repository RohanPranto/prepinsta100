##Frequency of Characters in a String

string = input("Enter a string: ")
freq = {} #Empty dictionary to store frequency of characters
for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Frequency of characters in the string: ", freq)