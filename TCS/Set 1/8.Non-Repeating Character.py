##Find Non-Repeating Character in a String

string = input("Enter a string: ")
freq = {}  # Empty dictionary to store the frequency of characters

for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

non_repeating_characters = []
for i in string:
    if freq[i] == 1:
        non_repeating_characters.append(i)

if non_repeating_characters:
    print("Non-repeating characters: ", ' '.join(non_repeating_characters))
else:
    print("No non-repeating characters found.")
