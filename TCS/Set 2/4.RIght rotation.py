#Print Array After It Is Right Rotated K Times

def right_rotate(arr, k):
    n = len(arr)
    # k = k % n #To handle the case when k > n. 
    for i in range(n):
        print(arr[(n - k + i) % n], end = " ")
    print()

arr = input('Enter the array').split()
arr = [int(i) for i in arr] #Converting string array to integer array
k = int(input('Enter the number of times to rotate'))
right_rotate(arr, k)
