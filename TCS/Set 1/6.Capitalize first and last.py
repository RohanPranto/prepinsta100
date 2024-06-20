##Capitalize First and Last Character of Each Word in a Sentence

string = input("Enter a string: ")
words = string.split()
new_string = ""
for word in words:
    new_string += word[0].upper() + word[1:-1].lower() + word[-1].upper() + " " # word[0] is the first character of the word, word[1:-1] is the middle part of the word, word[-1] is the last character of the word
print("New string: ", new_string)
