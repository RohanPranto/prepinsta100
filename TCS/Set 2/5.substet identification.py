def is_subset(arr1, arr2):
    for element in arr1:
        if element not in arr2:
            return False
    return True

# Get input from user
arr1 = input("Enter the first array (elements separated by spaces): ")
arr2 = input("Enter the second array (elements separated by spaces): ")

# Convert input strings to lists of integers
arr1 = list(map(int, arr1.split()))
arr2 = list(map(int, arr2.split()))

# Check if arr1 is a subset of arr2
result = is_subset(arr1, arr2)

# Print the result
print(f"Is the first array a subset of the second array? {result}")
