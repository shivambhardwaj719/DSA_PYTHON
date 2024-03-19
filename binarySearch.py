pos = -1
def binarySearch(arr, n):

    l = 0
    u = len(arr) - 1

    while l <= u:
        mid = (l + u) // 2

        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            low = mid+1
        else:
            high = mid-1 

binary = [3,78,44,54,33,102,66,88,23,23]
n = 23
index = binarySearch(arr,n)
if index != -1:
    print("Found at",pos+1)
else:
    print("Not found")