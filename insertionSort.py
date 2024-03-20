def insertionSort(arr):
    if len(arr) > 1:
        for i in range(0,len(arr)):
            j = i
            while arr[j-1] > arr[j] and j > 0:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j -= 1

   
arr = [4,5,33,53,56,345,433,3456,90]
insertionSort(arr)
print(arr)