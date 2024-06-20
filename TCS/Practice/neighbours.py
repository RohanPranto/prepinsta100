array = input("Enter the elements of the array separated by spaces: ")
array = list(map(int, array.split()))

# Variable to store the last peak element found
last_peak = None

# Check for peak elements
for i in range(1, len(array) - 1):
    if array[i] >= array[i - 1] and array[i] >= array[i + 1]:
        last_peak = array[i]

# Check the edge cases
if len(array) > 1:
    if array[0] >= array[1]:
        last_peak = array[0]
    if array[-1] >= array[-2]:
        last_peak = array[-1]

if last_peak is not None:
    print("Peak element:", last_peak)
else:
    print("No peak element found")
