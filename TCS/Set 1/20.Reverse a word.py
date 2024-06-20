#Reverse Words in a Given String

string = input("Enter a string: ")
# print(string[::-1])
words = string.split() # Split the string into words
words = words[::-1] # Reverse the list of words
string = ' '.join(words) # Join the words with a space

print("Reversed string:", string)