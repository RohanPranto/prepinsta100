#Find Non-Repeating Elements in an array

from collections import Counter

# Take input from user
input_string = input("Enter the elements of the array separated by spaces: ")

# Split the input string into a list of strings
input_list = input_string.split()

# Convert the list of strings into a list of integers
arr = list(map(int, input_list))

# Count the frequency of each element in the array
element_counts = Counter(arr)

# Extract elements that appear only once
non_repeating_elements = []
for element, count in element_counts.items():
    if count == 1:
        non_repeating_elements.append(element)

# Print the result
print("Non-repeating elements:", non_repeating_elements)

