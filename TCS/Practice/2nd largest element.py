#print the 2nd largest element in an array

array_input = input("Enter an array: ")
array = list(map(int, array_input.split()))

array.sort()  # Sorting the array in ascending order
print("2nd largest element is ", array[-2])  # Accessing the second largest element
