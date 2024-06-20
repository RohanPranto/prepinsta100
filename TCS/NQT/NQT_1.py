def brute_force(arr, target):
    n = len(arr)
    for i in range(n):
        cur_sum = 0 # current sum
        for j in range(i, n): # iterate from i to n
            cur_sum += arr[j] #arr[j] means the jth element of the array
            if cur_sum == target:
                print(" ".join(map(str, arr[i:j+1]))) #print the elements from i to j. j+1 means the jth element is not included. if it was j then the jth element would be included.

if __name__ == "__main__":
    arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    target = int(input("Enter the target sum: "))
    brute_force(arr, target)
#the logic of this approach is to iterate through the array and check for the sum of the elements from i to j. If the sum is equal to the target sum, then print the elements from i to j. time complexity of this approach is O(n^2). space complexity is O(1).