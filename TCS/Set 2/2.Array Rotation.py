#Program for Array Rotation

array = input("Enter the elements of the array separated by spaces: ").split()
n = len(array)
d = int(input("Enter the number of rotations: "))
d = d % n # to handle cases where d > n. For example, if n = 5 and  d = 7, then d = 7 % 5 = 2

array = array[d:] + array[:d] # Slicing the array and concatenating the two parts. [:d] gives the first d elements and [d:] gives the rest of the elements
print("Array after rotation:", array)

# Output:
# Enter the elements of the array separated by spaces: 1 2 3 4 5
# Enter the number of rotations: 2
# Array after rotation: ['3', '4', '5', '1', '2']