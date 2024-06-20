#Find Equilibrium Index of an Array in Python
# An equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
array = input("Enter the elements of the array separated by spaces: ").split()

# Convert the list of strings into a list of integers
arr = list(map(int, array))

# Find the total sum of the array
total_sum = sum(arr)

# Initialize left_sum and right_sum to 0
left_sum = 0
right_sum = 0

# Iterate through the array to find the equilibrium index
for i in range(len(arr)):
    right_sum = total_sum - left_sum - arr[i]
    if left_sum == right_sum:
        print("Equilibrium index:", i)
        break
    left_sum += arr[i]
else:
    print("No equilibrium index found")

# Output:  
# Enter the elements of the array separated by spaces: -7 1 5 2 -4 3 0
# Equilibrium index: 3