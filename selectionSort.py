def selectionSort(arr):
    for i in range(0, len(arr)-1):
        cur_min_idx = 1
        for j in range(i+1,len(arr)):
            if arr[j] < arr[cur_min_idx]:
                cur_min_idx = j
        arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]



arr = [44,334,545,566,3,234,2,1,5,564]
selectionSort(arr)
print(arr)