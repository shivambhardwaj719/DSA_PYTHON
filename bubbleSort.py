def bubbleSort(arr):
    if len(arr) > 1:
        for i in range(len(arr)-1,0,-1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] =   arr[j+1]
                    arr[j+1] = temp


arr = [4,6,2,7,1,6,8,55,77,34,56]
bubbleSort(arr)
print(arr)