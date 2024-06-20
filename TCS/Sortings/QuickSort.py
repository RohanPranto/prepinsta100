def quicksort(arr,low,high):
    if low<high:
        pivot=partition(arr,low,high)
        quicksort(arr,low,pivot-1) #recursive call to left subarray
        quicksort(arr,pivot+1,high) #recursive call to right subarray

def partition(arr,low,high):
    p=arr[low]
    i=low+1
    j=high
    while True:
        while i<=j and arr[i]<=p:
            i+=1
        while i<=j and arr[j]>=p:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break

    arr[low],arr[j]=arr[j],arr[low]
    return j

arr=input("Enter the array: ")
arr=list(map(int,arr.split()))
quicksort(arr,0,len(arr)-1)
print("Sorted array: ",arr)
