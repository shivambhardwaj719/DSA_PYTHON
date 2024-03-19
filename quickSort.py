def quickSort(arr,left,right):
    if left < right:
        partition_pos = partition(arr,left,right)
        quickSort(arr,left,partition_pos - 1)
        quickSort(arr,partition_pos + 1,right)

def partition(arr,left,right):
    i = left
    j = right
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > arr[j]:
        arr[i], arr[right] = arr[right], arr[i]
    return i

arr = [5,3,6,8,11,56,78,4,1,66,44]
quickSort(arr, 0, len(arr)-1)
print(arr)