def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while temp < arr[j] and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr


print(insertionSort([5,1,7,5,1,0,8,9]))

# 时间复杂度: O(n^2)
