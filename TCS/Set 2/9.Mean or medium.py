#Find Mean and Median of an Unsorted Array

def mean(arr):
    return sum(arr)/len(arr)

def median(arr):
    arr.sort()
    if len(arr)%2==0:
        return (arr[len(arr)//2]+arr[len(arr)//2-1])/2
    else:
        return arr[len(arr)//2]
    
arr = input().split()
arr = [int(x) for x in arr]
print(mean(arr))
print(median(arr))
