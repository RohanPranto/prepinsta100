#take input from the user and remove all the odd int from it

# Taking input from the user
numbers = input("Enter numbers separated by space: ")
numbers = list(map(int, numbers.split()))

# Finding even elements and appending them to a new array
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

# Printing the new array with all even numbers
print("Even numbers:", even_numbers)
