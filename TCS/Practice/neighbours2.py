def find_peak(arr):
    n = len(arr)
    if n == 0:
        print("No peak element found")
        return

    peak = arr[0]
    i = 1

    while i < n:
        # If current element is greater than peak
        if arr[i] > peak:
            peak = arr[i]
            # If peak is greater than both its neighbors, then it's the peak
            if i == n - 1 or (peak > arr[i + 1] and peak > arr[i - 1]):
                print("Peak element:", peak)
                return
        else:
            i += 1

    print("No peak element found")

# Input
array = input("Enter the elements of the array separated by spaces: ").split()
array = [int(x) for x in array]

find_peak(array)
